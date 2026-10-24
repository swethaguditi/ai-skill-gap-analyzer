
# AI Skill-Gap Analyzer

## Project Overview

AI Skill-Gap Analyzer is a Python-based web application that helps students identify the skills they already have and the skills they need to learn for a target job role.

Users upload their resume in PDF format and enter a job description. The application extracts skills, compares them with job requirements, calculates a skill-match percentage, and recommends learning resources for missing skills.

## Features

- Upload resumes in PDF format.
- Extract text from resumes.
- Identify skills in resumes and job descriptions.
- Calculate the job skill-match percentage.
- Display matched and missing skills.
- Visualize skill gaps using an interactive chart.
- Recommend learning resources for missing skills.
- Download a PDF analysis report.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- PyMuPDF
- ReportLab
- Chart.js

## How It Works

1. The user uploads a PDF resume.
2. The application extracts text from the resume.
3. Skills are identified in the resume and job description.
4. The application compares the identified skills.
5. A skill-match percentage is calculated.
6. Matched skills, missing skills, and learning recommendations are displayed.
7. The user can download the analysis report as a PDF.

## Installation and Setup

### Prerequisites

- Python 3.11 or compatible version
- pip

### Run the Project on Windows

1. Open the project folder in VS Code.
2. Open the terminal.
3. Activate the virtual environment:

   .\venvv\Scripts\Activate.ps1

4. Install the required packages if needed:

   pip install Flask PyMuPDF reportlab

5. Start the application:

   python app.py

6. Open this address in your browser:

   http://127.0.0.1:5000

## Project Purpose

This project helps students understand the difference between their current skills and the skills required for a target job. It provides learning recommendations to help them prepare for job opportunities.

## Future Enhancements

- Save previous analyses in a database.
- Support more skills and job roles.
- Improve skill extraction.
- Compare skills against multiple job descriptions.
