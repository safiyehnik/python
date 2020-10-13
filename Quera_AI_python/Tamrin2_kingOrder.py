word = input().split()
list1 = list()
list1.append(word[0])
list1.append((word[1]))
if list1 == ["food", "water"]:
    print(0.5)
elif list1 == ["food", "dinner"]:
    print(1.0)
elif list1 == ["promote", "judge"]:
    print(50.0)
elif list1 == ["promote", "minister"]:
    print(80.0)
elif list1 == ["promote", "governor"]:
    print(100.0)
elif list1 == ["travel", "ground"]:
    print(45.0)
elif list1 == ["travel", "sea"]:
    print(58.0)
else:
    print(10.0)