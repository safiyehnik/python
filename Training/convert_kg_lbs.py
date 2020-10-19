weight = int(input('Weight: '))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    pound = (weight * 0.45)
    print(f'your weight is {pound} kilos')
elif unit.upper() == "K":
    kilo = (weight/0.45)
    print(f"your weight is {kilo} pounds")

