# Написати програму — конвертер валют. Реалізувати спілкування з користувачем через меню.

# Value of currencies
USD = 37
EUR = 38

# Conversion option
print("1. UAH to USD \n2. UAH to EUR \n3. USD to UAH \n4. EUR to UAH")

# Ask conversion option
convert_to = input("Select conversion option: ")

# Сhecking for conversion option and converting
if convert_to == "1" : 
    amount = float(input("Enter amount UAH: "))
    print(f"{amount} UAH in USD = {round(amount / USD, 2)} USD")
elif convert_to == "2" : 
    amount = float(input("Enter amount UAH: "))
    print(f"{amount} UAH in EUR = {round(amount / EUR, 2)} EUR")
elif convert_to == "3" : 
    amount = float(input("Enter amount USD: "))
    print(f"{amount} USD in UAH = {round(amount * USD, 2)} UAH")
elif convert_to == "4" : 
    amount = float(input("Enter amount USD: "))
    print(f"{amount} EUR in UAH = {round(amount * EUR, 2)} EUR")
else : print("You didn't select an option ")