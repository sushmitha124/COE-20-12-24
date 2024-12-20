def calculate_price(cart_items):
    if not cart_items:
        return "empty"
    total = 0
    for cart in cart_items.values():
        if(cart>25000):
            total+=cart
            if 20000>total<50000:
                total*=(1-0.1)
                return total
            elif total>50000:
                total*=(1-0.15)
                return total
cart_items=eval(input("Enter keys and items"))
print(calculate_price(cart_items))