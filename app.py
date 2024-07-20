import streamlit as st
import google.generativeai as genai
import os
import json
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv()  ## load all the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## Gemini Pro Response
def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text


## Get text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# beautify the Gemini model responses in Streamlit
def beautify_response(response):
    try:
        # Parse the response as JSON
        response_data = json.loads(response)
    except json.JSONDecodeError:
        # If the response is not a valid JSON string, treat it as plain text
        st.subheader("Model Response")
        st.text(response)
        return

    st.title("Resume Analysis Result")

    # Display the job description match percentage
    if "JD Match" in response_data:
        st.markdown(f"### Job Description Match: **{response_data['JD Match']}**")

    # Display the missing keywords
    if "MissingKeywords" in response_data and response_data["MissingKeywords"]:
        st.markdown("#### Missing Keywords:")
        st.markdown(
            "\n".join(
                [f"- **{keyword}**" for keyword in response_data["MissingKeywords"]]
            )
        )
    else:
        st.markdown("#### Missing Keywords:")
        st.markdown("No missing keywords identified.")

    # Display the profile summary
    if "Profile Summary" in response_data and response_data["Profile Summary"]:
        st.markdown("#### Profile Summary:")
        st.markdown(response_data["Profile Summary"])
    else:
        st.markdown("#### Profile Summary:")
        st.markdown("No profile summary provided.")


## Prompt Template

input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
resume_text = st.text_area("Paste your Resume Text Here")
uploaded_file = st.file_uploader(
    "Upload Your Resume", type="pdf", help="Please Upload the pdf"
)

submit = st.button("Submit")

if submit:
    # consider uploaded resume as top choice
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        # st.text(body=text)
        st.text_area(label="Resume Text", value=text, height=500)
        # st.subheader(response)
        beautify_response(response)
    # consider resume text if no file is provided
    elif resume_text is not None:
        # text = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        # st.text(body=text)
        # st.text_area(label="Resume Text", value=resume_text, height=500)
        # st.subheader(response)
        beautify_response(response)
