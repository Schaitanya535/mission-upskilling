from pathlib import Path
from fastembed import TextEmbedding
import utils.file_reader as fr

DOCS_PATH = Path(__file__).parent / "docs.txt"


def read_data() -> list[str]:
    return fr.read_lines(str(DOCS_PATH))


def load_model():
    # Deafult model is model_name: str = "BAAI/bge-small-en-v1.5",
    return TextEmbedding()


def generate_embeddings():
    data_points = read_data()
    model = load_model()
    embeddings = list(model.embed(data_points))
    return embeddings


# Use this method to check the models and change the models.
def list_available_models():
    for m in TextEmbedding.list_supported_models():
        print(m["model"], m["dim"], m.get("size_in_GB"))


def main():
    # list_available_models()
    embeddings = generate_embeddings()
    print(embeddings)


if __name__ == "__main__":
    main()
