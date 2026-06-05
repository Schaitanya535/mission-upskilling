import numpy as np
from fastembed import TextEmbedding


def load_model():
    # Deafult model is model_name: str = "BAAI/bge-small-en-v1.5",
    return TextEmbedding()


def check_normalised():
    v = TextEmbedding().embed((["hello world world world world hello hello "]))
    print("Normalization Score", np.linalg.norm(list(v)))


# Use this method to check the models and change the models.
def list_available_models():
    print("Available models\n")
    print("###################################################")
    for m in TextEmbedding.list_supported_models():
        print(m["model"], m["dim"], m.get("size_in_GB"))
    print("###################################################\n")


def main():
    list_available_models()
    check_normalised()


if __name__ == "__main__":
    main()
