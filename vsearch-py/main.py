from pathlib import Path
import utils.file_reader as fr


def main():
    DOCS = Path(__file__).parent / "docs.txt"
    lines = fr.read_lines(str(DOCS))
    for line in lines:
        print(line)
    print(len(lines))


if __name__ == "__main__":
    main()
