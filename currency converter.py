while True:

    rates = {"usd" : 1.00,
         "eur" : 0.84,
         "gbp" : 0.72,
         "jpy" : 109.98,
         "aud" : 1.33,
         "cad" : 1.26,
         "chf" : 0.92,
         "cny" : 6.46,
         "hkd" : 7.76,
         "nzd" : 1.43

}

    amount = float(input("Enter an amount: "))
    first_cur = input("Enter the currency you're trying to convert (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): ").lower()
    second_cur = input("Enter the target currency (USD, EUR, GBP, JPY, AUD, CAD, CHF, CNY, HKD, NZD): ").lower()



    if first_cur not in rates:
        print("Currency unavailable")

    elif second_cur not in rates:
        print("Currency unavailable")

    else:
        final_amount = amount / rates[second_cur] * rates[first_cur]
        print(f"{amount} {first_cur} = {final_amount} {second_cur}")
        break