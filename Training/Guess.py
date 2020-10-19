guess_count = 0
guess_limit = 3
Secret_number = 22

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count = guess_count + 1
    if guess == Secret_number:
        print('Well done!')
        break
else:
    print('sorry you failed')