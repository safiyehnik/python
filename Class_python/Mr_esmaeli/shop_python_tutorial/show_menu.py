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

print(''''
*****************************
*   Welcome to Online shop  *
*****************************
you could select 
number [17] for login
number [10] for register customer
number [12] for register admin
 ''')
user_input = input("Enter your number:")
if user_input == "17":
    print('''
--> Welcome to login <---"
import [username] & [password]
        ''')
    print(User.login())
    user_input = input("Enter your number")
elif user_input == "12":
    print('''
**** Welcome to Register Admin ****"
import your information for login as ADMIN
            ''')
    firstname = input("please enter your firstname: ")
    lastname = input("please enter your lastname: ")
    username = input("please enter your <<phone_number>> for username: ")
    password = input("please enter your password: ")
    print(User.register_admin(firstname, lastname, username, password))
    user_input = input("Enter your number:")
elif user_input == "10":
        print('''
**** welcome to Register Customer ****
import your information for login as Customer
    ''')
        firstname = input("please enter your firstname: ")
        lastname = input("please enter your lastname: ")
        username = input("please enter your <<phone_number>> for username: ")
        password = input("please enter your password: ")
        print(User.register_customer(firstname, lastname, username, password))
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
        print(User.register_customer(firstname, lastname, username, password))

    if user_input == "11":
        print('''
    **** welcome to my online shop ****
    import your information for login as Employee
    ''')
        firstname = input("please enter your firstname: ")
        lastname = input("please enter your lastname: ")
        username = input("please enter your <<phone_number>> for username: ")
        password = input("please enter your password: ")
        print(User.register_employee(firstname, lastname, username, password))

    if user_input == "12":
        print('''
    **** welcome to my online shop ****
    import your information for login as Admin
    ''')
        firstname = input("please enter your firstname: ")
        lastname = input("please enter your lastname: ")
        username = input("please enter your <<phone_number>> for username: ")
        password = input("please enter your password: ")
        print(User.register_admin(firstname, lastname, username, password))

    if user_input == "17":
        print(User.login())

    if user_input == "18":
        username = input("please enter your <<phone_number>> for username: ")
        password = input("please enter your password: ")
        print(User.logout(username, password))



    user_input = input("Enter your number:")
