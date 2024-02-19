from dataclasses import dataclass


@dataclass
class Product:
    name: str = ''
    price: float = 0.0
    discount: int = 0

    def getDiscountPrice(self) -> float:
        return self.price * (self.discount / 100)

    def getDiscountAmount(self) -> float:
        return self.price - self.getDiscountPrice()

    def getDescription(self) -> str:
        return self.name


@dataclass
class Movie(Product):
    year: int = 0

    def getYear(self) -> int:
        return self.year


@dataclass
class Book(Product):
    author: str = ''

    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} by {self.author}"
