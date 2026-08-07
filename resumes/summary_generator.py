class SummaryGenerator:
    @staticmethod
    def generate_summary(resume):
        skills = ", ".join(resume.extracted_skills[:5])
        return(
            f"Candidate has "
            f"{resume.experience_years} years of experience."
            f"Key skills include {skills}. "
            f"Highest Qualification:"
            f"{', '.join(resume.education)}." 
            f"Resume Score: {resume.score}%."
        )
    