import re


class InformationExtractor:
    @staticmethod
    def extract_skills(text):
        # A simple regex-based skill extractor (can be improved with NLP techniques)
        skills_pattern = re.compile(r'\b(Python|Java|C\+\+|SQL|JavaScript|Django|React|AWS|Docker|Kubernetes)\b', re.IGNORECASE)
        return list(set(skills_pattern.findall(text)))

    @staticmethod
    def extract_experience(text):
        matches = re.findall(r'(\d+)\s+years?', text, re.IGNORECASE)
        if matches:
            return int(matches[0])
        return 0

    @staticmethod
    def extract_companies(text):

        known_companies = [
            "ABC Technologies Pvt Ltd",
            "Infosys",
            "TCS",
            "Wipro",
            "Accenture",
            "Cognizant",
            "Techversant"
        ]

        companies = []

        for company in known_companies:
            if company.lower() in text.lower():
                companies.append(company)

        return companies

    @staticmethod
    def extract_education(text):
        education = []
        keywords = ['Bachelor', 'Master', 'PhD']
        for keyword in keywords:
            if keyword.lower() in text.lower():
                education.append(keyword)
        # education_pattern = re.compile(r'(Bachelor|Master|PhD)\'?s?\s+in\s+([A-Za-z ]+)', re.IGNORECASE)
        # return education_pattern.findall(text)
        return education