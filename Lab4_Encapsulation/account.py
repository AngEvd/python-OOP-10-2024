class Account:
    def __init__(self, id: int, balance: int, pin: int) -> None:
        self.__id = id
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin) -> int or str:
        if self.__pin == pin:
            return self.__id
        else:
            return "Wrong pin"

    def change_pin(self, old_pin, new_pin) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        else:
            return "Wrong pin"
