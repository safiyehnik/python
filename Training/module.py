def my_list():
    print('''please input your number
for "end" enter "exit"''')
    myList = list()
    while True:
        new_list_item = input()
        if new_list_item == "exit":
            print(myList)
            break
        myList.append(new_list_item)


x = my_list()




