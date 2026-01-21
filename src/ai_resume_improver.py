from transformers import pipeline

# Load once (important)
resume_improver = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)

def improve_resume(resume_text, jd_text):
    prompt = f"""
    Improve the following resume to better match the job description.
    Focus on ATS keywords and measurable achievements.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}
    """

    output = resume_improver(prompt)
    return output[0]["generated_text"]
