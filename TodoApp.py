# function
# def print_order(name , chai_type):
#     print(f"{name} ordered {chai_type} chai!")

# print_order("Ashutosh" , "Black")

def GST_THOKO(amount , GST):
    return amount + (amount * GST/100)

prices = [121 , 100 , 10]

for price in prices:
    cost = GST_THOKO(price , 50)
    print(f"{price} with  {cost}")







