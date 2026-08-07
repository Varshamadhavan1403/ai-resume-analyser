class JobMatcher:
    @staticmethod
    def match(resume_skills, required_skills):
        matched_skills = []
        missing_skills = []
        resume_skills_lower = [skill.lower() for skill in resume_skills]

        for skill in required_skills:
            if skill.lower() in resume_skills_lower:
                matched_skills.append(skill)
            else:
                missing_skills.append(skill)

        if len(required_skills) > 0:
            match_percentage = int(len(matched_skills) / len(required_skills) * 100)
        else:
            match_percentage = 0
        return {
            'matched_skills': matched_skills,
            'missing_skills': missing_skills,
            'match_percentage': match_percentage
        }