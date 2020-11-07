import itertools
from src.enums import RoleEnum
from src.session.session import Session


class User:
    __user_db = [
        {
            "_id": "1",
            "first_name": "safiyeh",
            "last_name": "nikkhah",
            "username": "09153218364",
            "password": "safa",
            "role_is": RoleEnum.ADMIN
        }
    ]
    __id = itertools.count(2)


    # @classmethod
    # def register_admin(cls, first_name: str = None, last_name: str = None, username: str = None,
    #                    password: str = None) -> bool:
    #     if not cls.check_user(first_name, last_name):
    #         user = {
    #             "_id": next(cls.__id),
    #             "first_name": first_name,
    #             "last_name": last_name,
    #             "username": username,
    #             "password": password,
    #             "role_is": RoleEnum.ADMIN
    #         }
    #         cls.__user_db.append(user)
    #         return True
    #     return False


    @classmethod
    def register_employee(cls, first_name: str = None, last_name: str = None, username: str = None,
                          password: str = None) -> bool:
        if not cls.check_user(first_name, last_name):
            user = {
                "_id": next(cls.__id),
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "password": password,
                "role_is": RoleEnum.EMPLOYEE
            }
            cls.__user_db.append(user)
            return True
        return False

    @classmethod
    def register_customer(cls, first_name: str = None, last_name: str = None, username: str = None,
                          password: str = None) -> bool:
        if not cls.check_user(first_name, last_name):
            user = {
                "_id": next(cls.__id),
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "password": password,
                "role_is": RoleEnum.CUSTOMER
            }
            cls.__user_db.append(user)
            return True
        return False

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
    def login(cls, username: str = None, password: str = None) -> (bool, str):
        if cls.check_login(username, password):
            return False, f"user with this username: {username} & password: {password}  login in database"
        else:
            for user in cls.__user_db:
                if user.get("username") == username and user.get("password") == password:
                    for login in Session.get_session():
                        Session.get_session().remove(login)
                    if len(Session.get_session()) == 0:
                        Session.get_session().append(user)
                        return True, ""
                    return False, "more than one user login in session"
            return False, f'''
you don't have any permission
    please first register
                '''

    @classmethod
    def logout(cls, username=None, password=None) -> (bool, str):
        if not Session.get_session():
            return False, "database is empty"
        # print(Session.get_session())
        for user in Session.get_session():
            if user.get("username") == username and user.get("password") == password:
                Session.get_session().remove(user)
                return True, ""
        return False, "user not found"

    @classmethod
    def get_all_user(cls):
        return cls.__user_db

# print(User.register_employee("safiyeh", "nikkhah","09153218364","safa"))
# print(User.is_admin("09153218364","safa"))
# print(User.get_all_user())
# print(User.check_user("safiyeh","nikkhah"))
# print(User.register_admin("safiyeh", "nikkhah", "09153218364", "safa"))
# print(User.login())
# print(Session.get_session())
# print(User.register_customer("alireza", "omidvar", "alio", "09155054160"))
# print(User.check_user("alireza","omidvar"))
# User.is_employee("alireza", "omidvar", "alio", "09155054160")
# print(User.get_all_user())
# print(User.login())
# print(Session.get_session())
# print(User.logout("09153218364","safa"))
# print(User.get_session_user())
