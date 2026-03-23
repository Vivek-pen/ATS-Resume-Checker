# 🚀 Advanced ATS Resume Checker

An AI-powered tool to analyze and optimize your resume for Applicant Tracking Systems (ATS) and improve your job application success rate.

![ATS Resume Checker](https://placehold.co/800x400/e9f5eb/31572c?text=ATS+Resume+Checker&font=montserrat)

## ✨ Features

### Resume Analysis
- **AI-Powered Analysis**: Get intelligent insights using **OpenRouter (GPT-OSS-120B)** for deep analysis.
- **Multiple Analysis Options**: Choose from Quick Scan, Detailed Analysis, ATS Optimization, or Formatting Check.
- **Keyword Matching**: See which keywords from job descriptions match your resume.
- **Visual Feedback**: Resume heatmaps and word clouds visualize your resume's strengths.
- **Industry-Specific Advice**: Get tailored recommendations for your field.
- **Version Tracking**: Save multiple versions to measure improvements over time.

### GitHub Profile Analysis
- **Repository Assessment**: Analyze your GitHub profile to complement your resume.
- **Skills Gap Identification**: See if your GitHub projects showcase skills missing from your resume.
- **Technical Validation**: Demonstrate coding abilities with actual GitHub projects.
- **Language Visualization**: See your programming language distribution and activity patterns.
- **AI-Powered Insights**: Get recommendations on how to improve your GitHub profile using AI.

### Industry Insights
- **Industry-Specific Skills**: View top skills required for various industries.
- **Resume Optimization Tips**: Get tailored advice for your specific industry.
- **ATS Best Practices**: Learn how to format your resume for optimal ATS performance.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vivek-pen/advanced-ats-resume-checker.git
   cd advanced-ats-resume-checker
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # Mac/Linux
    python3 -m venv venv
    source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your API keys:
   ```env
   # OpenRouter API Key for AI Analysis
   API_KEY=your_openrouter_api_key_here
   
   # GitHub Token (Optional, avoids rate limits for GitHub Analysis)
   GITHUB_TOKEN=your_github_personal_access_token
   ```

## 🚀 Usage

1. Start the Streamlit application:
   ```bash
   streamlit run resumeATS.py
   ```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501).

3. Use the tabs to:
   - **Resume Analysis**: Upload PDF and paste Job Description.
   - **GitHub Analyzer**: Analyze a GitHub profile.
   - **Industry Insights**: Get specific advice.

## 📋 How to Use

### Resume Analysis
1. Upload your resume in PDF format.
2. Paste the job description you're applying for.
3. Choose your preferred analysis type:
   - **Quick Scan**: Fast overview.
   - **Detailed Analysis**: Comprehensive breakdown.
   - **ATS Optimization**: Keywords and formatting advice.
   - **Formatting Check**: Layout and structure analysis.
4. Review the results and score.

### GitHub Profile Analyzer
1. Enter your GitHub username.
2. Optionally, use an existing resume from the Resume Analysis tab.
3. Review insights about your repositories, languages, and activity.
4. Use the AI analysis to understand how your GitHub profile complements your resume.

### Industry Insights
1. Select your industry.
2. Review the top skills and tips.

## 🔧 Requirements

- Python 3.7+
- Streamlit
- OpenAI (client for OpenRouter)
- NLTK
- Pandas
- Plotly / Matplotlib
- PyMuPDF / PyPDF2
- Sentence Transformers (BERT)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- **OpenRouter & OpenAI**: For providing the AI capabilities.
- **Streamlit**: For the web application framework.
- **NLTK & HuggingFace**: For NLP and BERT embeddings.
