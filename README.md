# ✈️ Aviation RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) assistant designed to answer aviation-related questions using a curated aviation knowledge base.

The assistant retrieves relevant information from aviation documents before generating an answer using a Large Language Model (LLM). This approach helps provide responses that are grounded in the available knowledge base rather than relying entirely on the model's pre-trained knowledge.

This project was developed as part of the **Ready Tensor AI Developer Certification Program**.

---

## 📌 Project Overview

The Aviation RAG Assistant allows users to ask aviation-related questions in natural language and receive answers based on information contained in the aviation knowledge base.

The knowledge base covers topics including:

- Aviation fundamentals
- Airport operations
- Passenger processing
- Air cargo operations
- Airport statistics and KPIs
- ICAO and IATA
- Air Traffic Management
- Safety Management Systems
- Airport security
- Airport Rescue and Fire Fighting (ARFF)
- Environmental management
- Aviation meteorology
- Kenya's aviation industry
- Kenya Airports Authority (KAA)
- Kenya Civil Aviation Authority (KCAA)
- Major airports in Kenya
- Aviation economics
- Airport planning and development
- Emerging aviation technologies

The system uses semantic similarity search to identify relevant document chunks and provides these chunks as context to the language model.

---

## 🎯 Objectives

The main objectives of the project are to:

1. Build a practical aviation-focused RAG application.
2. Enable natural-language interaction with aviation documents.
3. Retrieve relevant information using semantic similarity search.
4. Generate answers grounded in retrieved document content.
5. Reduce the likelihood of unsupported or hallucinated responses.
6. Evaluate retrieval performance using a predefined test dataset.
7. Provide a foundation that can be extended to other aviation knowledge applications.

---

## ✨ Features

- Aviation-focused question answering
- Retrieval-Augmented Generation (RAG)
- Semantic similarity search
- Document-based responses
- HuggingFace embeddings
- ChromaDB vector database
- Groq language model
- Streamlit user interface
- Configurable text chunking
- Chunk metadata and unique chunk IDs
- Retrieval evaluation dataset
- Recall@1, Recall@3 and Recall@5 evaluation
- Mean Reciprocal Rank (MRR) evaluation
- Environment-based API key management
- MIT licensed
- Modular project structure

---

## 🧠 How the RAG System Works

The assistant follows a retrieval-augmented generation pipeline:

```text
                    AVIATION DOCUMENTS
                           │
                           ▼
                 Document Loading
                           │
                           ▼
                  Text Processing
                           │
                           ▼
                    Text Chunking
                           │
                           ▼
                 Generate Embeddings
                           │
                           ▼
                  Chroma Vector DB
                           │
                           │
                     USER QUESTION
                           │
                           ▼
                    Query Embedding
                           │
                           ▼
                Similarity Search
                           │
                           ▼
                Relevant Text Chunks
                           │
                           ▼
              Prompt + Retrieved Context
                           │
                           ▼
                     Groq LLM
                           │
                           ▼
                  Grounded Response

The system separates the process into two main stages.

Retrieval

The user's question is converted into an embedding and compared against the embeddings stored in ChromaDB.

The most relevant document chunks are retrieved based on semantic similarity.

Generation

The retrieved chunks are provided to the language model as context. The model then generates an answer based on the retrieved information.

📚 Knowledge Base

The project uses aviation documents stored in the data/ directory.

The documents are processed and divided into smaller text chunks before being converted into embeddings.

Each chunk is assigned metadata including:

chunk_id
chunk_size
source

For example:

chunk_id: chunk_001
chunk_size: 770
source: Part 1.docx

The chunk IDs make it possible to identify which sections of the knowledge base were retrieved during evaluation.

✂️ Text Chunking Strategy

The project uses LangChain's RecursiveCharacterTextSplitter.

The chunking configuration is controlled through the project configuration:

RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
)

The current knowledge base produces chunks of approximately 700–800 characters, depending on the content and document structure.

Chunk metadata is stored alongside the vector representations.

This allows the retrieval system to identify individual chunks such as:

chunk_001
chunk_002
chunk_003
...

The chunking strategy was selected to keep retrieved passages reasonably focused while retaining enough surrounding context for question answering.

🔎 Retrieval

The system uses:

HuggingFace embeddings for semantic representation
ChromaDB for vector storage
Similarity search for retrieving relevant chunks

For each query, the system retrieves the top relevant chunks and ranks them according to their similarity distance.

Example:

Question:
What is a Safety Management System in aviation?

Rank 1: chunk_033
Distance: 0.4037

Rank 2: chunk_032
Distance: 0.5227

Rank 3: chunk_034
Distance: 0.8323

Lower distance indicates greater similarity in the retrieval results.

📊 Retrieval Evaluation

To assess the performance of the retrieval component, a dedicated evaluation dataset was created in:

src/evaluation/test_questions.json

The evaluation dataset contains aviation questions together with reference answers and relevant chunk IDs.

The evaluation covers different areas of the aviation knowledge base, including:

Airport operations
Passenger processing
Air cargo
Aviation statistics
ICAO and IATA
Air Traffic Management
Safety Management Systems
Airport security
ARFF
Environmental management
Aviation meteorology
📈 Evaluation Metrics

The retrieval system was evaluated using the following metrics.

Recall@1

Measures how often the relevant chunk appears as the first retrieved result.

Recall@3

Measures how often the relevant chunk appears within the first three retrieved results.

Recall@5

Measures how often the relevant chunk appears within the first five retrieved results.

Mean Reciprocal Rank (MRR)

Measures how highly the first relevant result is ranked.

Higher values indicate better retrieval performance.

🧪 Evaluation Results

The retrieval evaluation was conducted using 30 test questions.

Metric	Result
Number of Questions	30
Recall@1	0.833
Recall@3	1.000
Recall@5	1.000
MRR	0.917
Interpretation

The system achieved:

83.3% Recall@1, meaning the relevant chunk was the top result for most questions.
100% Recall@3, meaning the relevant information was retrieved within the first three results for all 30 questions.
100% Recall@5, meaning the relevant information appeared within the first five results for all questions.
0.917 MRR, indicating that relevant information was generally ranked near the top of the retrieval results.

These results indicate that the retrieval component provides a strong foundation for the aviation question-answering system.

🧪 Example Evaluation

Example query:

What are the main objectives of Airport Rescue and Fire Fighting?

Retrieved results:

Rank 1: chunk_039 | Distance: 0.6927
Rank 2: chunk_041 | Distance: 0.7229
Rank 3: chunk_040 | Distance: 0.8654
Rank 4: chunk_038 | Distance: 0.8841
Rank 5: chunk_036 | Distance: 0.9062

The relevant ARFF information was retrieved within the top results, demonstrating the ability of the system to locate appropriate aviation content.

🛠️ Technology Stack
Technology	Purpose
Python	Application development
LangChain	RAG pipeline and document processing
HuggingFace	Text embeddings
ChromaDB	Vector database
Groq	Large Language Model
Streamlit	User interface
python-dotenv	Environment variable management
📁 Project Structure
Aviation-RAG-assistant/
│
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

🚀 Installation
1. Clone the repository
git clone https://github.com/Lengerpei/Aviation-RAG-assistant.git
cd Aviation-RAG-assistant
2. Create a virtual environment
Windows
python -m venv .venv

Activate it:

.venv\Scripts\activate
macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project root.

GROQ_API_KEY=your_api_key_here

Replace the placeholder with your own API key.

Do not commit your .env file to GitHub.

The project uses environment variables to avoid exposing API credentials in source code.

🗄️ Build the Vector Database

Before running the application, ingest the aviation documents into ChromaDB.

Run:

python -m src.ingest

The ingestion process:

Loads the Word documents.
Processes the document content.
Splits the content into chunks.
Generates embeddings.
Stores the embeddings in ChromaDB.
Assigns metadata and chunk IDs.

The vector database is stored in:

chromadb/
▶️ Run the Application

Start the Streamlit application:

streamlit run src/app.py

The application will open in your browser.

Users can then ask aviation-related questions through the interface.

🔍 Run Retrieval Evaluation

The project includes a retrieval evaluation script.

Run:

python -m src.evaluation.evaluate_retrieval

The script evaluates the predefined questions and reports:

Recall@1
Recall@3
Recall@5
MRR
🔎 Inspect Chunk Metadata

The project also includes a utility for checking the metadata stored in ChromaDB.

Run:

python -m src.evaluation.check_metadata

This can be used to verify:

Chunk IDs
Chunk sizes
Source documents

Example:

{'chunk_size': 770,
 'chunk_id': 'chunk_001',
 'source': 'Part 1.docx'}
🧪 Evaluation Dataset

The evaluation questions are stored in:

src/evaluation/test_questions.json

Each test case contains information such as:

{
    "id": "Q001",
    "question": "What is aviation and why is it important?",
    "reference_answer": "Aviation involves the operation of aircraft...",
    "relevant_chunk_ids": [
        "chunk_001"
    ]
}

This structure makes the evaluation dataset reproducible and allows the retrieval system to be tested against known relevant chunks.

🛡️ Responsible Use and Limitations

The Aviation RAG Assistant is designed as a knowledge and educational support tool.

It should not be treated as an operational aviation authority or as a replacement for official aviation regulations, procedures, NOTAMs, safety instructions, or professional judgment.

The system has several limitations:

Responses depend on the quality and coverage of the knowledge base.
The system may not answer questions outside the available documents accurately.
Retrieval quality depends on the embedding model and chunking strategy.
Similarity search may occasionally retrieve partially relevant information.
The language model can still generate incorrect interpretations.
Aviation information can change over time and should be verified against current official sources where necessary.

Users should verify safety-critical or operational information using appropriate official aviation sources.

🔧 Maintenance and Updating

The knowledge base can be updated by adding or replacing documents in the data/ directory.

After updating the documents, rebuild the vector database:

python -m src.ingest

The retrieval evaluation can then be rerun:

python -m src.evaluation.evaluate_retrieval

This provides a simple way to check whether changes to the knowledge base or retrieval configuration affect system performance.

🔮 Future Improvements

Potential future improvements include:

Hybrid keyword and semantic search
Query rewriting
Reranking of retrieved documents
Improved retrieval evaluation
Automated answer evaluation
Source citations in generated answers
Conversation memory
Multi-document management
Better handling of ambiguous questions
Cloud deployment
User authentication
Improved content filtering
Monitoring and logging of retrieval performance
💡 Why RAG?

Traditional LLM applications generate responses primarily from information learned during model training.

A RAG system first retrieves relevant information from a specific knowledge base and then provides that information to the language model as context.

This provides several advantages:

Better grounding in the available documents
Reduced reliance on model memory
Improved transparency
Easier knowledge-base updates
Better control over the information used to answer questions

For an aviation-focused application, this approach is useful because the assistant can be constrained to a defined aviation knowledge base.

📌 Example Questions

Users can ask questions such as:

What are the main components of Air Traffic Management?

What is a Safety Management System in aviation?

What are the main objectives of airport security?

What are the main types of air cargo?

What is the difference between ICAO and IATA?

What are the main stages of a passenger journey?

What are the main objectives of Airport Rescue and Fire Fighting?

What factors can affect aviation operations and safety?
📂 Repository

GitHub repository:

https://github.com/Lengerpei/Aviation-RAG-assistant

👨‍💻 Author

Ambrose Lengerpei

Statistician | Data Scientist | AI & Machine Learning Enthusiast

Areas of interest:

Artificial Intelligence
Retrieval-Augmented Generation
Aviation Analytics
Machine Learning
Data Science
Business Intelligence

GitHub:

https://github.com/Lengerpei

📄 License

This project is licensed under the MIT License.

See the LICENSE file for the complete license terms.

🙏 Acknowledgements

This project was developed as part of the Ready Tensor AI Developer Certification Program.

The project demonstrates the practical application of:

Retrieval-Augmented Generation
Semantic search
Vector databases
Embeddings
Prompt engineering
Retrieval evaluation
Aviation-focused knowledge retrieval
