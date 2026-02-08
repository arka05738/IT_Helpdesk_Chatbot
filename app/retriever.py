from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "it_docs.txt"

def retrieve_context(query: str) -> str:
    if not DATA_FILE.exists():
        return ""

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        docs = f.read()

    return docs
