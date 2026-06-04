def parse_ranges(range_string: str) -> tuple[int, int]:
    start, end = range_string.split("-")
    return int(start), int(end)


def parse_to_grid(line: str, seperator: str | None = None):
    return [val for val in line.split(seperator) if val]


def read_lines(filepath: str) -> list[str]:
    """Read file and return list of lines (stripped)."""
    with open(filepath) as f:
        return [line.strip() for line in f]


def read_raw(filepath: str) -> str:
    """Read entire file as single string."""
    with open(filepath) as f:
        return f.read().strip()


def read_ints(filepath: str) -> list[int]:
    """Read file where each line is an integer."""
    return [int(line) for line in read_lines(filepath)]


def read_grid(filepath: str) -> list[list[str]]:
    """Read file as 2D character grid."""
    return [list(line) for line in read_lines(filepath)]


def read_comma_separated_input(filepath: str):
    """Read file and take the comma separated input and give the list of strings"""
    with open(filepath) as f:
        return [item.strip() for line in f for item in line.split(",") if item.strip()]


def read_range_input(
    filepath: str, comma_separated: bool = False
) -> list[tuple[int, int]]:
    """Read file and take the input as range with a delimiter."""
    range_strings = (
        read_comma_separated_input(filepath)
        if comma_separated
        else read_lines(filepath)
    )
    return [parse_ranges(range_string) for range_string in range_strings]


def read_blocks(filepath: str) -> list[str]:
    """
    Read the nth block from a file where blocks are separated by 2+ blank lines.

    Args:
        filepath: Path to the file to read
        block_number: Zero-indexed block number to retrieve

    Returns:
        The content of the nth block as a string

    Raises:
        IndexError: If block_number is out of range
    """
    with open(filepath) as f:
        content = f.read()

    # Split by two or more consecutive newlines
    return [block.strip() for block in content.split("\n\n") if block.strip()]


def read_columns(filepath: str, separator: str | None = None) -> list[list[str]]:
    """
    Read file in columns rather than rows.

    Args:
        filepath: Path to the file to read
        separator: Optional separator (default: any whitespace)

    Returns:
        List of columns, where each column is a list of values

    Example:
        For a file with:
        1 2 3
        4 5 6
        7 8 9

        Returns: [['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
    """
    lines = read_lines(filepath)
    if not lines:
        return []

    # Split each line by separator
    rows = [[val for val in line.split(separator) if val] for line in lines]

    # Transpose rows to columns
    num_cols = len(rows[0])
    return [[row[i] for row in rows] for i in range(num_cols)]


def read_int_columns(filepath: str, separator: str | None = None) -> list[list[int]]:
    """
    Read file in columns and convert to integers.

    Args:
        filepath: Path to the file to read
        separator: Optional separator (default: any whitespace)

    Returns:
        List of columns, where each column is a list of integers
    """
    columns = read_columns(filepath, separator)
    return [[int(val) for val in col if val] for col in columns]
