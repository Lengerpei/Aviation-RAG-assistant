# ✈️ Aviation RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) assistant that answers aviation-related questions using uploaded documents instead of relying solely on a Large Language Model (LLM). The application retrieves relevant information from aviation documents and uses it to generate accurate, context-aware responses.

---

## Project Overview

The Aviation RAG Assistant helps users quickly find information from aviation documents by allowing them to ask questions in natural language.

Unlike a standard chatbot, this assistant first searches the uploaded documents for relevant information before generating a response. This reduces hallucinations and improves the reliability of answers.

---

## Features

- Upload aviation documents
- Ask questions in natural language
- Retrieves relevant document sections before answering
- Context-aware responses using Retrieval-Augmented Generation (RAG)
- Simple web interface built with Streamlit
- Modular architecture for future expansion

---

## How It Works

The assistant follows a standard RAG pipeline:

```
            Aviation Documents
                     │
                     ▼
         Document Processing
                     │
                     ▼
            Text Chunking
                     │
                     ▼
          Generate Embeddings
                     │
                     ▼
          Vector Database Storage
                     │
                     ▼
             User Question
                     │
                     ▼
      Retrieve Relevant Chunks
                     │
                     ▼
          Prompt + Retrieved Context
                     │
                     ▼
             Groq Language Model
                     │
                     ▼
             Generated Response
```

---

## Tech Stack

- Python
- LangChain
- Groq LLM
- HuggingFace Embeddings
- Chroma Vector Database
- Streamlit

---

## Project Structure

```
Aviation-RAG-assistant/
│
├── src/
│   ├── app.py
│   ├── rag_pipeline.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── utils.py
│
├── data/
│
├── requirements.txt
│
├── .env.example
│
└── README.md
```

> Folder names may vary depending on your implementation.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Lengerpei/Aviation-RAG-assistant.git

cd Aviation-RAG-assistant
```

### 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

Create a file named `.env`

```text
GROQ_API_KEY=your_api_key_here
```

Replace the value with your own Groq API key.

---

### 5. Run the application

```bash
streamlit run src/app.py
```

The application will open in your browser.

---

## Example Questions

Try asking questions such as:

- What is a Fixed Base Operator?
- Explain ICAO Annex 14.
- What are the responsibilities of Air Traffic Control?
- What documents are required for airport certification?
- Summarize the uploaded aviation report.

---

## Example Workflow

1. Upload aviation documents.
2. Wait for indexing to complete.
3. Ask a question.
4. The assistant retrieves relevant information.
5. A grounded answer is generated.

---

## Limitations

- Responses depend on the quality of uploaded documents.
- Cannot answer questions outside the document collection.
- Performance depends on the selected embedding model and language model.

---

## Future Improvements

- Source citations for every response
- Multi-document collections
- Chat history and conversation memory
- Hybrid keyword and semantic search
- Cloud deployment
- User authentication

---

## Why RAG?

Traditional language models generate responses from learned knowledge, which may not always be accurate or up to date.

Retrieval-Augmented Generation (RAG) improves reliability by retrieving relevant information from documents before generating an answer.

This makes responses:

- More accurate
- More transparent
- Better grounded in source documents
- Less prone to hallucination

---

## Repository

GitHub Repository:

https://github.com/Lengerpei/Aviation-RAG-assistant

---

## Author

**Ambrose Lengerpei**

Statistician | Data Scientist | AI & Machine Learning Enthusiast

Interests:

- Artificial Intelligence
- Retrieval-Augmented Generation (RAG)
- Aviation Analytics
- Machine Learning
- Business Intelligence

GitHub:
https://github.com/Lengerpei

---

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2026 Ambrose Lengerpei

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software.
```

---

## Acknowledgements

This project was developed as part of the **Ready Tensor AI Developer Certification Program**, demonstrating the practical application of Retrieval-Augmented Generation (RAG) for document-based question answering.
