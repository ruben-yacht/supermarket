class Counter():
    def __init__(self, cart):
        self.cart = cart

    def total_without_discounts(self):
        total = 0
        for product, value in self.cart.products.items():
            print(value,'x',product, '€', value * product.price)
            total += value * product.price
        return total

    def total_with_discounts(self):
        total = 0
        for product, value in self.cart.products.items():
            if product.is_discounted():
                subtotal = product.price * value
                product.get_discounted_total_price(value)
                pass
            else:
                total += value * product.price

            total += value * product.price
        return total

        pass
