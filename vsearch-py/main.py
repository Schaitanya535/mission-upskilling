from pathlib import Path
from utils.fastembed_utils import load_model
import utils.file_reader as fr

DOCS_PATH = Path(__file__).parent / "docs.txt"


def read_data() -> list[str]:
    return fr.read_lines(str(DOCS_PATH))


def generate_embeddings():
    data_points = read_data()
    model = load_model()
    embeddings = list(model.embed(data_points))
    return embeddings


def main():
    embeddings = generate_embeddings()
    print(embeddings)


if __name__ == "__main__":
    main()
