# Project Overview: Advanced ATS Resume Checker

This document provides a comprehensive overview of the **Advanced ATS Resume Checker** project, designed to help users optimize their resumes for Applicant Tracking Systems (ATS) and improve their job application success rates.

## 1. Project Introduction
The **Advanced ATS Resume Checker** is a sophisticated web application built with **Streamlit** that leverages **Artificial Intelligence (Google Gemini)** and **Natural Language Processing (BERT, NLTK)** to analyze resumes against job descriptions. It provides detailed feedback, scores, and actionable insights to help job seekers land their dream jobs.

## 2. Core Problems Solved
*   **ATS Visibility**: Ensures resumes are readable and keyword-optimized for automated systems.
*   **Content Relevance**: Matches resume content semantically with job descriptions to ensure alignment.
*   **Formatting Errors**: Identifies layout issues that confuse parsers.
*   **Skill Gaps**: Highlights missing skills compared to job requirements.
*   **Developer Assessment**: Analyzes GitHub profiles to get a complete picture of technical candidates.

## 3. Key Features

### A. Intelligent Resume Analysis
*   **PDF Parsing**: Extracts text from PDF resumes accurately using `PyPDF2`.
*   **Multi-Criteria Scoring System**:
    *   **Keyword Match (40%)**: Calculates the percentage of exact keywords from the job description found in the resume.
    *   **Semantic Match (40%)**: Uses **BERT (Bidirectional Encoder Representations from Transformers)** embeddings (`all-MiniLM-L6-v2`) to understand the *meaning* and context of the resume, not just exact words.
    *   **Structure/Formatting Score (20%)**: Evaluates the resume's layout and essential sections ("Experience", "Education", "Skills").
*   **Visual Heatmap**: Generates a heatmap visualization to show which sections of the resume match keywords from the job description.
*   **Word Cloud**: Creates a visual representation of the most frequent words in the resume.

### B. AI-Powered Insights (Google Gemini)
The system uses Google's Gemini Pro model to provide qualitative feedback in four modes:
1.  **Quick Scan**: Identifies the most suitable profession, top 3 strengths, and quick improvements.
2.  **Detailed Analysis**: Provides a deep dive into impact, brevity, style, structure, and skills, with a section-by-section review.
3.  **ATS Optimization**: Suggests keywords to include, reformatting advice, and how to tailor the resume for specific roles.
4.  **Formatting Check**: Detailed analysis of layout, whitespace, bullet points, and potential parsing issues.

### C. Formatting & Structure Checks
*   **Section Detection**: Verifies the presence of key sections like "Experience", "Education", and "Skills".
*   **Bullet Point Consistency**: Checks for consistent use of bullet styles.
*   **Table Detection**: Warns if tables are used (which often break ATS parsers).
*   **Paragraph Length**: Checks for text density and readability.

### D. GitHub Profile Analyzer
*   **Profile Fetching**: Retrieves public profile data (Bio, Followers, Repositories, Stars, Forks) via the GitHub API.
*   **Repository Analysis**: Analyzes top 10 repositories, identifying primary languages used and project descriptions.
*   **Language Distribution**: Visualizes the programming languages used across all repositories.
*   **AI Developer Assessment**: Uses AI to evaluate the GitHub profile's strength, compare it with the resume, and provide specific recommendations for technical roles.

### E. Industry Insights
*   **Automatic Industry Detection**: Classifies the resume into industries like Technology, Healthcare, Finance, Marketing, Education, or Engineering based on keyword density.
*   **Tailored Advice**: Provides specific "Top Skills" and "Resume Tips" relevant to the detected industry.
*   **Skill Recommendations**: Lists essential skills for the selected industry (e.g., "HIPAA Compliance" for Healthcare, "SEO/SEM" for Marketing).

### F. Bulk Resume Comparator (Leaderboard) Experimental
*   **Multi-Resume Upload**: Allows uploading multiple resumes at once to compare against a single job description.
*   **Ranking System**: Ranks candidates based on keyword match percentage.
*   **Visual Analytics**:
    *   **Bar Charts**: Compare match scores across all candidates.
    *   **Distribution Plots**: Show the spread of scores.
    *   **Keyword Frequency**: Shows which keywords are most common across all resumes.
*   **Export Data**: Download analysis results as CSV or Excel.

## 4. Technical Architecture & Tech Stack

### Frontend & UI
*   **Framework**: [Streamlit](https://streamlit.io/) (Python-based web app framework).
*   **Visualization**:
    *   **Plotly**: Interactive heatmaps and charts.
    *   **Matplotlib / Seaborn**: Static statistical charts.
    *   **WordCloud**: Text visualization.

### Backend & Logic
*   **Language**: Python 3.x.
*   **NLP Libraries**:
    *   **NLTK (Natural Language Toolkit)**: Tokenization, stopword removal.
    *   **Sentence Transformers (Hugging Face)**: BERT model for semantic similarity.
*   **AI Integration**:
    *   **Google Gemini API (`google.generativeai`)**: Large Language Model for qualitative analysis.
*   **Data Processing**:
    *   **Pandas**: Data manipulation and analysis.
    *   **PyPDF2**: PDF text extraction.
*   **External APIs**:
    *   **GitHub REST API**: Fetching user profile and repository data.

## 5. User Workflow
1.  **User Uploads Resume**: The user uploads a PDF resume.
2.  **Job Description Input**: Takes the job description text.
3.  **Processing**:
    *   Text is extracted and cleaned.
    *   Industry is detected.
    *   Keywords are matched (Exact Match).
    *   Embeddings are generated and compared (Semantic Match).
4.  **AI Analysis**: The processed text is sent to Gemini with a specific prompt (Analysis/Optimization).
5.  **Output**: Scores, charts, and detailed text feedback are displayed to the user.

## 6. Unique Selling Points (USP)
*   **Hybrid Scoring**: Combines rigid keyword matching with flexible semantic understanding (BERT).
*   **Holistic View**: Integrates GitHub data for a complete view of technical candidates.
*   **Actionable Feedback**: Doesn't just give a score; tells you *how* to improve.
*   **Industry Context**: Adapts advice based on the professional field.
