import streamlit as st
import pdfplumber
import pandas as pd
import spacy
import plotly.express as px

from job_predictor import predict_job_role
from recommendation import analyze_skill_gap
from resume_score import calculate_resume_score
from course_recommender import recommend_courses
from pdf_generator import generate_pdf_report
from interview_generator import generate_interview_questions
from ats_checker import calculate_ats_score
from chatbot import chatbot_response
from roadmap import generate_roadmap
from auth import register_user, login_user

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="SkillSync Engine",
    page_icon="🚀",
    layout="wide"
)


# ---------------- SESSION STATE ----------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------------- LOAD NLP ----------------

nlp = spacy.load("en_core_web_sm")

# ---------------- LOAD DATA ----------------

skills_df = pd.read_csv("data/skills.csv")
skills_list = skills_df["Skill"].tolist()

# ---------------- CUSTOM CSS ----------------

st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Segoe UI';
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    .block-container {
        padding-top: 2rem;
    }

    h1, h2, h3 {
        color: white;
    }

    .metric-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 1px solid #00ffd5;
    }

    .stButton>button {
        background-color: #00ffd5;
        color: black;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }

    div[data-testid="metric-container"] {
        background-color: #1e293b;
        border: 1px solid #00ffd5;
        padding: 15px;
        border-radius: 15px;
    }

    textarea {
        background-color: #1e293b !important;
        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------

st.sidebar.title("🚀 SkillSync Engine")

st.sidebar.markdown("---")

st.sidebar.subheader("User Authentication")

auth_option = st.sidebar.selectbox(
    "Choose Option",
    ["Login", "Register"]
)

username = st.sidebar.text_input(
    "Username"
)

password = st.sidebar.text_input(
    "Password",
    type="password"
)

# ---------------- REGISTER ----------------

if auth_option == "Register":

    if st.sidebar.button("Register"):

        success = register_user(
            username,
            password
        )

        if success:

            st.sidebar.success(
                "Registration Successful!"
            )

        else:

            st.sidebar.error(
                "Username already exists."
            )

# ---------------- LOGIN ----------------

elif auth_option == "Login":

    if st.sidebar.button("Login"):

        authenticated = login_user(
            username,
            password
        )

        if authenticated:

            st.session_state.authenticated = True

            st.sidebar.success(
                "Login Successful!"
            )

        else:

            st.sidebar.error(
                "Invalid Credentials"
            )

st.sidebar.markdown("---")

st.sidebar.info(
    """
    ### Features

    ✅ Resume Analysis  
    ✅ ATS Resume Checker  
    ✅ Skill Extraction  
    ✅ Job Prediction  
    ✅ Skill Gap Analysis  
    ✅ Course Recommendations  
    ✅ AI Interview Questions  
    ✅ Skill Roadmap  
    ✅ AI Career Chatbot  
    """
)

# ---------------- HERO SECTION ----------------

st.title("🚀 SkillSync Engine")

st.subheader("AI-Powered Career Recommendation System")

st.write(
    """
Analyze resumes, predict careers, identify skill gaps,
and recommend personalized learning paths using AI.
"""
)

# ---------------- FILE UPLOAD ----------------

uploaded_file = st.file_uploader(
    "📄 Upload Your Resume (PDF)",
    type=["pdf"]
)
# ---------------- PDF EXTRACTION ----------------

def extract_text_from_pdf(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text

# ---------------- SKILL EXTRACTION ----------------

def extract_skills(resume_text):

    detected_skills = []

    resume_text_lower = resume_text.lower()

    for skill in skills_list:

        if skill.lower() in resume_text_lower:

            detected_skills.append(skill)

    return list(set(detected_skills))

# ---------------- MAIN APPLICATION ----------------

if st.session_state.authenticated:

    if uploaded_file is not None:

        st.success("✅ Resume Uploaded Successfully!")

        # Extract Resume Text
        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        # Extract Skills
        skills = extract_skills(
            resume_text
        )

        # Predict Role
        predicted_role = predict_job_role(
            skills
        )

        # Skill Gap
        required_skills, missing_skills, match_percentage = analyze_skill_gap(
            predicted_role,
            skills
        )

        # ATS Score
        ats_score, ats_suggestions = calculate_ats_score(
            skills,
            required_skills,
            resume_text
        )

        # Resume Score
        resume_score = calculate_resume_score(
            skills,
            missing_skills,
            match_percentage
        )

        # Course Recommendations
        course_recommendations = recommend_courses(
            missing_skills
        )

        # Interview Questions
        interview_questions = generate_interview_questions(
            predicted_role
        )

        # Roadmap
        roadmap = generate_roadmap(
            predicted_role
        )

        # ---------------- DASHBOARD ----------------

        st.markdown("## 📊 Dashboard")

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Skills",
                len(skills)
            )

        with col2:

            st.metric(
                "Missing Skills",
                len(missing_skills)
            )

        with col3:

            st.metric(
                "ATS Score",
                f"{ats_score}%"
            )

        with col4:

            st.metric(
                "Resume Score",
                f"{resume_score}/100"
            )

        st.divider()

        # ---------------- TABS ----------------

        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📄 Resume",
            "🧠 Skills",
            "📊 ATS",
            "📘 Courses",
            "🎯 Interview",
            "🛣️ Roadmap"
        ])

        # ---------------- RESUME TAB ----------------

        with tab1:

            st.subheader("Predicted Job Role")

            st.success(predicted_role)

            st.subheader("Resume Content")

            st.text_area(
                "Resume",
                resume_text,
                height=350
            )

        # ---------------- SKILLS TAB ----------------

        with tab2:

            st.subheader("Detected Skills")

            if skills:

                for skill in skills:

                    st.write(f"✅ {skill}")

                skill_data = {
                    "Skills": skills,
                    "Count": [1] * len(skills)
                }

                fig = px.bar(
                    skill_data,
                    x="Skills",
                    y="Count",
                    title="Detected Skills"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            st.subheader("Missing Skills")

            if missing_skills:

                for skill in missing_skills:

                    st.write(f"❌ {skill}")

            else:

                st.success(
                    "No Missing Skills"
                )

        # ---------------- ATS TAB ----------------

        with tab3:

            st.subheader("ATS Resume Checker")

            st.metric(
                "ATS Score",
                f"{ats_score}%"
            )

            st.progress(
                ats_score / 100
            )

            st.subheader("ATS Suggestions")

            if ats_suggestions:

                for suggestion in ats_suggestions:

                    st.write(f"⚠️ {suggestion}")

            else:

                st.success(
                    "Resume is ATS Optimized!"
                )

        # ---------------- COURSES TAB ----------------

        with tab4:

            st.subheader("Recommended Courses")

            if course_recommendations:

                for course in course_recommendations:

                    st.markdown(
                        f"""
                        ### 📘 {course['Skill']}

                        **Course:** {course['Course']}

                        **Platform:** {course['Platform']}
                        """
                    )

                    st.divider()

            else:

                st.success(
                    "No Courses Needed"
                )

        # ---------------- INTERVIEW TAB ----------------

        with tab5:

            st.subheader("AI Interview Questions")

            if interview_questions:

                for question in interview_questions:

                    st.write(f"🎯 {question}")

        # ---------------- ROADMAP TAB ----------------

        with tab6:

            st.subheader("Skill Roadmap")

            for step, skill in enumerate(
                roadmap,
                start=1
            ):

                st.write(
                    f"{step}. {skill}"
                )

        # ---------------- PDF REPORT ----------------

        st.divider()

        pdf_file = generate_pdf_report(
            predicted_role,
            skills,
            missing_skills,
            resume_score,
            match_percentage,
            course_recommendations
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📥 Download Full PDF Report",
                data=file,
                file_name="SkillSync_Report.pdf",
                mime="application/pdf",
                key="pdf_download"
            )

else:

    st.warning(
        "⚠️ Please login to use the platform."
    )

# ---------------- AI CHATBOT ----------------

st.divider()

st.subheader("🤖 AI Career Chatbot")

user_question = st.text_input(
    "Ask Career Questions"
)

if user_question:

    response = chatbot_response(
        user_question
    )

    st.success(response)

# ---------------- FOOTER ----------------

st.markdown(
    """
    <hr>

    <center>

    Developed with ❤️ using Python,
    NLP, Machine Learning & Streamlit

    </center>
    """,
    unsafe_allow_html=True
)