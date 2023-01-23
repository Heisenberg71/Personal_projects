import base64
from difflib import SequenceMatcher
from pathlib import Path
import streamlit as st
from pdfminer.high_level import extract_text

import nltk
nltk.download('punkt')
nltk.download('stopwords')

import math
import re
from collections import Counter

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def extract_skills(input_text, SKILLS_DB):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    word_tokens = nltk.tokenize.word_tokenize(input_text)

    # remove the stop words
    filtered_tokens = [w for w in word_tokens if w not in stop_words]

    # remove the punctuation
    filtered_tokens = [w for w in word_tokens if w.isalpha()]

    # generate bigrams and trigrams (such as artificial intelligence)
    bigrams_trigrams = list(map(' '.join, nltk.everygrams(filtered_tokens, 2, 3)))

    # we create a set to keep the results in.
    found_skills = set()

    # we search for each token in our skills database
    for token in filtered_tokens:
        if token.lower() in SKILLS_DB:
            found_skills.add(token)

    # we search for each bigram and trigram in our skills database
    for ngram in bigrams_trigrams:
        if ngram.lower() in SKILLS_DB:
            found_skills.add(ngram)

    return found_skills

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

uploaded_file_resume = st.file_uploader('Upload Your Resume', type="pdf")

if uploaded_file_resume is not None:
    save_folder = "C:/Users/ASUS/Desktop/AI_Project/uploaded_resumes"
    save_path = Path(save_folder, uploaded_file_resume.name)
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file_resume.getvalue())

    displayPDF(save_path)

    resume_text = extract_text(save_path)
    w.close()
    #st.text(resume_text)

uploaded_file_requirement = st.file_uploader('Upload The Job Requirement', type="pdf")

if uploaded_file_requirement is not None:
    save_folder = "C:/Users/ASUS/Desktop/AI_Project/uploaded_job_requirements"
    save_path = Path(save_folder, uploaded_file_requirement.name)
    with open(save_path, mode='wb') as w:
        w.write(uploaded_file_requirement.getvalue())

    displayPDF(save_path)

    requirement_text = extract_text(save_path)
    w.close()

    skills = extract_skills(resume_text, requirement_text)

    print(skills)

    vector1 = text_to_vector(str(skills))
    vector2 = text_to_vector(requirement_text)

    cosine = get_cosine(vector2, vector1)

    st.text('Resume matched to Job description by ' + str(cosine*100) + '%')
