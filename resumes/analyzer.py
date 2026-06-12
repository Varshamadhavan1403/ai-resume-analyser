REQUIRED_SKILLS = [
    "Python",
    "Django",
    "REST APIs",
    "POSTGRESQL",
    "MySQL",
    "Docker",
    "Git",
    "Redis",
    "Celery",
    "Linux"
]

class ResumeAnalyzer:
    @staticmethod
    def analyze(skills):
        missing_skills = []
        for skill in REQUIRED_SKILLS:
            if skill not in skills:
                missing_skills.append(skill)
        score = int((len(skills) / len(REQUIRED_SKILLS)) * 100)
        return {
            "score": score,
            "missing_skills": missing_skills
        }