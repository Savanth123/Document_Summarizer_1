import os
import sys
import logging
from fastapi import FastAPI, File, UploadFile
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter

# Set up logging
logging.basicConfig(
    filename="server.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)



# Hardcoded OpenAI API key
OPENAI_API_KEY = ""


app = FastAPI()

chat_history = []  # Initialize chat memory

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile):
    try:
        # Initialize Langchain components
        loader = PyPDFLoader(file)
        documents = loader.load()

        # Split the documents into smaller chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
        documents = text_splitter.split_documents(documents)

        # Convert the document chunks to embeddings and save them to the vector store
        vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(api_key=OPENAI_API_KEY), persist_directory="./data")
        vectordb.persist()

        # # Create a Q&A chain
        # pdf_qa = ConversationalRetrievalChain.from_llm(
            # ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo'),
            # retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
            # return_source_documents=True,
            # verbose=False
        # )

        # Handle PDF file upload and vectorization here
        # Store the vectors in the vector store

        # Log success
        logging.info("PDF uploaded and vectors stored successfully")
        
        return {"message": "PDF uploaded and vectors stored successfully"}

    except Exception as e:
        # Log the error
        logging.error(f"Error in /upload-pdf/ endpoint: {str(e)}")
        return {"error": str(e)}

@app.post("/ask-question/")
async def ask_question(question: str):
    try:
        # Initialize Langchain components
        # loader = PyPDFLoader()
        # documents = loader.load()

        # # Split the documents into smaller chunks
        # text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
        # documents = text_splitter.split_documents(documents)

        # # Convert the document chunks to embeddings and save them to the vector store
        # vectordb = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(api_key=OPENAI_API_KEY), persist_directory="./data")
        # vectordb.persist()

        # Create a Q&A chain
        pdf_qa = ConversationalRetrievalChain.from_llm(
            ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo'),
            retriever=vectordb.as_retriever(search_kwargs={'k': 6}),
            return_source_documents=True,
            verbose=False
        )

        # Use the Langchain Q&A chain to answer the question
        result = pdf_qa(
            {"question": question, "chat_history": chat_history}
        )

        # Log success
        logging.info("Question successfully answered")

        # Append the question and answer to chat memory
        chat_history.append((question, result["answer"]))

        # Return the answer
        return {"answer": result["answer"]}

    except Exception as e:
        # Log the error
        logging.error(f"Error in /ask-question/ endpoint: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)

