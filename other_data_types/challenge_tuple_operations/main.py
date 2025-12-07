# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#Count
apple_count = shelf.count("apples")

#find
banana_index = shelf.index("bananas")

#check (If Statement)
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

#count
if shelf.count("grapes") == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

#check 'Oranges'
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")

print("Number of apples:", apple_count)
print("First Banana Index:", banana_index)

