from typing import Generator


def genrange(start: int, end: int) -> Generator[int, None, None]:
    i = start
    while i <= end:
        yield i
        i += 1
