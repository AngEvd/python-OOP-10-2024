from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @property
    def gain_weight(self) -> float:
        return 0.10

    @staticmethod
    def make_sound() -> str:
        return "Squeak"


class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 0.40

    @staticmethod
    def make_sound() -> str:
        return "Woof!"


class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return [Vegetable, Meat]

    @property
    def gain_weight(self) -> float:
        return 0.30

    @staticmethod
    def make_sound() -> str:
        return "Meow"


class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 1.00

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"
