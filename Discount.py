from datetime import *
import calendar

class Discount():
    '''can calculate various types of discounts'''
    def __init__(self):
        pass

    @staticmethod
    def percentage_discount_with_threshold(orig_price, amount, args={'percentage':0, 'threshold':1}):
        if amount >= args['threshold']:
            return orig_price + ((100-args['percentage'])/100)
        else:
            return orig_price * amount

    @staticmethod
    def x_for_price_of_y(orig_price, amount, args={'x':1, 'y':1}):
        if amount == args['x']:
            return orig_price * args['y']
        else:
            return orig_price * amount

    @staticmethod
    def weekday_price(orig_price, amount, args={'weekday':None, 'discount_price':0}):
        if calendar.day_name[date.today().weekday()] == args['weekday']:
            return args['discount_price']
        return orig_price
