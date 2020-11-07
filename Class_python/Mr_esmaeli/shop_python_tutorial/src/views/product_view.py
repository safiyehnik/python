from src.decorators.user_decorators import check_permissions
from src.models.product import Product


class ProductView:
    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def add_product(cls):
        print("-------- add product --------")
        name = input("product_name: ")
        price = input("price: ")
        category = input("category: ")
        off = input("off: ")
        if not name or not price or not category or not off:
            print("you forget enter something")
        elif Product().save(name, price, category, off):
            print(f"product {name} add successfully")
        else:
            print(f"category {category} not exist " \
                  f"please first add category {category}")

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def delete_product(cls):
        print("-------- delete product --------")
        _id = input("please enter product_id for delete: ")
        if not _id:
            print("you forget enter id")
        elif Product.delete(_id):
            print(f"product with id {_id} deleted successfully ")
        else:
            print(f"product with id {_id} not found")

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def update_product(cls):
        print("-------- update product --------")
        _id = input("please enter Product_id for update: ")
        if not _id:
            print("without product_id you couldn't update!")
        else:
            name = input("Enter new_name for update: ")
            price = input("Enter new_price for update: ")
            off = input("enter new_off for update: ")
            category = input("Enter new_category for update: ")
            result, msg = Product.update(_id, name, price, category, off)
            if result:
                print(f"product with id {_id} update successfully")
            else:
                print(msg)

    @classmethod
    @check_permissions(admin_access=True, employee_access=True)
    def show_all_products(cls):
        print(Product.get_products_db())


# Category().save("cloths")
# print(Category.get_all_category())
# Product().save("shoes", 200000, "cloths", 23)
# Product().save("dress", 200000, "cloths", 23)
# print(Product.get_products_db())
# ProductView.delete_product()
# print(Product.get_products_db())
# ProductView.update_product()
# print(Product.get_products_db())