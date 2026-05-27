def chatbot_response(user_input):

    user_input = user_input.lower()

    # Resume Advice
    if "resume" in user_input:

        return (
            "Improve your resume by adding "
            "projects, technical skills, "
            "certifications, and achievements."
        )

    # Skill Advice
    elif "skill" in user_input:

        return (
            "Focus on Python, SQL, Machine Learning, "
            "Power BI, and communication skills."
        )

    # Interview Advice
    elif "interview" in user_input:

        return (
            "Practice technical questions, "
            "mock interviews, and explain "
            "projects confidently."
        )

    # Career Advice
    elif "career" in user_input:

        return (
            "Build strong projects, improve problem solving, "
            "and stay active on GitHub and LinkedIn."
        )

    # Default
    else:

        return (
            "I can help with resumes, skills, "
            "interview preparation, and career guidance."
        )