from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter


def generate_pdf_report(
    predicted_role,
    skills,
    missing_skills,
    resume_score,
    match_percentage,
    course_recommendations
):

    pdf_path = "report.pdf"

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    elements = []

    # Title
    elements.append(
        Paragraph(
            "SkillSync Engine Report",
            styles['Title']
        )
    )

    elements.append(Spacer(1, 20))

    # Predicted Role
    elements.append(
        Paragraph(
            f"<b>Predicted Role:</b> {predicted_role}",
            styles['BodyText']
        )
    )

    # Resume Score
    elements.append(
        Paragraph(
            f"<b>Resume Score:</b> {resume_score}/100",
            styles['BodyText']
        )
    )

    # Match Percentage
    elements.append(
        Paragraph(
            f"<b>Profile Match:</b> {match_percentage}%",
            styles['BodyText']
        )
    )

    elements.append(Spacer(1, 20))

    # Skills
    elements.append(
        Paragraph(
            "<b>Detected Skills:</b>",
            styles['Heading2']
        )
    )

    for skill in skills:

        elements.append(
            Paragraph(
                f"• {skill}",
                styles['BodyText']
            )
        )

    elements.append(Spacer(1, 20))

    # Missing Skills
    elements.append(
        Paragraph(
            "<b>Missing Skills:</b>",
            styles['Heading2']
        )
    )

    for skill in missing_skills:

        elements.append(
            Paragraph(
                f"• {skill}",
                styles['BodyText']
            )
        )

    elements.append(Spacer(1, 20))

    # Course Recommendations
    elements.append(
        Paragraph(
            "<b>Recommended Courses:</b>",
            styles['Heading2']
        )
    )

    for course in course_recommendations:

        elements.append(
            Paragraph(
                f"{course['Skill']} - "
                f"{course['Course']} "
                f"({course['Platform']})",
                styles['BodyText']
            )
        )

    # Build PDF
    doc.build(elements)

    return pdf_path