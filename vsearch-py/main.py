import search


def repl():
    print("Building your Index")
    print("############################")
    model, db = search.build_index()
    print("Ready to Go!!!")
    print("Search my Brain!")
    print("exit or quit to quit")
    print("\n")
    while True:
        try:
            q = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in {"exit", "quit"}:
            break
        if not q:
            continue
        scores = search.query(model, db, q, k=5, rel=0.5)
        if not scores:
            print(f"Sorry! No Relavent Results Available for your query: {q}")
        else:
            for score, _, text in scores:
                print(f"{score:.3f} {text}")
        print("\n")


def main():
    repl()


if __name__ == "__main__":
    main()
