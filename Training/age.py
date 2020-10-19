from datetime import datetime
print("please enter your birthday with format---> 'year-month-day'")
age = datetime.strptime(input(">"), "%Y-%m-%d")
day = (datetime.now() - age).days
if day <= 0:
    print("you have n't born yet")
else:
    print(f"days:{day}")
#print(f'day:{age.day} month:{age.month} years:{age.year}')
