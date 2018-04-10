class Discount():
    '''can calculate various types of discounts'''
    def __init__(self):
        pass

    @staticmethod
    def percentage_discount_with_threshold(orig_price, amount, args={'percentage':0, 'threshold':1}):
        
        pass

    @staticmethod
    def x_for_price_of_y(orig_price, amount, args={'x':1, 'y':1}):
        print('received arguments',args)
        print(args['x'], 'for the price of ', args['y'])
        pass

    @staticmethod
    def weekday_price(orig_price, amount, args={'weekday':None, 'discount_price':0}):
        pass
