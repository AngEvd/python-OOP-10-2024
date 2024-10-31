class countdown_iterator:
    def __init__(self, count: int) -> None:
        self.count = count

    def __iter__(self) -> "countdown_iterator":
        return self

    def __next__(self) -> int:
        if self.count >= 0:
            num = self.count
            self.count -= 1
            return num
        else:
            raise StopIteration()
