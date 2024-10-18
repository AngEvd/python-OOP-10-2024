from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: list[Food, Drink] = []

    def add(self, product: Product) -> None:
        if product not in self.products:
            self.products.append(product)

    def find(self, product_name: str) -> Food or Drink:
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name) -> None:
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join(f"{product.name}: {product.quantity}" for product in self.products)
