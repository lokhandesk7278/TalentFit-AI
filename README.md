
# TalentFit AI – Resume–Job Fit Analyzer

**TalentFit AI** is an AI-powered Resume–Job Fit Analyzer that simulates how modern Applicant Tracking Systems (ATS) evaluate resumes.
It uses **Natural Language Processing (NLP)** and **Hugging Face transformer models** to provide explainable match scores, skill gap analysis, and AI-driven resume improvement suggestions.

---

## 🚀 Features

* Resume and Job Description analysis (PDF / DOCX / TXT)
* Dual ATS scoring:

  * **TF-IDF Score** (Traditional keyword-based ATS)
  * **Semantic Score** (Hugging Face transformer-based)
* Skill matching and priority classification
* Keyword gap visualization
* AI-powered resume improvement suggestions
* Explainable ATS insights
* Interactive Streamlit dashboard

---

## 🧠 Technologies Used

* Python
* Streamlit
* Scikit-learn
* Hugging Face Transformers
* Sentence Transformers
* PyPDF2, python-docx
* Matplotlib, Pandas

---

## 📂 Project Structure

```
talentfit-ai/
│
├── app.py
├── requirements.txt
├── src/
│   ├── text_extraction.py
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── skills.py
│   ├── keyword_gap.py
│   ├── ai_resume_improver.py
│   └── skill_priority.py
│
├── samples/
│   ├── sample_resume.txt
│   └── sample_jd.txt
│
└── README.md
```

---

## 🛠 How It Works

1. User uploads a Resume and Job Description
2. Text is extracted and preprocessed
3. Similarity analysis is performed using:

   * TF-IDF (keyword-based)
   * Semantic embeddings (transformer-based)
4. Skills and keyword gaps are identified
5. AI model generates ATS-optimized resume suggestions
6. Results are displayed through a multi-tab dashboard

---

## ▶️ Running the App Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## 📌 Sample Data

Sample resume and job description files are provided in the `samples/` folder for demonstration and testing purposes.
All sample data is **fictional** and used only for educational purposes.


---

## ⚖️ License

This project is licensed under the **MIT License**.

---

## 👤 Author

Shravani Lokhande
AI / ML Intern

---

## 🔮 Future Enhancements

* Resume score comparison (Before vs After AI improvement)
* Multi-job role matching
* Resume analytics dashboard
* Multilingual resume support
* AI-powered interview preparation

---

⭐ *If you find this project useful, feel free to explore or fork it.*
