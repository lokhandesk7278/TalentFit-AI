def calculate_skill_priority(skills, jd_text):
    jd_text = jd_text.lower()

    priority = {}
    for skill in skills:
        count = jd_text.count(skill.lower())

        if count >= 3:
            priority[skill] = "High"
        elif count == 2:
            priority[skill] = "Medium"
        elif count == 1:
            priority[skill] = "Low"

    return priority
