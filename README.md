# CAT 777F GenAI Maintenance Assistant

A GenAI-powered assistant built using LangChain, FAISS, and OpenAI to help field technicians query maintenance manuals (e.g., CAT 777F).

## Features
- Ingests large PDF manuals
- Semantic search using embeddings
- Retrieval-Augmented Generation (RAG) pipeline
- Gradio UI (coming soon)

## Project Structure
- `src/` - Source code
- `data/` - Manuals or documents
- `vectorstore/` - FAISS saved embeddings
- `.env` - API keys

## Setup
```bash
pip install -r requirements.txt
python src/ingest.py
