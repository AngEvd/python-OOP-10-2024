from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, id: int) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: list[DVD] = []

    # def __repr__(self) -> str:
    #     return (f"{self.id}: {self.name} of age {self.age}"
    #             f" has {len(self.rented_dvds)} rented DVD's ({', '.join(map(str, self.rented_dvds))})")

    def __repr__(self) -> str:
        return (f"{self.id}: {self.name} of age {self.age}"
                f" has {len(self.rented_dvds)} rented DVD's ({', '.join(dvd.name for dvd in self.rented_dvds)})")