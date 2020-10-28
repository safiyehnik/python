from product import Product
from category import Category
from user import User

a = {
    "1": "Add Product",
    "2": "Show Product",
    "3": "Update Product",
    "4": "Delete Product",

    "5": "Add Category",
    "6": "Show Category",
    "7": "Update Category",
    "8": "Delete Category",

    "9": "Show users",
    "10": "Add Customer ",
    "11": "Add employee",
    "12": "Add admin",

    "17": "login",
    "18": "logout"

}

print("---------- Welcome ----------")
for num, title in a.items():
    print(f"{num}: {title}")

print("*****************************")
user_input = input("Enter your number:")
if user_input == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "11":
    print("you don't have any permission please first login")
    a = User.login()
    print(a)
    user_input = input("Enter your number:")
while True:
    if user_input == "1":
        name = input("name: ")
        price = input("price: ")
        category = input("category: ")
        off = input("off: ")
        res = Product().save(name, price, category, off)
        if res:
            print("yesssss")
        else:
            print(f"Please add category with {category}")
    if user_input == "2":
        print(Product.get_products_db())

    if user_input == "3":
        id = int(input("please enter Product_id for update "))
        name = input("Enter new_name for update ")
        price = input("Enter new_price for update ")
        category = input("Enter new_category for update ")
        off = input("enter new_off for update ")
        print(Product.update(id, name, price, category, off))

    if user_input == "4":
        id = input("please enter product id for delete: ")
        if Product.delete(id):
            print(f"product with {id} deleted ")
        else:
            print(f"{id} not found")

    if user_input == "5":
        name = input("please enter Category's name: ")
        if Category().save(name) is True:
            print(f"success add category:{name}")
        else:
            print(f"This category exists with {name}'s name")

    if user_input == "6":
        print(Category().get_all_category())

    if user_input == "7":
        new_name = input("new name: ")
        id = int(input("id: "))
        if Category.update(new_name, id):
            print("update successfully")
        else:
            print(f"category's {id} not found")

    if user_input == "8":
        id = int(input("please enter your id for delete Category: "))
        if Category().delete(id):
            print(f"category {id} deleted successfully")
        else:
            print(f"sorry Category {id} not found")

    if user_input == "9":
        print(User.get_all_user())

    if user_input == "10":
        print('''
    **** welcome to my online shop ****
    import your information for login as Customer
    ''')
        firstname = input("please enter your firstname: ")
        lastname = input("please enter your lastname: ")
        username = input("please enter your <<phone_number>> for username: ")
        password = input("please enter your password: ")
        print(User.is_customer(firstname, lastname, username, password))

    if user_input == "11":
        print('''
    **** welcome to my online shop ****
    import your information for login as Employee
    ''')
        firstname = input("please enter your firstname: ")
        lastname = input("please enter your lastname: ")
        username = input("please enter your <<phone_number>> for username: ")
        password = input("please enter your password: ")
        print(User.is_employee(firstname, lastname, username, password))

    if user_input == "12":
        print('''
    **** welcome to my online shop ****
    import your information for login as Admin
    ''')
        firstname = input("please enter your firstname: ")
        lastname = input("please enter your lastname: ")
        username = input("please enter your <<phone_number>> for username: ")
        password = input("please enter your password: ")
        print(User.is_admin(firstname, lastname, username, password))

    if user_input == "17":
        print(User.login())



    user_input = input("Enter your number:")
