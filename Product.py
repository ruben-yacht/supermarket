from Discount import Discount
class Product():
    '''meta information for a product item in a supermarket'''

    def __init__(self, name, price, discount_rule = None, **kwargs):
        self.name = name
        self.price = price
        self.discount_rule = discount_rule
        self.kwargs = kwargs
        print('kwargs:',self.kwargs)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if(price >= 0):
            self.__price = price
        else:
            self.__price = 0

    def is_discounted(self):
        if self.discount_rule != None:
            return True
        return False

    def get_discounted_total_price(self, amount=1):
        if(self.is_discounted):
            print('gonna discount with arguments',self.kwargs)
            return self.discount_rule(orig_price=self.price, args=self.kwargs)



    def __str__(self):
        return self.__name

    __repr__ = __str__
