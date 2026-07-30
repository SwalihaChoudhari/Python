shop={
    "Biscuits":10,
    "Milk":32,
    "Soap":20,
    "sauce":35,
    "peanut butter":60,
    "coco powder":25,
    "dark chocolate":100
    }
cart=[]
item=input("Enter item:")
if item in shop:
    cart.append(item)
    print(f"{item} added")
else:
    print(f"{item} does not exist!")
total = 0
for item in cart:
    total = total + shop.get(item, 0) 
print("Your cart:", cart)
print("Total bill: ₹", total)

