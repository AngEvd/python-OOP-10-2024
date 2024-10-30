from typing import Generator


def reverse_text(string: str) -> Generator[str, None, None]:
    for i in range(len(string) - 1, -1, -1):
        yield string[i]
