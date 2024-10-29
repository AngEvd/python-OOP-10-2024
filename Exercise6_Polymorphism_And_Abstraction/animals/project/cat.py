from abc import ABC
from project.animal import Animal


class Cat(Animal, ABC):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound() -> str:
        return "Meow meow!"

