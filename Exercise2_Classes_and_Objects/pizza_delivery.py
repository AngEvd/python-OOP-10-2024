class PizzaDelivery:
    ordered = False

    def __init__(self, name: str, price: float, ingredients: dict) -> None:
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float) -> None or str:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float) -> str or None:
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            if quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= price_per_quantity * quantity
        else:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"

    def make_order(self):
        self.ordered = True
        return (f"You've ordered pizza {self.name} "
                f"prepared with {', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])} "
                f"and the price will be {self.price}lv.")
