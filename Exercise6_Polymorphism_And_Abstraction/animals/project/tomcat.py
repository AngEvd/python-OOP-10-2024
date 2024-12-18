from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int, gender: str = "Male") -> None:
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound() -> str:
        return "Hiss"

