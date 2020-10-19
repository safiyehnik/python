phone = input("Phone: ")
phoneNumber = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine"
}
new_phoneNumber = ""
for ch in phone:
    new_phoneNumber += phoneNumber.get(ch, "!") + " "
print(new_phoneNumber)

