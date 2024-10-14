class Circle:
    pi = 3.14

    def __init__(self, radius: int) -> None:
        self.radius = radius

    def set_radius(self, new_radius: int) -> None:
        self.radius = new_radius

    def get_area(self) -> float:
        return Circle.pi * pow(self.radius, 2)

    def get_circumference(self) -> float:
        return 2 * Circle.pi * self.radius


