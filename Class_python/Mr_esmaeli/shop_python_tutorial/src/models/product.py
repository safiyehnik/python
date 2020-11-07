import itertools
from src.models.category import Category


class Product:
    __db = []
    __id = itertools.count(1)

    @classmethod
    def save(cls, name: str = None, price: int = None, category: str = None, off: float = None) -> bool:
        new_category = Category.get_one_category(category)
        if new_category:
            g = {
                "id": next(Product.__id),
                "name": name,
                "price": int(price),
                "category_id": new_category.get("id"),
                "off": float(off)
            }
            cls.__db.append(g)
            return True
        else:
            return False

    @classmethod
    def get_products_db(cls):
        # print(cls.products_db)
        return cls.__db

    def __repr__(self):
        return self.name

    @classmethod
    def delete(cls, _id: int) -> bool:
        for product in cls.__db:
            if int(_id) == product.get("id"):
                cls.__db.remove(product)
                return True
        return False

    @classmethod
    def update(cls, _id: int, new_name: str, new_price: int, new_category: str, new_off: float) -> (bool, str):
        if new_category:
            if not Category().exist(new_category):
                return False, f"category [{new_category}] not found please first add new category"
        if _id:
            for product in cls.__db:
                if product.get("id") == int(_id):
                    if new_name:
                        product["name"] = new_name
                    if new_price:
                        product["price"] = int(new_price)
                    if new_category:
                        ca = Category.get_one_category(new_category)
                        product["category_id"] = ca.get("id")
                    if new_off:
                        product["off"] = float(new_off)
                    return True, ""
            return False, f"id: {_id} not found"


    # def update(self, id):
    #     for product in self.__db:
    #         if id == product.__id:
    #             if name:
    #                 product.name = name

# shoes_product_obj = Product("shoes", 200000, "cloths", 23)
# shoes_product_obj.add_product()
# shoes_product_obj.show()

# bag_product_obj = Product("bag", 180000, "cloths", 2.1)
# bag_product_obj.add_product()
# bag_product_obj.show()
# print(shoes_product_obj.id)
# print(bag_product_obj.id)

# products = Product.get_products_db()
#
# for product in products:
#     print(product)
#     print(product.off)
#     print("------------")


# print(Product.__products_db)

# g = itertools.count(1, 2)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# Category().save("cloths")
# print(Category.get_all_category())
# print(Category().exist("cloths"))
# Product().save("shoes", 200000, "cloths", 23)
# Product().save("dress", 200000, "cloths", 23)
# print(Product().update(2,"hat",100,"shoes",4))
# print(Product.get_products_db())

