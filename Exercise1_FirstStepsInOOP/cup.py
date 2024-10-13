class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, amount: int):
        if self.quantity + amount <= self.size:
            self.quantity += amount

    def status(self):
        return self.size - self.quantity

