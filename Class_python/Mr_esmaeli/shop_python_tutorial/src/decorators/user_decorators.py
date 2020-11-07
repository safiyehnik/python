from src.enums import RoleEnum
from src.session.session import Session


def check_permissions(admin_access: bool = False, employee_access: bool = False, customer_access: bool = False):
    def decorator(function):
        def wrapper(*args, **kwargs):
            if (admin_access and Session.is_admin()) or (employee_access and Session.is_employee()) or (customer_access and Session.is_customer()):
                function(*args, **kwargs)
            else:
                message = "This option is available only for "
                user = list()
                if admin_access:
                    user.append(f"{RoleEnum.ADMIN}")
                if employee_access:
                    user.append(f"{RoleEnum.EMPLOYEE}")
                if customer_access:
                    user.append(f"{RoleEnum.CUSTOMER}")

                message += " and ".join(user)
                print(message)
        return wrapper
    return decorator
