from dataclasses import dataclass

@dataclass
class product:
    name: str
    price: float
    discountPercent: int

    def getDiscountAmount(self):
        return self.price * (self.discountPercent / 100)

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()