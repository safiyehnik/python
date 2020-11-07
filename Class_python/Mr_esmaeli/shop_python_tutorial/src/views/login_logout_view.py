from src.models.user import User
from src.session.session import Session


class LoginLogout:

    @classmethod
    def login_user(cls) -> (bool, str):
        print("----------login----------")
        username = input("phone_number for username: ")
        password = input("password: ")
        if not username or not password:
            return False, "you forgot enter username or password"
        else:
            result, msg = User.login(username, password)
            if result:
                return True, "you login successfully"
            else:
                return False, msg

    @classmethod
    def logout_user(cls) -> (bool, str):
        print("--------logout---------")
        username = input("<<phone_number>> for username: ")
        password = input("password: ")
        if not username or not password:
            print("you forgot enter username or password")
        else:
            result, msg = User.logout(username, password)
            if result:
                print("user logout successfully")
            else:
                print(msg)

    @classmethod
    def show_all_session(cls):
        print(Session.get_session())