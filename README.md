# ✈️ Aviation RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) assistant designed to answer aviation-related questions using a curated aviation knowledge base.

The assistant retrieves relevant information from aviation documents before generating an answer using a Large Language Model (LLM). This approach helps provide responses that are grounded in the available documents.

This project was developed as part of the **Ready Tensor AI Developer Certification Program**.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Quick start](#quick-start)
- [Features](#features)
- [How the RAG System Works](#how-the-rag-system-works)
- [Knowledge Base & Chunking](#knowledge-base--chunking)
- [Retrieval Evaluation](#retrieval-evaluation)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Environment Variables](#installation--environment-variables)
- [Build the Vector Database](#build-the-vector-database)
- [Run the Application](#run-the-application)
- [Run Retrieval Evaluation](#run-retrieval-evaluation)
- [Inspect Chunk Metadata](#inspect-chunk-metadata)
- [Future Improvements](#future-improvements)
- [Responsible Use and Limitations](#responsible-use-and-limitations)
- [Author & License](#author--license)


## 📌 Project Overview

The Aviation RAG Assistant allows users to ask aviation-related questions in natural language and receive answers based on information contained in a curated knowledge base. The knowledge base covers topics including airport operations, air traffic management, safety management systems, ARFF, airport security, aviation meteorology, Kenya's aviation industry, and more.

The system uses semantic similarity search to identify relevant document chunks and provides those chunks as context to a language model so answers are grounded in source material.


## 🎯 Quick start

Clone, create a virtual environment, install dependencies, ingest documents, and run the app:

```bash
git clone https://github.com/Lengerpei/Aviation-RAG-assistant.git
cd Aviation-RAG-assistant
python -m venv .venv            # Windows: python -m venv .venv
# Activate the virtualenv:
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
# Create a .env (see .env.example) and set GROQ_API_KEY and any other required vars
python -m src.ingest           # build the Chroma vector DB
streamlit run src/app.py       # start the Streamlit UI
```


## ✨ Features

- Aviation-focused question answering
- Retrieval-Augmented Generation (RAG)
- Semantic similarity search
- Document-based responses with source-aware chunk metadata
- Hugging Face embeddings
- ChromaDB vector database
- Groq language model
- Streamlit user interface
- Configurable text chunking (chunk size & overlap)
- Retrieval evaluation (Recall@1/3/5, MRR)
- Environment-based API key management
- MIT licensed
- Modular project structure


## 🧠 How the RAG System Works

The assistant follows a retrieval-augmented generation pipeline:

1. Document Loading
2. Text Processing
3. Text Chunking
4. Generate Embeddings
5. Store embeddings in ChromaDB
6. User question -> Query Embedding -> Similarity Search
7. Retrieve relevant chunks
8. Provide retrieved context + prompt to LLM (Groq)
9. Generate grounded response


## Knowledge Base & Chunking

Documents are stored in the `data/` directory and are split into smaller text chunks using LangChain's RecursiveCharacterTextSplitter. Each chunk is assigned metadata such as:

- chunk_id
- chunk_size
- source

Example metadata:

```python
{
    'chunk_id': 'chunk_001',
    'chunk_size': 770,
    'source': 'Part 1.docx'
}
```

Text chunking configuration is controlled via the project configuration (e.g., `CHUNK_SIZE`, `CHUNK_OVERLAP`) and typically results in chunks of ~700–800 characters.


## 🔎 Retrieval

- Embeddings: Hugging Face embeddings are used for semantic representation.
- Vector DB: ChromaDB stores the embeddings and metadata.
- Search: Similarity search retrieves the top-k most relevant chunks for a query.

Lower similarity distance indicates greater relevance. Example:

Question: What is a Safety Management System in aviation?

Rank 1: chunk_033 — Distance: 0.4037

Rank 2: chunk_032 — Distance: 0.5227

Rank 3: chunk_034 — Distance: 0.8323


## 📊 Retrieval Evaluation

The evaluation dataset is stored at `src/evaluation/test_questions.json` and contains test questions with reference answers and relevant chunk IDs. The project includes a script to compute Recall@1, Recall@3, Recall@5 and Mean Reciprocal Rank (MRR).

Evaluation summary (30 test questions):

| Metric               | Result |
|---------------------:|:------:|
| Number of Questions  | 30     |
| Recall@1             | 0.833  |
| Recall@3             | 1.000  |
| Recall@5             | 1.000  |
| MRR                  | 0.917  |

Interpretation: 83.3% Recall@1 (relevant chunk was top result for most questions), and 100% Recall@3/5 for the provided test set.


### Example evaluation

Question: What are the main objectives of Airport Rescue and Fire Fighting?

Retrieved results (example):

- Rank 1: chunk_039 | Distance: 0.6927
- Rank 2: chunk_041 | Distance: 0.7229
- Rank 3: chunk_040 | Distance: 0.8654
- Rank 4: chunk_038 | Distance: 0.8841
- Rank 5: chunk_036 | Distance: 0.9062


## 🛠️ Technology Stack

| Technology | Purpose |
|-----------|---------|
| Python    | Application development |
| LangChain | RAG pipeline and document processing |
| Hugging Face | Text embeddings |
| ChromaDB  | Vector database |
| Groq      | Large Language Model |
| Streamlit | User interface |
| python-dotenv | Environment variable management |


## 📁 Project Structure

Aviation-RAG-assistant/

├── data/
│   ├── Part 1.docx
│   ├── Part 2.docx
│   └── Part 3.docx
│
├── src/
│   ├── app.py
│   ├── config.py
│   ├── ingest.py
│   ├── rag_pipeline.py
│   │
│   └── evaluation/
│       ├── test_questions.json
│       ├── evaluate_retrieval.py
│       └── check_metadata.py
│
├── chromadb/
│
├── .env.example
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md

The exact file structure may change as the project evolves.


## Installation & Environment Variables

1. Create a virtual environment and activate it (see Quick start above).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root (you can copy `.env.example`). At minimum set:

```
GROQ_API_KEY=your_api_key_here
```

If your setup uses additional services (Hugging Face API, CHROMA settings, or others), add those variables to `.env` and `.env.example`.

Do not commit your `.env` file to version control.


## 🗄️ Build the Vector Database

Before running the application, ingest the aviation documents into ChromaDB:

```bash
python -m src.ingest
```

This loads Word documents from `data/`, processes the content, splits it into chunks, generates embeddings, and stores them in `chromadb/` along with chunk metadata and IDs.


## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run src/app.py
```

The UI will open in your browser and users can ask aviation-related questions.


## 🔍 Run Retrieval Evaluation

To evaluate retrieval performance:

```bash
python -m src.evaluation.evaluate_retrieval
```

This prints Recall@1, Recall@3, Recall@5 and MRR for the evaluation dataset.


## 🔎 Inspect Chunk Metadata

Utility to inspect metadata stored in ChromaDB:

```bash
python -m src.evaluation.check_metadata
```

Example output:

```python
{
 'chunk_size': 770,
 'chunk_id': 'chunk_001',
 'source': 'Part 1.docx'
}
```


## 🔮 Future Improvements

Potential future improvements include hybrid keyword+semantic search, query rewriting, reranking, automated answer evaluation, source citations in generated answers, conversation memory, multi-document management, cloud deployment, and monitoring of retrieval performance.


## 🛡️ Responsible Use and Limitations

This tool is intended for knowledge and educational support only. It is not an operational aviation authority and should not be used as a substitute for official regulations, NOTAMs, safety instructions, or professional judgment.

Limitations:
- Responses depend on the coverage and quality of the knowledge base.
- The language model can still generate incorrect interpretations.
- Retrieval quality depends on embedding model and chunking strategy.

Always verify safety-critical or operational information against official sources.


## 💡 Example Questions

- What are the main components of Air Traffic Management?
- What is a Safety Management System in aviation?
- What are the main objectives of airport security?
- What are the main types of air cargo?


## 📂 Repository

GitHub repository:

https://github.com/Lengerpei/Aviation-RAG-assistant


## 👨‍💻 Author

Ambrose Lengerpei

Statistician | Data Scientist | AI & Machine Learning Enthusiast

GitHub: https://github.com/Lengerpei


## 📄 License

This project is licensed under the MIT License. See the LICENSE file for full terms.


## 🙏 Acknowledgements

Developed as part of the Ready Tensor AI Developer Certification Program. Demonstrates application of RAG, semantic search, vector databases, embeddings, prompt engineering and retrieval evaluation.
