from Counter import Counter
from Discount import Discount
from ShoppingCart import ShoppingCart
from Weekday import Weekday
from Product import Product
import calendar
from datetime import *
print(calendar.day_name[date.today().weekday()])

washing_powder = Product('washing powder', 8, Discount.percentage_discount_with_threshold, percentage=30, threshold=2)
chocolate = Product('chocolate', 2)
chinese_vegetables = Product('chinese veggies', 3)
yoghurt = Product('yoghurt', 1.5, Discount.weekday_price, weekday="Wednesday", discount_price=1)
butter = Product('butter', 2.25, Discount.x_for_price_of_y, x=4,y=3)

cart = ShoppingCart({washing_powder:2, chocolate:3, chinese_vegetables:2, yoghurt:3, butter:2})
counter = Counter(cart)

print(washing_powder.is_discounted())

print(cart.products)
print('Total without discounts: €' + str(counter.total_without_discounts()))

print('Total with discounts: €' + str(counter.total_with_discounts()))
