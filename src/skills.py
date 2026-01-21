SKILLS = [
    "python", "machine learning", "data analysis", "sql",
    "nlp", "deep learning", "pandas", "numpy",
    "tensorflow", "scikit-learn"
]

def extract_skills(resume, jd):
    matched, missing = [], []

    for skill in SKILLS:
        if skill in resume and skill in jd:
            matched.append(skill)
        elif skill in jd and skill not in resume:
            missing.append(skill)

    return matched, missing
