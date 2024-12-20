def calculate_electricity_bill(units):
    if units <= 100:
        rate = 0.5  
    elif units <= 300:
        rate = 0.75  
    else:
        rate = 1.20  
    bill = units * rate
    return bill

units_consumed = int(input("Enter units"))
bill = calculate_electricity_bill(units_consumed)
print(f"Electricity bill for {units_consumed} units is ${bill:.2f}")
