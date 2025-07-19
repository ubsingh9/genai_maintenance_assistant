# 🛠️ GenAI Maintenance Assistant

A GenAI-powered RAG chatbot designed to help technicians and engineers interact with the **Dump Truck Operation Manual**. This assistant answers maintenance, repair, safety, and specification-related questions using context-aware AI grounded in the original manual.

![Streamlit App](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png)

---

## 🚀 Live Demo

🔗 [Launch the Assistant on Streamlit](https://genaimaintenanceassistant.streamlit.app/)

---

## 🎯 Use Case

This assistant is tailored for field technicians, shop floor workers, or engineers who want instant answers to:

- Safety instructions  
- Maintenance steps  
- Torque values  
- Hydraulic system procedures  
- Troubleshooting guides  

Instead of scanning a 200+ page manual, users simply ask natural-language questions.

---

## 🧠 Powered By

| Component             | Tech Used |
|----------------------|-----------|
| 🧾 Document Loader    | LangChain `PyPDFLoader` |
| 🔍 Chunking           | `RecursiveCharacterTextSplitter` |
| 📐 Embeddings         | `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`) |
| 🧠 LLM                | `ChatGroq` (via LLaMA or Mixtral) |
| 🗃️ Vector Store       | `FAISS` |
| 💬 UI                 | `Streamlit` |
| ☁️ Deployment         | `Streamlit Cloud` |
| 🔐 API Management     | Streamlit Secrets for `GROQ_API_KEY` |

---

## 🏗️ Project Structure

```
genai-maintenance-assistant/
├── data/                # PDF manual
├── vectorstore/         # FAISS vector DB
├── src/
│   └── query.py         # RAG chain logic (get_qa_chain)
├── ui/
│   └── app.py           # Streamlit chat interface
├── requirements.txt
└── README.md
```

---

## 🧪 Sample Questions to Try

> 🔹 What are the daily maintenance tasks for the dump truck?  
> 🔹 What is the recommended tire pressure for rear wheels?  
> 🔹 What are the safety precautions before working under the dump body?  
> 🔹 How do I reset the transmission system?

---

## 📦 Setup Instructions (Local)

1. **Clone this repo:**
```bash
git clone https://github.com/ubsingh9/genai-maintenance-assistant.git
cd genai-maintenance-assistant
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
streamlit run ui/app.py
```

4. **Configure secrets:**
On local, create a `.env` file or export:
```bash
export GROQ_API_KEY="your-api-key"
```

---

## 💡 Future Enhancements

- [ ] Upload & switch between multiple manuals (CAT, Komatsu, etc.)
- [ ] Add voice input support
- [ ] Add PDF section preview with answers
- [ ] Host on HuggingFace Spaces

---

## 🙋‍♂️ About the Author
Uday Singh
Data Scientist | GenAI Developer | Domain: Mining, Retail, Supply Chain

Connect: [LinkedIn](https://www.linkedin.com/in/udaysingh3/)

Portfolio: *Coming soon*

---

## 📄 License

MIT License