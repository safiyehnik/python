from src.decorators.user_decorators import check_permissions
from src.models.category import Category


class CategoryView:

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def add_category(cls):
        print("------ add category -----")
        name = input("please enter category's name: ")
        if not name:
            print("you forget enter name!")
        elif Category.save(name):
            print(f"category {name} add successfully")
        else:
            print(f"category {name} exists!")

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def del_category(cls):
        print("------ delete category -----")
        _id = input("please enter your id for delete Category: ")
        if not _id:
            print("you forget enter id!")
        elif Category.delete(_id):
            print(f"category {_id} delete successfully")
        else:
            print(f"sorry,category {_id} not found!")

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def update_category(cls):
        print("-----update category-----")
        _id = input("category's id: ")
        new_name = input("new category's name: ")
        if not _id or not new_name:
            print("you forget enter id or new name")
        else:
            result, msg = Category.update(new_name, _id)
            if result:
                print(msg)
            else:
                print(msg)

    @classmethod
    def show_all_category(cls):
        print(Category.get_all_category())
