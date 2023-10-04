# Document_Summarizer_1
An advanced document summarizer powered by LLM (Large Language Model) technology, Langchain, and OpenAI, with efficient data storage through Vector Stores.This repository contains a Document Summarizer project. The frontend allows users to upload a PDF document, while the backend processes the document and provides summarization and question-answering capabilities. Follow the steps below to set up and run the project.

## Prerequisites

- Python 3.7 or higher installed on your local system.
- Access to an EC2 instance for hosting the backend server.
- Access to the internet to install Python libraries and dependencies.
- Basic knowledge of working with Streamlit, FastAPI, and PDF processing in Python.

## Setting up the Backend Server

1. **Create a Virtual Environment on the EC2 Instance**: SSH into your EC2 instance and navigate to the project directory. Create a virtual environment by running:

   ```bash
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**:

   ```bash
   source venv/bin/activate
   ```

3. **Install Python Libraries**: Install the required Python libraries using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Backend Server**: Start the backend server using Uvicorn with the following command:

   ```bash
   uvicorn backend:app --host 0.0.0.0 --port 80 --log-level info --log-config logging_config.ini
   ```

   The server should now be running and listening on port 80.

## Running the Frontend

1. **Install Streamlit**: If you don't have Streamlit installed on your local system, install it using:

   ```bash
   pip install streamlit
   ```

2. **Run the Frontend**: Start the Streamlit frontend script by running the following command from your local system:

   ```bash
   streamlit run frontend.py
   ```

3. **Upload a PDF Document**: Access the frontend in your web browser, and you should see the interface. Upload a PDF document using the provided interface.

4. **Summarization and Question-Answering**: Once the document is successfully uploaded, you will get a positive response once that is done you can ask questions and the LLMs will summarise the pdf and will give the answer. 

## APIs Provided by the Backend

- **Upload PDF API**: The endpoint `/upload-pdf` accepts a PDF file upload and processes the document for summarization and question-answering.

- **Ask Questions API**: The endpoint `/ask-question` allows users to ask questions about the uploaded document. It uses NLP techniques to provide answers based on the content of the document.

## Additional Notes

- In the Frontend code change the API URL address with the server address "http://ec2-instance-server-address/upload-pdf/" 

- Ensure that your EC2 instance has the necessary firewall rules (security groups) to allow incoming traffic on port 80.

- Make sure to properly configure AWS EC2 instance security groups, IAM roles, and permissions for seamless file uploads and interaction with the backend.

- Ensure that the Python environment on your EC2 instance is activated when running the backend server.

- The summarization and question-answering quality may depend on the complexity and content of the uploaded PDF document.

By following these steps, you can set up and run the Document Summarizer project with both the frontend and backend components.
