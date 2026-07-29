from pathlib import Path

from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import (
    DATA_DIR,
    CHROMA_DB_DIR,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def load_documents():
    """Load all Word documents from the data folder."""

    data_path = Path(DATA_DIR)

    files = list(data_path.glob("*.docx"))

    if not files:
        raise FileNotFoundError(
            f"No Word documents (.docx) found in {DATA_DIR}"
        )

    documents = []

    print(f"\nFound {len(files)} Word documents:\n")

    for file in files:
        print(f"Loading: {file.name}")

        loader = UnstructuredWordDocumentLoader(str(file))
        docs = loader.load()

        documents.extend(docs)

    print(f"\nLoaded {len(documents)} document(s).\n")

    return documents


def split_documents(documents):
    """Split documents into smaller chunks."""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks.\n")

    return chunks


def create_vector_database(chunks):
    """Generate embeddings and store them in ChromaDB."""

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR,
    )

    print("Vector database created successfully.")
    print(f"Saved to: {CHROMA_DB_DIR}")

    return vector_db


def main():

    print("=" * 60)
    print("AVIATION KNOWLEDGE BASE INGESTION")
    print("=" * 60)

    documents = load_documents()

    chunks = split_documents(documents)

    create_vector_database(chunks)

    print("\nDone!")
    print("Your Aviation Knowledge Base is ready.")


if __name__ == "__main__":
    main()