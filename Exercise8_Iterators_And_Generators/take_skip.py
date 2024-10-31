class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.start: int = 0

    def __iter__(self) -> "take_skip":
        return self

    def __next__(self) -> int:
        if self.count > 0:
            num = self.start
            self.start += self.step
            self.count -= 1
            return num
        else:
            raise StopIteration()
