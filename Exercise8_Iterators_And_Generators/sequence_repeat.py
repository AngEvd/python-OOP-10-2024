class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.idx = 0

    def __iter__(self) -> "sequence_repeat":
        return self

    def __next__(self) -> str:
        if self.number > 0:
            char = self.sequence[self.idx]
            self.idx = (self.idx + 1) % len(self.sequence)
            self.number -= 1
            return char
        else:
            raise StopIteration()

