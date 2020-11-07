from src.enums import RoleEnum
from src.models.user import User
from src.decorators.user_decorators import check_permissions


class RegisterView:

#     @classmethod
#     @check_permissions(admin_access=True)
#     def add_admin(cls):
#         print('''
# **** Register Admin ****"
# import your information
#                 ''')
#         firstname = input("please enter your firstname: ")
#         lastname = input("please enter your lastname: ")
#         username = input("<<phone_number>> for username: ")
#         password = input("please enter your password: ")
#         if not firstname or not lastname or not username or not password:
#             print("you forgot enter something")
#         elif User.register_admin(firstname, lastname, username, password):
#             print(f'''
# *** you register successfully ***
# check your information
# first_name : {firstname}
# last_name  : {lastname}
# username   : {username}
# password   : {password}
# ''')
#         else:
#             print(f"user {firstname} {lastname} with {RoleEnum.ADMIN} role have been registered")

    @classmethod
    @check_permissions(admin_access=True)
    def add_employee(cls):
        print("------- Register Employee ------")
        firstname = input("please enter your firstname: ")
        lastname = input("please enter your lastname: ")
        username = input("<<phone_number>> for username: ")
        password = input("please enter your password: ")
        if not firstname or not lastname or not username or not password:
            print("you forgot enter something")
        elif User.register_employee(firstname, lastname, username, password):
            print(f'''
*** you register successfully ***
check your information
first_name : {firstname}
last_name  : {lastname}
username   : {username}
password   : {password}
''')
        else:
            print(f"user {firstname} {lastname} with {RoleEnum.EMPLOYEE} role have been registered")

    @classmethod
    @check_permissions(admin_access=True, employee_access=False, customer_access=True)
    def add_customer(cls) -> (bool, str):
        print("------- Register Customer ------")
        firstname = input("please enter your firstname: ")
        lastname = input("please enter your lastname: ")
        username = input("<<phone_number>> for username: ")
        password = input("please enter your password: ")
        if not firstname or not lastname or not username or not password:
            print("you forgot enter something")
        elif User.register_customer(firstname, lastname, username, password):
            print(f'''
*** you register successfully ***
check your information
first_name : {firstname}
last_name  : {lastname}
username   : {username}
password   : {password}
''')
        else:
            return False, f"user {firstname} {lastname} with {RoleEnum.CUSTOMER} role have been registered"

    @classmethod
    def show_all_users(cls):
        print(User.get_all_user())


# RegisterView.add_admin()
# RegisterView.add_employee()
# RegisterView.add_customer()
# print(RegisterView.show_all_users())
# LoginLogout.login_user()
# LoginLogout.login_user()
# LoginLogout.logout_user()