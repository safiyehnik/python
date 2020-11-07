from src.views.category_view import CategoryView
from src.views.login_logout_view import LoginLogout
from src.views.product_view import ProductView
from src.views.register_view import RegisterView


class MenuView:
    menu = {
        "1": "Add Product",
        "2": "Show Product",
        "3": "Update Product",
        "4": "Delete Product",

        "5": "Add Category",
        "6": "Show Category",
        "7": "Update Category",
        "8": "Delete Category",

        "9": "Show users",
        "10": "Register Customer ",
        "11": "Register employee",
        "12": "Show Session",

        "17": "login",
        "18": "logout",
        "19": "Show Menu",
        "0": "exit"
    }

    @classmethod
    def print_task(cls):
        for index, name in cls.menu.items():
            print(f' {index} : {name} ')
        print("--------------------------")

    @classmethod
    def show(cls):

        print('''
*****************************
*   Welcome to Online shop  *
*****************************
             ''')
        while True:
            result, msg = LoginLogout.login_user()
            if result:
                print(msg)
                break
            else:
                print(msg)
                continue
        print("------------------welcome--------------------")
        MenuView.print_task()
        print("--------------------------")
        user_input = input("Enter your number: ")
        while True:
            if user_input == "1":  # add product
                ProductView.add_product()

            if user_input == "2":  # show product
                ProductView.show_all_products()

            if user_input == "3":  # update product
                ProductView.update_product()

            if user_input == "4":  # delete product
                ProductView.delete_product()

            if user_input == "5":  # add Category
                CategoryView.add_category()

            if user_input == "6":  # show category
                CategoryView.show_all_category()

            if user_input == "7":  # update category
                CategoryView.update_category()

            if user_input == "8":  # delete category
                CategoryView.del_category()

            if user_input == "9":
                RegisterView.show_all_users()

            if user_input == "10":
                RegisterView.add_customer()

            if user_input == "11":
                RegisterView.add_employee()

            if user_input == "12":
                LoginLogout.show_all_session()

            if user_input == "17":  # login
                print(LoginLogout.login_user())

            if user_input == "18":  # logout
                LoginLogout.logout_user()

            if user_input == "19":
                MenuView.print_task()

            if user_input == "0":
                break

            user_input = input("Enter your number:")
        print("Thank you ,bye")


