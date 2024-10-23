from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: list[Customer] = []
        self.dvds: list[DVD] = []

    @classmethod
    def dvd_capacity(cls) -> int:
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls) -> int:
        return cls.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                for customer in self.customers:
                    if customer.id == customer_id:
                        if dvd in customer.rented_dvds:
                            return f"{customer.name} has already rented {dvd.name}"
                        if dvd.is_rented:
                            return "DVD is already rented"
                        if dvd.age_restriction > customer.age:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        customer.rented_dvds.append(dvd)
                        dvd.is_rented = True
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in self.dvds:
                    if dvd.id == dvd_id:
                        if dvd in customer.rented_dvds:
                            customer.rented_dvds.remove(dvd)
                            dvd.is_rented = False
                            return f"{customer.name} has successfully returned {dvd.name}"
                        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        return "\n".join([*[str(customer) for customer in self.customers], *[str(dvd) for dvd in self.dvds],])


