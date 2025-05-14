class Store:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        return sum([p.quantity for p in self.products if p.is_active()])

    def get_all_products(self):
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list):
        total_cost = 0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise Exception(f"Product {product.name} is not active.")
            total_cost += product.buy(quantity)
        return total_cost
