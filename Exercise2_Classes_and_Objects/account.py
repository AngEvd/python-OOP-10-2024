class Account:
    def __init__(self, id: int, name: str, balance: int = 0) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount) -> int or str:
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Amount exceeded balance"

    def info(self) -> str:
        return f"User {self.name} with account {self.id} has {self.balance} balance"
