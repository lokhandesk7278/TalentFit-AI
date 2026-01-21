import streamlit as st
import pandas as pd
import time


from src.text_extraction import extract_text
from src.preprocessing import clean_text
from src.similarity import tfidf_similarity, semantic_similarity
from src.skills import extract_skills
from src.keyword_gap import extract_keyword_gap, plot_keyword_gap
from src.ai_resume_improver import improve_resume
from src.skill_priority import calculate_skill_priority

# ---------------- SESSION STATE INIT ----------------
if "app_loaded" not in st.session_state:
    st.session_state["app_loaded"] = False


import time

if not st.session_state["app_loaded"]:
    loader = st.empty()

    with loader.container():
        st.markdown(
            """
            <div style="
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 70vh;
                text-align: center;
            ">
                <h2>🚀 TalentFit AI</h2>
                <p style="font-size:18px;">
                    Preparing AI models and user interface...
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

    loader.empty()

    # ✅ SET FLAG HERE (IMPORTANT)
    st.session_state["app_loaded"] = True




# =====================================================
# SESSION STATE INITIALIZATION (MUST BE AT TOP)
# =====================================================
if "improved_resume" not in st.session_state:
    st.session_state["improved_resume"] = None

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="TalentFit AI – Resume–Job Fit Analyzer",
    layout="wide"
)

st.markdown(
    """
    <h1 style="text-align: center; margin-bottom: 10px;">
        📄 TalentFit AI – Resume–Job Fit Analyzer
    </h1>
    <p style="text-align: center; font-size: 18px; color: gray;">
        An AI-powered ATS-style resume and job description matching system
    </p>
    """,
    unsafe_allow_html=True
)


# =====================================================
# FILE UPLOAD
# =====================================================
col1, col2 = st.columns(2)
resume_file = col1.file_uploader("Upload Resume", ["pdf", "docx", "txt"])
jd_file = col2.file_uploader("Upload Job Description", ["pdf", "docx", "txt"])

# =====================================================
# ANALYZE BUTTON
# =====================================================
if st.button("Analyze Resume"):

    if not resume_file or not jd_file:
        st.error("Please upload both Resume and Job Description.")
        st.stop()

    resume_text = clean_text(extract_text(resume_file))
    jd_text = clean_text(extract_text(jd_file))

    with st.spinner("Analyzing using AI models..."):
        tfidf_score = tfidf_similarity(resume_text, jd_text)
        semantic_score = semantic_similarity(resume_text, jd_text)

        matched, missing = extract_skills(resume_text, jd_text)
        keyword_gap = extract_keyword_gap(resume_text, jd_text)
        skill_priority = calculate_skill_priority(matched + missing, jd_text)

    # =================================================
    # TABS
    # =================================================
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📊 Match",
            "🧠 Skills",
            "📈 Keyword Gap",
            "🧠 Explainability",
            "✍ AI Resume Improvement",
        ]
    )

    # =================================================
    # TAB 1: MATCH
    # =================================================
    with tab1:
        st.metric("TF-IDF Score", f"{round(tfidf_score, 2)}%")
        st.metric("Semantic Score (Hugging Face)", f"{round(semantic_score, 2)}%")

        st.markdown("---")
        st.subheader("ℹ️ How to interpret these scores")

        st.markdown("""
    **TF-IDF Score**  
    This score represents keyword similarity between the resume and the job description.
    It measures how many important words overlap, but it does not understand meaning.
    Traditional ATS systems rely heavily on this approach.

    **Semantic Score (Hugging Face)**  
    This score measures contextual similarity using a transformer-based AI model.
    It understands meaning, synonyms, and intent, even if exact keywords differ.
    Modern ATS systems increasingly use semantic matching.

    **Why the scores are different:**  
    A resume may use different wording while still being a strong match.
    That is why the semantic score is often higher and more reliable.
    """)

        if semantic_score > tfidf_score:
            st.success(
            "✅ Your resume aligns well in meaning with the job description, "
            "even if some exact keywords are missing."
        )
        else:
            st.warning(
            "⚠️ Your resume may need better keyword alignment "
            "to perform well in traditional ATS systems."
        )

    # =================================================
    # TAB 2: SKILL PRIORITY
    # =================================================
    with tab2:
        st.subheader("🧠 Skill Analysis with Priority")

        if not skill_priority:
            st.info("No skills detected for priority analysis.")
        else:
            for skill, level in skill_priority.items():
                if level == "High":
                    st.error(f"{skill} – HIGH Priority")
                elif level == "Medium":
                    st.warning(f"{skill} – Medium Priority")
                else:
                    st.info(f"{skill} – Low Priority")

    # =================================================
    # TAB 3: KEYWORD GAP
    # =================================================
    with tab3:
        st.subheader("🔍 Keyword Gap Analysis")

        if not keyword_gap:
            st.success(
                "No significant keyword gaps found. "
                "Your resume is well aligned with the job description."
            )
        else:
            plot_keyword_gap(keyword_gap)

    # =================================================
    # TAB 4: EXPLAINABILITY
    # =================================================
    with tab4:
        st.subheader("🧠 ATS Explainability")

        if semantic_score < 60:
            st.warning("Low resume–job alignment detected.")
        else:
            st.success("Good semantic alignment detected.")

        st.markdown("""
        ### Why this score?
        - Semantic similarity measures contextual meaning, not just keywords
        - Missing high-priority skills reduce ATS ranking
        - Keyword gaps reduce contextual alignment
        """)

        st.markdown("### What to improve first:")
        if missing:
            st.write(f"Add or highlight these skills: {', '.join(missing[:5])}")
        else:
            st.write("Improve wording and quantify achievements.")

    # =================================================
    # TAB 5: AI RESUME IMPROVEMENT (HUGGING FACE)
    # =================================================
    with tab5:
        st.subheader("✍ AI-Guided Resume Improvement Suggestions")

        suggestions = []

        if semantic_score < 70:
            suggestions.append(
            "Improve alignment by rewriting experience using job description terminology."
        )

        if missing:
            suggestions.append(
            f"Add or highlight these missing skills: {', '.join(missing[:5])}."
        )

        if tfidf_score < semantic_score:
            suggestions.append(
            "Increase keyword overlap to improve performance in traditional ATS systems."
        )

            suggestions.append(
        "Use measurable achievements (e.g., percentages, impact, metrics) in experience bullets."
    )

            suggestions.append(
        "Ensure project descriptions clearly mention tools, models, and outcomes."
    )

        for s in suggestions:
            st.info("• " + s)

