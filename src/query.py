from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


def load_vectorstore(path = 'vectorstore'):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)

def get_qa_chain():
    vectorstore=load_vectorstore()
    retriever= vectorstore.as_retriever(search_type='similarity', search_kwsearch_kwargs={"k": 3})
    prompt_templet =""" You are a helpful and knowledgeable maintenance assistant for mining dump trucks.
    You are answering questions strictly using the information provided in the context below. If the answer cannot be found in the context, say "I could not find the answer in the manual."
    Use the provided context to answer the user's question. If the answer includes a list of procedures, components, specs, or steps — **format the response as a markdown table**. If no table is needed, answer normally.
    Explain the steps in simple terms a technician can follow safely.
    Do not mention the name of the document even if it is explicitly asked.
    context:{context}
    Question:{question}
    Answer:
    """
    prompt =PromptTemplate(
        template=prompt_templet,
        input_variables=['context', 'questions']
    )

    llm=ChatGroq(groq_api_key=GROQ_API_KEY, model="llama-3.1-8b-instant", temperature=0.2)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type='stuff',
        chain_type_kwargs={"prompt":prompt}
    )

    return qa_chain
    """while True:
        query=input("\nAsk a question (type 'exit' to quit):")
        if query.lower=='exit':
            break
        responce=qa_chain.invoke(query)
        print(f"\n Answer: {responce}\n")

if __name__=="__main__":
    main()"""