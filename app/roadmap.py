def generate_roadmap(role):

    roadmaps = {

        "Data Scientist": [
            "Python",
            "SQL",
            "Statistics",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Model Deployment"
        ],

        "Data Analyst": [
            "Excel",
            "SQL",
            "Python",
            "Power BI",
            "Tableau",
            "Statistics"
        ],

        "Machine Learning Engineer": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "MLOps",
            "Deployment"
        ],

        "Python Developer": [
            "Python Basics",
            "OOP",
            "Flask/Django",
            "APIs",
            "Database",
            "Deployment"
        ],

        "Full Stack Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "MongoDB",
            "Deployment"
        ]
    }

    return roadmaps.get(
        role,
        ["No roadmap available."]
    )