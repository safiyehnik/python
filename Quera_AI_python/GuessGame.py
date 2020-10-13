Counter = 1
true_number = 22
while Counter <= 3:
    guess = int(input(f"Guess{Counter}: "))
    Counter += 1
    if guess == true_number:
        print('''
******************
* Great you won! *
******************''')
        break
    else:
        print("wrong number")
else:
    print("Loser ;(!")










