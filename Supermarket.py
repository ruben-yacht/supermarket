from Counter import Counter
from Discount import Discount
from ShoppingCart import ShoppingCart
from Weekday import Weekday
from Product import Product

washing_powder = Product('washing powder', 8, Discount.x_for_price_of_y, x=4,y=3)
chocolate = Product('chocolate', 2)
chinese_vegetables = Product('chinese veggies', 3)
yoghurt = Product('yoghurt', 1)
butter = Product('butter', 2.25)

cart = ShoppingCart({washing_powder:1, chocolate:3, chinese_vegetables:2, yoghurt:3, butter:2})
counter = Counter(cart)

print(washing_powder.is_discounted())

print(cart.products)
print('Total without discounts: €' + str(counter.total_without_discounts()))

print('Total with discounts: €' + str(counter.total_with_discounts()))
