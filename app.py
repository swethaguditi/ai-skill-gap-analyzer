
from flask import Flask, render_template, request, make_response

from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.learning_recommender import get_learning_recommendations

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from io import BytesIO
from xml.sax.saxutils import escape


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Check whether a resume was uploaded
    if "resume" not in request.files:
        return "No resume was uploaded.", 400

    resume = request.files["resume"]

    if resume.filename == "":
        return "Please select a resume.", 400

    # Get the job description
    job_description = request.form.get("job_description", "")

    if not job_description.strip():
        return "Please enter a job description.", 400

    try:
        # Step 1: Extract text from the resume PDF
        resume_text = extract_text_from_pdf(resume)

        if not resume_text.strip():
            return "No readable text found in this PDF.", 400

        # Step 2: Extract skills from the resume
        skills = extract_skills(resume_text)

        # Step 3: Extract required skills from the job description
        required_skills = extract_skills(job_description)

        # Step 4: Identify missing skills
        missing_skills = [
            skill for skill in required_skills
            if skill not in skills
        ]

        # Step 5: Generate learning recommendations
        recommendations = get_learning_recommendations(
            missing_skills
        )

        # Step 6: Calculate the skill match percentage
        if required_skills:
            matched_count = (
                len(required_skills) - len(missing_skills)
            )

            match_percentage = round(
                matched_count / len(required_skills) * 100
            )
        else:
            match_percentage = 0

        # Step 7: Display the results page
        return render_template(
            "results.html",
            resume_skills=skills,
            required_skills=required_skills,
            missing_skills=missing_skills,
            match_percentage=match_percentage,
            recommendations=recommendations
        )

    except Exception:
        app.logger.exception("Resume analysis failed")

        return (
            "Could not analyze the resume. "
            "Check the terminal for the error details.",
            500
        )


@app.route("/download-report", methods=["POST"])
def download_report():

    try:
        # Get the analysis data from the form
        match_percentage = int(
            request.form.get("match_percentage", 0)
        )

        resume_skills = request.form.getlist("resume_skills")
        required_skills = request.form.getlist("required_skills")
        missing_skills = request.form.getlist("missing_skills")

        # Validate the report data
        if not 0 <= match_percentage <= 100:
            return "Invalid match percentage.", 400

        if len(missing_skills) > len(required_skills):
            return "Invalid skill data.", 400

        matched_count = (
            len(required_skills) - len(missing_skills)
        )

        # Create an in-memory PDF
        buffer = BytesIO()

        document = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=2 * cm,
            leftMargin=2 * cm,
            topMargin=2 * cm,
            bottomMargin=2 * cm
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "ReportTitle",
            parent=styles["Title"],
            textColor=colors.HexColor("#3730a3"),
            alignment=TA_CENTER,
            spaceAfter=18
        )

        section_style = ParagraphStyle(
            "ReportSection",
            parent=styles["Heading2"],
            textColor=colors.HexColor("#4338ca"),
            spaceBefore=12,
            spaceAfter=8
        )

        normal_style = styles["BodyText"]
        story = []

        # Report title
        story.append(
            Paragraph(
                "AI Skill-Gap Analyzer Report",
                title_style
            )
        )

        story.append(Spacer(1, 8))

        # Match percentage
        story.append(
            Paragraph(
                f"<b>Job Skill Match:</b> {match_percentage}%",
                styles["Heading2"]
            )
        )

        story.append(
            Paragraph(
                f"Matched skills: {matched_count} out of "
                f"{len(required_skills)} required skills.",
                normal_style
            )
        )

        story.append(Spacer(1, 12))

        # Helper function to add skill sections
        def add_skill_section(heading, skills_list):

            story.append(
                Paragraph(heading, section_style)
            )

            if skills_list:
                rows = [
                    [Paragraph(escape(skill), normal_style)]
                    for skill in skills_list
                ]

                table = Table(
                    rows,
                    colWidths=[16 * cm]
                )

                table.setStyle(TableStyle([
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, -1),
                        colors.HexColor("#f5f7ff")
                    ),
                    (
                        "BOX",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.HexColor("#e0e7ff")
                    ),
                    (
                        "INNERGRID",
                        (0, 0),
                        (-1, -1),
                        0.3,
                        colors.HexColor("#e5e7eb")
                    ),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ]))

                story.append(table)

            else:
                story.append(
                    Paragraph("None identified.", normal_style)
                )

            story.append(Spacer(1, 8))

        # Add the three skill sections
        add_skill_section(
            "Skills Found in Your Resume",
            resume_skills
        )

        add_skill_section(
            "Skills Required for the Job",
            required_skills
        )

        add_skill_section(
            "Skills You Need to Learn",
            missing_skills
        )

        # Learning recommendations
        story.append(
            Paragraph(
                "Learning Recommendations",
                section_style
            )
        )

        recommendations = get_learning_recommendations(
            missing_skills
        )

        if recommendations:

            for item in recommendations:
                skill = escape(item["skill"])
                topics = escape(item["what_to_learn"])
                resource = escape(item["resource"])

                story.append(
                    Paragraph(
                        f"<b>{skill}</b>",
                        normal_style
                    )
                )

                story.append(
                    Paragraph(
                        f"What to learn: {topics}",
                        normal_style
                    )
                )

                story.append(
                    Paragraph(
                        f'Resource: <link href="{resource}" '
                        f'color="#4f46e5">{resource}</link>',
                        normal_style
                    )
                )

                story.append(Spacer(1, 8))

        else:
            story.append(
                Paragraph(
                    "No missing skills were identified.",
                    normal_style
                )
            )

        # Generate the PDF
        document.build(story)

        pdf_data = buffer.getvalue()
        buffer.close()

        response = make_response(pdf_data)

        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = (
            'attachment; filename="skill_gap_report.pdf"'
        )

        return response

    except (ValueError, TypeError):
        return "Invalid report data.", 400

    except Exception:
        app.logger.exception("PDF report generation failed")
        return "Could not generate the PDF report.", 500


if __name__ == "__main__":
    app.run(debug=True)
