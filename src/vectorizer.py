import os
import json
import argparse
from typing import List
from sentence_transformers import SentenceTransformer


"""
Simple CLI tool to create test questions for the Kibana frontend
"""

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="CLI tool for embedding creation"
    )
    parser.add_argument(
        "--question",
        required=True,
        type=str,
        help="Input question to vectorize"
    )
    return parser.parse_args()


def generate_embedding(text: str, model: SentenceTransformer) -> List[float]:
    embeddings = model.encode(
        text,
        normalize_embeddings=True
    )
    # convert numpy array → python list
    return embeddings.tolist()


def main() -> None:
    args = parse_args()
    embedding_model = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    model = SentenceTransformer(embedding_model)
    embedding_vector = generate_embedding(args.question, model)
    with open("test_questions.info", "a") as q_file:
        json.dump(embedding_vector, q_file)
        q_file.write("\n")


if __name__ == "__main__":
    main()