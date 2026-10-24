
def get_learning_recommendations(missing_skills):
    learning_resources = {
        "Python": {
            "what_to_learn": "Variables, loops, functions, data structures, and OOP",
            "resource": "https://docs.python.org/3/tutorial/"
        },
        "SQL": {
            "what_to_learn": "SELECT queries, JOINs, GROUP BY, and subqueries",
            "resource": "https://www.w3schools.com/sql/"
        },
        "Flask": {
            "what_to_learn": "Routes, templates, forms, and REST APIs",
            "resource": "https://flask.palletsprojects.com/en/stable/tutorial/"
        },
        "Django": {
            "what_to_learn": "Models, views, templates, URLs, and forms",
            "resource": "https://docs.djangoproject.com/en/stable/intro/tutorial01/"
        },
        "Machine Learning": {
            "what_to_learn": "Data preprocessing, supervised learning, and model evaluation",
            "resource": "https://scikit-learn.org/stable/getting_started.html"
        },
        "Git": {
            "what_to_learn": "Repositories, commits, branches, and GitHub workflows",
            "resource": "https://git-scm.com/doc"
        },
        "HTML": {
            "what_to_learn": "Elements, forms, semantic HTML, and page structure",
            "resource": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content"
        },
        "CSS": {
            "what_to_learn": "Selectors, box model, Flexbox, Grid, and responsive design",
            "resource": "https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics"
        },
        "JavaScript": {
            "what_to_learn": "Variables, functions, arrays, objects, and DOM manipulation",
            "resource": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"
        },
        "C": {
            "what_to_learn": "Variables, loops, functions, arrays, and pointers",
            "resource": "https://www.learn-c.org/"
        },
        "C++": {
            "what_to_learn": "OOP, STL, classes, inheritance, and algorithms",
            "resource": "https://www.learncpp.com/"
        },
        "Problem Solving": {
            "what_to_learn": "Practice arrays, strings, searching, sorting, and coding challenges",
            "resource": "https://www.hackerrank.com/domains/algorithms"
        },
        "Pandas": {
            "what_to_learn": "DataFrames, data cleaning, filtering, and grouping",
            "resource": "https://pandas.pydata.org/docs/getting_started/"
        },
        "NumPy": {
            "what_to_learn": "Arrays, indexing, vectorized operations, and mathematical functions",
            "resource": "https://numpy.org/doc/stable/user/quickstart.html"
        },
        "Data Analysis": {
            "what_to_learn": "Data cleaning, exploratory analysis, visualization, and interpretation",
            "resource": "https://www.kaggle.com/learn"
        },
        "Artificial Intelligence": {
            "what_to_learn": "AI fundamentals, search, machine learning, and neural networks",
            "resource": "https://www.ibm.com/think/topics/artificial-intelligence"
        },
        "Excel": {
            "what_to_learn": "Formulas, sorting, filtering, charts, and pivot tables",
            "resource": "https://support.microsoft.com/excel"
        },
        "React": {
            "what_to_learn": "Components, props, state, and hooks",
            "resource": "https://react.dev/learn"
        },
        "Communication": {
            "what_to_learn": "Clear explanations, active listening, and professional communication",
            "resource": "https://www.coursera.org/articles/communication-skills"
        }
    }

    recommendations = []

    for skill in missing_skills:
        if skill in learning_resources:
            recommendations.append({
                "skill": skill,
                "what_to_learn": learning_resources[skill]["what_to_learn"],
                "resource": learning_resources[skill]["resource"]
            })
        else:
            recommendations.append({
                "skill": skill,
                "what_to_learn": f"Learn the fundamentals and practice projects related to {skill}",
                "resource": "https://www.google.com/search?q=" + skill.replace(" ", "+") + "+tutorial"
            })

    return recommendations
