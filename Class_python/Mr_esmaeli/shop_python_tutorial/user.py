from enums import RoleEnum
from session import Session

class User:

    __user_db = []

    @classmethod
    def register_admin(cls, first_name: str = None, last_name: str = None, username: str = None, password: str = None):
        if not cls.check_user(first_name, last_name):
            user = {
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "password": password,
                "role_is": RoleEnum.ADMIN
            }
            cls.__user_db.append(user)
            return f'''*** you register successfully ***
check your information
first_name : {first_name}
last_name  : {last_name}
username   : {username}
password   : {password}
'''
        else:
            return f"user {first_name} {last_name} with [admin] role have been registered"

    @classmethod
    def register_employee(cls, first_name: str = None, last_name: str = None, username: str = None, password: str = None):
        if not Session.is_admin():
            return False, "you don't have any permission "
        if not cls.check_user(first_name, last_name):
            user = {
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "password": password,
                "role_is": RoleEnum.EMPLOYEE
            }
            cls.__user_db.append(user)
            return f'''
*** you register successfully ***
check your information
first_name : {first_name}
last_name  : {last_name}
username   : {username}
password   : {password}
            '''
        else:
            return f"user {first_name} {last_name} with [employee] role have been registered"

    @classmethod
    def register_customer(cls, first_name: str = None, last_name: str = None, username: str = None, password: str = None):
        if not cls.check_user(first_name, last_name):
            user = {
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "password": password,
                "role_is": RoleEnum.CUSTOMER
            }
            cls.__user_db.append(user)
            return f'''
*** you register successfully ***
check your information
first_name : {first_name}
last_name  : {last_name}
username   : {username}
password   : {password}
            '''
        else:
            return f"user {first_name} {last_name} with [customer] role have been registered"

    @classmethod
    def check_user(cls, first_name=None, last_name=None):
        for user in cls.__user_db:
            if user.get("first_name") == first_name and user.get("last_name") == last_name:
                return True
        return False

    @classmethod
    def check_login(cls, username, password):
        for user in Session.get_session():
            if user.get("username") == username and user.get("password") == password:
                return True
        return False

    @classmethod
    def login(cls):
        username = input("phone_number for username: ")
        password = input("password: ")
        if username and password:
            if not cls.check_login(username, password):
                for user in cls.__user_db:
                    if user.get("username") == username and user.get("password") == password:

                        Session.get_session().append(user)
                        return"you login successfully"

                return f'''
 you don't have any permission
  please first register 
  [12] for register admin
  [10] for register customer
                '''

            else:
                return f"user with this username: {username} & password: {password}  login in database"
        return "you forgot enter username & password"

    @classmethod
    def logout(cls, username=None, password=None):
        if Session.get_session():
            for user in cls.__user_db:
                if user.get("username") == username and user.get("password") == password:
                    Session.get_session().remove(user)
                    return f"user with username: {username} & password: {password} logout"
            return "user not found"
        return "database is empty"


    @classmethod
    def get_all_user(cls):
        return cls.__user_db





#print(User.register_employee("safiyeh", "nikkhah","09153218364","safa"))
#print(User.is_admin("09153218364","safa"))
#print(User.get_all_user())
#print(User.check_user("safiyeh","nikkhah"))
#User.is_admin("safiyeh", "nikkhah", "saf", "09153218364")
#User.is_employee("alireza", "omidvar", "alio", "09155054160")
#print(User.check_user("alireza","omidvar"))
#User.is_employee("alireza", "omidvar", "alio", "09155054160")
#print(User.get_all_user())
#print(User.login())
#print(User.login())
#print(User.logout("09153218364","safa"))
#print(User.get_session_user())
