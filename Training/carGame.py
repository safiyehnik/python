command = ""
started = False
while command != "quite":
    command = input("> ").lower()
    if command == "help":
        print("""
start- to Start the car
stop- to stop the car
quite- to exit""")
    elif command == "start":
        if started:
            print("car is already started!")
        else:
            started = True
            print('car Started!')
    elif command == "stop":
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print('car stopped...')
    elif command == "quite":
        break
    else:
        print("sorry....i don't understand")