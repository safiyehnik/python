class Session:
    __db_login = []

    @classmethod
    def get_session(cls):
        return cls.__db_login

    @classmethod
    def is_admin(cls):
        for session in cls.__db_login:
            if session.get("role_is") == "Admin":
                return True
        return False

    @classmethod
    def is_employee(cls):
        for session in cls.__db_login:
            if session.get("role_is") == "Employee":
                return True
        return False

    @classmethod
    def is_customer(cls):
        for session in cls.__db_login:
            if session.get("role_is") == "Customer":
                return True
        return False

