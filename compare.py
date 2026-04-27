import re

# -------- SKILL WEIGHTS -------- #
SKILL_WEIGHTS = {
    "python": 2,
    "machine learning": 3,
    "data science": 3,
    "deep learning": 3,
    "nlp": 3,
    "sql": 2,
    "java": 2,
    "ai": 2,
    "excel": 1,
    "data analysis": 2,
    "hadoop": 2
}

# -------- FEATURE EXTRACTION -------- #
def extract_features(text):
    text = text.lower()

    # -------- EXPERIENCE -------- #
    exp_matches = re.findall(r'(\d+)\s*(?:years|yrs)', text)
    experience = max([int(x) for x in exp_matches]) if exp_matches else 0

    # -------- EDUCATION -------- #
    education_score = 0
    if "phd" in text:
        education_score = 5
    elif "m.tech" in text or "master" in text:
        education_score = 4
    elif "b.tech" in text or "bachelor" in text:
        education_score = 3

    # -------- SKILLS -------- #
    skill_score = 0
    for skill, weight in SKILL_WEIGHTS.items():
        if skill in text:
            skill_score += weight

    # -------- PROJECTS -------- #
    project_count = len(re.findall(r'project', text))

    # -------- CERTIFICATIONS -------- #
    cert_count = len(re.findall(r'certified|certificate', text))

    return {
        "experience": experience,
        "education": education_score,
        "skills": skill_score,
        "projects": project_count,
        "certifications": cert_count
    }


# -------- SCORING FUNCTION -------- #
def compute_score(f):
    # Normalize (avoid one feature dominating)
    exp_score = min(f["experience"] / 10, 1) * 10
    skill_score = min(f["skills"] / 10, 1) * 10
    project_score = min(f["projects"] / 5, 1) * 5
    cert_score = min(f["certifications"] / 5, 1) * 5
    edu_score = f["education"]

    total = (
        3 * exp_score +
        2 * skill_score +
        1.5 * project_score +
        1 * cert_score +
        2 * edu_score
    )

    return round(total, 2)


# -------- MAIN COMPARISON -------- #
def compare_resumes(text1, text2):
    f1 = extract_features(text1)
    f2 = extract_features(text2)

    s1 = compute_score(f1)
    s2 = compute_score(f2)

    return f1, f2, s1, s2