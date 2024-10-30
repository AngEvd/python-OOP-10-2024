from typing import Generator


def squares(n: int) -> Generator[int, None, None]:
    i = 1
    while i <= n:
        yield i * i
        i += 1
