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

# Load Chroma database
vector_db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings,
)


# Generate chunk IDs from chunk_001 to chunk_015
chunk_ids = [
    f"chunk_{i:03d}"
    for i in range(31, 46)
]


# Retrieve the chunks
data = vector_db.get(
    ids=chunk_ids,
    include=["documents", "metadatas"]
)


print("\n" + "=" * 80)
print("CHUNKS 001 - 015")
print("=" * 80)


for chunk_id, document, metadata in zip(
    data["ids"],
    data["documents"],
    data["metadatas"]
):

    print("\n" + "=" * 80)
    print(f"CHUNK ID: {chunk_id}")
    print("=" * 80)

    print(f"Source: {metadata.get('source')}")

    print("\nCONTENT:")
    print(document)

    print("\n")