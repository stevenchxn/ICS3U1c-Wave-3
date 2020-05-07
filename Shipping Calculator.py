order = int(input("How many items would you like to purchase?: "))
price = 0
if order >= 2:
    price += 10.95 + (2.95 * (order-1))
else:
    price += 10.95

print ("Your shipping price is $", round(price, 2))