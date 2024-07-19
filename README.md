# ATS-Resume-Scorer

## Overview

ATS Resume Scorer is a Streamlit-based web application designed to help users improve their resumes by evaluating them against job descriptions using Google's Gemini Pro model. This tool acts as an ATS (Applicant Tracking System) to assess the match percentage, identify missing keywords, and provide a profile summary for better job application results.

## Features

- **Resume Analysis:** Upload your resume in PDF format and get it evaluated against a job description.
- **Job Description Matching:** The tool provides a match percentage based on the job description.
- **Keyword Identification:** It highlights missing keywords that could improve the resume.
- **Profile Summary:** A concise summary is generated to help users understand their profile's strengths and areas for improvement.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ATS-Resume-Scorer.git
   cd ATS-Resume-Scorer```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    - Create a .env file in the project directory.
    - Add your Google API key to the .env file:

    ```bash
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. Run the Streamlit app:

```bash
    streamlit run app.py
```

2. Open your web browser and go to <http://localhost:8501>.

3. Paste the job description in the provided text area.

4. Upload your resume in PDF format.

5. Click the "Submit" button to get the analysis.

## Project Structure

```bash
ATS-Resume-Scorer/
├── .env
├── app.py
├── requirements.txt
└── README.md
```

## Dependencies

- Streamlit
- Google Generative AI (Gemini Pro)
- PyPDF2
- python-dotenv

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to the existing coding standards and includes appropriate tests.

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for more details.

## Acknowledgments

Thanks to Streamlit for providing an easy-to-use framework for web applications.
Thanks to Google Generative AI for the powerful text generation capabilities.
