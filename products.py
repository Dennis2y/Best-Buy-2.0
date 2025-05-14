class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.promotion = None

    def is_active(self):
        return self.quantity > 0

    def activate(self):
        self.quantity = 1

    def deactivate(self):
        self.quantity = 0

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        promo = f" - Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo}"

    def buy(self, amount):
        if amount > self.quantity:
            raise Exception("Not enough quantity")
        if self.promotion:
            total = self.promotion.apply_promotion(self, amount)
        else:
            total = self.price * amount
        self.quantity -= amount
        return total


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def is_active(self):
        return True

    def buy(self, amount):
        if self.promotion:
            return self.promotion.apply_promotion(self, amount)
        return self.price * amount

    def show(self):
        return f"{self.name} (Non-stocked), Price: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, amount):
        if amount > self.maximum:
            raise Exception(f"Limit exceeded. Max allowed: {self.maximum}")
        return super().buy(amount)

    def show(self):
        return f"{self.name} (Limit {self.maximum}), Price: {self.price}, Quantity: {self.quantity}"
