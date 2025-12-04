# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# varibles items
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

# variables categories
category1 = categories[0:11]
category2 = categories[13:]

#price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

#message variable
message1 = "We have" + " " + candy1 + " " + "for" + " " + bubblegum_price + " " + "in the" + " " + category1
message2 = "We have" + " " + candy2 + " " + "for" + " " + chocolate_price + " " + "in the" + " " + category1
message3 = "We have" + " " + dry_goods + " " + "for" + " " + pasta_price + " " + "in the" + " " + category2

print(message1)
print(message2)
print(message3)