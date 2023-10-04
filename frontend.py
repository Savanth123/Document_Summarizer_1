import streamlit as st
import requests
import logging

# Set up logging
logging.basicConfig(
    filename="frontend.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Streamlit UI
st.title("DocBot")

# Upload PDF
st.write("Upload a PDF file:")
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    try:
        response = requests.post("http://54.179.21.212:80/upload-pdf/", files={"file": uploaded_file})
        st.write(response.json())
        logging.info("PDF uploaded and vectors stored successfully")
    except Exception as e:
        st.error(f"Error uploading PDF: {str(e)}")
        logging.error(f"Error uploading PDF: {str(e)}")

# Ask a Question
st.write("Ask a question:")
question = st.text_input("Your question:")
if st.button("Submit"):
    if question:
        try:
            response = requests.post("http://54.179.21.212:80/ask-question/", json={"question": question})
            st.write("Answer:", response.json()["answer"])
            logging.info("Question successfully answered")
        except Exception as e:
            st.error(f"Error asking question: {str(e)}")
            logging.error(f"Error asking question: {str(e)}")
    else:
        st.warning("Please enter a question.")



