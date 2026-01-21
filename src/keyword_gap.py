import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

TECH_KEYWORDS = {
    "python", "sql", "pandas", "numpy", "pytorch", "tensorflow",
    "scikit-learn", "machine learning", "deep learning", "nlp",
    "transformer", "bert", "huggingface", "deployment", "docker",
    "api", "rest", "model", "training", "inference", "cloud"
}

def extract_keyword_gap(resume_text, jd_text):
    resume_words = set(resume_text.split())
    jd_words = jd_text.split()

    keyword_gap = {}

    for word in jd_words:
        if (
            word in TECH_KEYWORDS
            and word not in resume_words
        ):
            keyword_gap[word] = keyword_gap.get(word, 0) + 1


    return dict(
        sorted(keyword_gap.items(), key=lambda x: x[1], reverse=True)[:10]
    )


def plot_keyword_gap(keyword_gap):
    """
    Visualizes missing keywords using skill pills and bar chart
    """
    df = pd.DataFrame(
        list(keyword_gap.items()),
        columns=["Keyword", "Frequency"]
    ).sort_values("Frequency", ascending=False)

    if df.empty:
        st.success(
            "No significant keyword gaps found. "
            "Your resume is well aligned with the job description."
        )
        return

    # Skill pills
    st.markdown("### 🔍 Missing Technical Keywords")
    for kw in df["Keyword"][:8]:
        st.markdown(
            f"<span class='skill-pill skill-missing'>{kw.capitalize()}</span>",
            unsafe_allow_html=True
        )

    # Chart
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.barh(df["Keyword"][:6], df["Frequency"][:6])
    ax.invert_yaxis()
    ax.set_xlabel("Importance in Job Description")
    ax.set_title("Top Missing Job Description Keywords")

    st.pyplot(fig)
