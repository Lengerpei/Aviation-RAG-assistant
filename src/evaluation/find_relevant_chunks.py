from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import (
    CHROMA_DB_DIR,
    EMBEDDING_MODEL,
)


# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

# Load existing Chroma database
vector_db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings,
)


questions = [
    "What are the main contributions of the aviation industry to Kenya's economy and society?",
    "What are the core functions of the Kenya Airports Authority?",
    "What aviation services does KAA provide at airports?",
    "How does KCAA differ from KAA in terms of their responsibilities?",
    "What types of aviation personnel and organizations does KCAA license?",
    "What are the main functions of Jomo Kenyatta International Airport?",
    "Which activities are associated with Wilson Airport?",
    "What are the main sources of aeronautical and non-aeronautical airport revenue?",
    "What factors can influence passenger demand for air travel?",
    "Which forecasting techniques can be used to estimate future airport traffic?",
    "What are the main components considered in airport planning?",
    "What information is normally included in an Airport Master Plan?",
    "How can artificial intelligence be used in aviation?",
    "What are some applications of Internet of Things technology in airports and aviation?",
    "What is an aircraft movement, and how are two movements recorded for an aircraft that lands and later departs?",
]


for question in questions:

    print("\n" + "=" * 80)
    print(f"QUESTION: {question}")
    print("=" * 80)

    results = vector_db.similarity_search_with_score(
        question,
        k=4
    )

    for rank, (document, score) in enumerate(results, start=1):

        print(f"\nRank: {rank}")
        print(f"Chunk ID: {document.metadata.get('chunk_id')}")
        print(f"Source: {document.metadata.get('source')}")
        print(f"Similarity score: {score}")

        print("\nContent:")
        print(document.page_content[:700])
        print("-" * 80)