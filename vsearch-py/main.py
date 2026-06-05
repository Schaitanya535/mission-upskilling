from pathlib import Path
from typing import Iterable

from fastembed import TextEmbedding
from fastembed.common.types import NumpyArray
import utils.file_reader as fr

import heapq as hq

DOCS_PATH = Path(__file__).parent / "docs.txt"


def generate_embeddings_data(model: TextEmbedding):
    data_points = fr.read_lines(str(DOCS_PATH))
    embeddings = model.embed(data_points)
    return list(zip(embeddings, data_points))


def generate_embedded_query(model: TextEmbedding, query: str):
    return next(iter(model.embed(query)))


def get_score(data_point: NumpyArray, query: NumpyArray):
    dot = data_point.dot(query)
    return float(dot)


def heap_search(database: list[tuple[NumpyArray, str]], query: NumpyArray, k: int):
    k = min(k, len(database))
    iter_db = iter(database)
    count = 0
    result: list[tuple[float, str]] = []
    len_db = len(database)
    while count < k:
        data_point = next(iter_db)
        score = get_score(data_point[0], query)
        result.append((score, data_point[1]))
        count += 1
    hq.heapify(result)

    for i in range(k, len_db):
        data_point = next(iter_db)
        score = get_score(data_point[0], query)
        top = result[0]
        if top[0] < score:
            hq.heappop(result)
            hq.heappush(result, (score, data_point[1]))
    return result


def search(database: Iterable[tuple[NumpyArray, str]], query: NumpyArray, k: int):
    scores = [
        (get_score(data_point[0], query), index, data_point[1])
        for index, data_point in enumerate(database)
    ]
    return sorted(scores, reverse=True)[0:k]


def main():
    # Text Embedding pulls the specified model and caches it.
    model = TextEmbedding("BAAI/bge-small-en-v1.5")
    db = generate_embeddings_data(model)
    query = """
    Harness Engineering
    """
    embedded_query = generate_embedded_query(model, query)
    # print(embedded_query)
    # scores = search(db, embedded_query, 5)
    heap_scores = heap_search(list(db), embedded_query, 5)
    heap_scores.sort(reverse=True)
    # for score in scores:
    #     print(score)
    # print("\n###########################################\n")
    for score in heap_scores:
        print(score)


if __name__ == "__main__":
    main()
