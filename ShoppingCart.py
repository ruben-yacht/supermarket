class ShoppingCart():
    '''collects the Products added to the shopping cart in a dictonary'''
    def __init__(self, products = {}):
        self.products = products

    def add(self, product, amount):
        self.__products[product] = amount

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        self.__products = products
