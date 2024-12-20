def convert_currency(amount_in_usd):
    usd_to_inr = 83.0
    usd_to_eur = 0.93
    usd_to_gbp = 0.74
    inr = amount_in_usd * usd_to_inr
    eur = amount_in_usd * usd_to_eur
    gbp = amount_in_usd * usd_to_gbp
    return inr, eur, gbp
usd_amount = float(input("Enter amount in USD: "))
inr, eur, gbp = convert_currency(usd_amount)
print(f"{usd_amount} USD is equal to:")
print(f"{inr:.2f} INR")
print(f"{eur:.2f} EUR")
print(f"{gbp:.2f} GBP")
