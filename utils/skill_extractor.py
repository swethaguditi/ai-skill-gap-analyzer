
import re


SKILL_VARIATIONS = {
    "Python": ["python", "python programming"],
    "Java": ["java", "java programming"],
    "C": ["c programming", "c language"],
    "C++": ["c++", "cpp"],
    "SQL": ["sql", "structured query language"],
    "HTML": ["html", "hypertext markup language"],
    "CSS": ["css", "cascading style sheets"],
    "JavaScript": ["javascript", "java script", "js"],
    "Flask": ["flask", "flask framework"],
    "Django": ["django", "django framework"],
    "Machine Learning": [
        "machine learning",
        "ml",
        "machine-learning"
    ],
    "Artificial Intelligence": [
        "artificial intelligence",
        "ai",
        "artificial intelligence systems"
    ],
    "Data Analysis": [
        "data analysis",
        "data analytics",
        "analyzing data",
        "analysing data"
    ],
    "Pandas": ["pandas", "python pandas"],
    "NumPy": ["numpy", "numerical python"],
    "Excel": ["excel", "microsoft excel", "ms excel"],
    "Git": ["git", "git version control"],
    "React": ["react", "react.js", "reactjs"],
    "Communication": [
        "communication",
        "communication skills",
        "verbal communication"
    ],
    "Problem Solving": [
        "problem solving",
        "problem-solving",
        "problem solving skills"
    ],
    "Database Management": [
        "database management",
        "database management systems",
        "dbms"
    ],
}


def extract_skills(resume_text):
    found_skills = []
    text = resume_text.lower()

    for skill, variations in SKILL_VARIATIONS.items():
        for variation in variations:
            pattern = (
                r"(?<!\w)"
                + re.escape(variation)
                + r"(?!\w)"
            )

            if re.search(pattern, text):
                found_skills.append(skill)
                break

    return found_skills
