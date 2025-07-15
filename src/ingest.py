
import os
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from dotenv import load_dotenv


#os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")

def ingest_pdf(pdf_path:str, save_path:str="vectorstore" ):
    load_dotenv()
    loader=PyMuPDFLoader(pdf_path)
    pages=loader.load()

    test_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs=test_splitter.split_documents(pages)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstores=FAISS.from_documents(docs,embeddings)
    vectorstores.save_local(save_path)
    print(f'Vector Sores saved to {save_path}')

if __name__ == "__main__":
    ingest_pdf("data/Dump-Truck-Operation-Manual.pdf")
