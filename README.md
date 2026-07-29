# ✈️ AviationGPT - Retrieval-Augmented Generation (RAG) Assistant

## Project Overview

AviationGPT is an AI-powered Retrieval-Augmented Generation (RAG) assistant that answers aviation-related questions using a custom knowledge base. Instead of relying only on a Large Language Model (LLM), the application retrieves relevant information from aviation documents stored in a vector database before generating an answer.

The project demonstrates how to build a complete RAG pipeline using LangChain, ChromaDB, Hugging Face Embeddings, and the Groq API.

---

## Features

* AI-powered aviation question answering
* Retrieval-Augmented Generation (RAG)
* Semantic search using vector embeddings
* ChromaDB vector database
* Hugging Face embedding model
* Groq LLM integration (Llama 3.3 70B)
* Automatic document chunking
* Word document ingestion (.docx)
* Interactive command-line interface

---

## Technologies Used

* Python 3.14
* LangChain
* LangChain-Chroma
* LangChain-Groq
* LangChain-HuggingFace
* ChromaDB
* Hugging Face Embeddings
* Sentence Transformers
* Groq API
* Python Dotenv

---

## Project Structure

```text
rt-aaidc_project aviation/
│
├── .venv/
├── .env
├── chromadb/
├── data/
│   ├── Aviation Knowledge Base Part 1.docx
│   ├── Aviation Knowledge Base Part 2.docx
│   ├── Aviation Knowledge Base Part 3.docx
│   └── Aviation Knowledge Base Part 4.docx
│
├── src/
│   ├── config.py
│   ├── ingest.py
│   ├── rag.py
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

## How the Application Works

1. Aviation documents are placed in the `data` folder.
2. `ingest.py` reads and splits the documents into manageable chunks.
3. Hugging Face generates vector embeddings for each chunk.
4. The embeddings are stored in ChromaDB.
5. When a user asks a question:

   * Relevant document chunks are retrieved from ChromaDB.
   * The retrieved context is sent to the Groq LLM.
   * The LLM generates an answer based on the retrieved information.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Lengerpei/rt-aaidc_project-aviation.git
```

Move into the project directory:

```bash
cd rt-aaidc_project-aviation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Build the Knowledge Base

Run:

```bash
python src/ingest.py
```

This will:

* Load all Word documents
* Split the documents into chunks
* Generate embeddings
* Store them in ChromaDB

---

## Run the Application

```bash
python src/app.py
```

Example:

```text
Ask:
What is ICAO?

Answer:
The International Civil Aviation Organization (ICAO) is a specialized agency of the United Nations responsible for developing international standards and recommended practices for civil aviation.
```

---

## Example Questions

* What is ICAO?
* What are the functions of Air Traffic Control?
* What is runway lighting?
* Explain aviation safety management.
* What are airport movement areas?
* What is the difference between ICAO and IATA?
* What are the responsibilities of an airport operator?

---

## Knowledge Base

The assistant was trained using custom aviation documents covering:

* Introduction to Aviation
* Airport Operations
* Air Traffic Management
* Aviation Safety
* Aviation Security
* Meteorology
* Aircraft Operations
* ICAO Standards
* IATA Overview
* Aviation Regulations

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Document preprocessing
* Text chunking
* Vector embeddings
* Semantic search
* Vector databases
* Large Language Model integration
* Prompt engineering
* AI application development

---

## Future Improvements

* Streamlit web interface
* PDF document support
* Conversation memory
* Source citations
* Hybrid search
* Multi-document collections
* Web deployment
* Upload documents through the interface

---

## Author

**Ambrose Lengerpei**

Statistics Officer | Data Analyst | AI Enthusiast

GitHub: https://github.com/Lengerpei

---

## License

This project is intended for educational purposes as part of the Ready Tensor Retrieval-Augmented Generation (RAG) Project.
