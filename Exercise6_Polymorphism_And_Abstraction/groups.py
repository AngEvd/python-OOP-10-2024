class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        return f"{self.name} {self.surname}"

    def __add__(self, other: "Person") -> "Person":
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: list["Person"]) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        return len(self.people)

    def __add__(self, other: "Group") -> "Group":
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self) -> str:
        return f"Group {self.name} with members {', '.join(map(str, self.people))}"

    def __getitem__(self, index: int) -> str:
        return f"Person {index}: {str(self.people[index])}"
