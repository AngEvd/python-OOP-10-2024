class dictionary_iter:
    def __init__(self, dictionary: dict) -> None:
        self.dictionary = list(dictionary.items())
        self.counter = 0

    def __iter__(self) -> "dictionary_iter":
        return self

    def __next__(self) -> tuple:
        if self.counter < len(self.dictionary):
            item = self.dictionary[self.counter]
            self.counter += 1
            return item
        else:
            raise StopIteration()
