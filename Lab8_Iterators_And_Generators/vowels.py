class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = [char for char in self.text if char.lower() in 'aeiou']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.vowels):
            raise StopIteration
        vowel = self.vowels[self.index]
        self.index += 1
        return vowel
