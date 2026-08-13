import json
from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import CHROMA_DB_DIR, EMBEDDING_MODEL


# --------------------------------------------------
# Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

QUESTIONS_FILE = (
    PROJECT_ROOT
    / "src"
    / "evaluation"
    / "test_questions.json"
)


# --------------------------------------------------
# Load evaluation questions
# --------------------------------------------------

with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
    questions = json.load(file)


# --------------------------------------------------
# Load embedding model
# --------------------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)


# --------------------------------------------------
# Load Chroma database
# --------------------------------------------------

vector_db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings,
)


# --------------------------------------------------
# Evaluation
# --------------------------------------------------

K_VALUES = [1, 3, 5]

results = []


for item in questions:

    question_id = item["id"]
    question = item["question"]

    relevant_chunks = set(
        item["relevant_chunk_ids"]
    )

    print("\n" + "=" * 80)
    print(f"{question_id}: {question}")
    print("=" * 80)

    # Retrieve top 5 chunks
    retrieved = vector_db.similarity_search_with_score(
        question,
        k=5
    )

    retrieved_ids = []

    for rank, (document, score) in enumerate(
        retrieved,
        start=1
    ):

        chunk_id = document.metadata.get("chunk_id")

        retrieved_ids.append(chunk_id)

        print(
            f"Rank {rank}: "
            f"{chunk_id} | "
            f"Score: {score:.4f}"
        )

    # --------------------------------------------------
    # Recall@K
    # --------------------------------------------------

    metrics = {}

    for k in K_VALUES:

        top_k = set(retrieved_ids[:k])

        hit = bool(
            top_k.intersection(relevant_chunks)
        )

        metrics[f"recall@{k}"] = int(hit)

    # --------------------------------------------------
    # Reciprocal Rank
    # --------------------------------------------------

    reciprocal_rank = 0

    for rank, chunk_id in enumerate(
        retrieved_ids,
        start=1
    ):

        if chunk_id in relevant_chunks:

            reciprocal_rank = 1 / rank
            break

    metrics["reciprocal_rank"] = reciprocal_rank

    results.append(
        {
            "id": question_id,
            "question": question,
            "relevant_chunks": list(
                relevant_chunks
            ),
            "retrieved_chunks": retrieved_ids,
            **metrics
        }
    )


# --------------------------------------------------
# Overall metrics
# --------------------------------------------------

total = len(results)

recall_at_1 = sum(
    r["recall@1"] for r in results
) / total

recall_at_3 = sum(
    r["recall@3"] for r in results
) / total

recall_at_5 = sum(
    r["recall@5"] for r in results
) / total

mrr = sum(
    r["reciprocal_rank"] for r in results
) / total


# --------------------------------------------------
# Display results
# --------------------------------------------------

print("\n")
print("=" * 80)
print("RETRIEVAL EVALUATION RESULTS")
print("=" * 80)

print(f"Number of questions: {total}")

print(f"Recall@1: {recall_at_1:.3f}")
print(f"Recall@3: {recall_at_3:.3f}")
print(f"Recall@5: {recall_at_5:.3f}")
print(f"MRR:      {mrr:.3f}")

print("=" * 80)
# --------------------------------------------------
# Save evaluation results
# --------------------------------------------------

results_file = (
    PROJECT_ROOT
    / "src"
    / "evaluation"
    / "evaluation_results.json"
)

evaluation_summary = {
    "number_of_questions": total,
    "recall_at_1": recall_at_1,
    "recall_at_3": recall_at_3,
    "recall_at_5": recall_at_5,
    "mrr": mrr,
    "question_results": results
}

with open(
    results_file,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        evaluation_summary,
        file,
        indent=4
    )

print(
    f"\nDetailed results saved to: "
    f"{results_file}"
)