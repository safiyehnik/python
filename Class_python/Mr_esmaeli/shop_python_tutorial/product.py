import itertools
from category import Category
from session import Session

class Product:
    __db = []
    __id = itertools.count(1)

    def save(self, name=None, price=None, category=None, off=None) -> (bool, str):
        if not Session.is_admin():
            return False, "you don't have any permission "
        new_category = Category.get_one_category(category)
        if new_category:
            g = {
                "id": next(Product.__id),
                "name": name,
                "price": int(price),
                "category_id": new_category.get("id"),
                "off": float(off)
            }
            self.__db.append(g)
            return True, f"product {name} add successfully "
        else:
            return False, f"category {category} not exist" \
                          f"plese first add category {category}  "

    @classmethod
    def get_products_db(cls):
        # print(cls.products_db)
        return cls.__db

    def __repr__(self):
        return self.name

    @classmethod
    def delete(cls, id):
        if not Session.is_admin():
            return False, "you don't have any permission "
        for product in cls.__db:
            if id == product.__id:
                cls.__db.remove(product)
    @classmethod
    def update(cls, id: int, new_name: str, new_price: int, new_category: str, new_off: float):
        if not Session.is_admin():
            return False, "you don't have any permission "
        if new_category:
            if not Category().exist(new_category):
                return f"category: {new_category} not found please first add new category"
        if id:
            for product in cls.__db:
                if product.get("id") == id:
                    if new_name:
                        product["name"] = new_name
                    if new_price:
                        product["price"] = int(new_price)
                    if new_category:
                        product["category"] = new_category
                    if new_off:
                        product["off"] = float(new_off)
                    return "update successfully"
            return f"id: {id} not found "
        return "please enter id"





    # def update(self, id):
    #     for product in self.__db:
    #         if id == product.__id:
    #             if name:
    #                 product.name = name


#shoes_product_obj = Product("shoes", 200000, "cloths", 23)
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
#Category().save("cloths")
#print(Category.get_all_category())
#print(Category().exist("cloths"))
#Product().save("shoes", 200000, "cloths", 23)
#Product().save("dress", 200000, "cloths", 23)
#print(Product().update(2,"hat",100,"cloths",4))
#print(Product.get_products_db())

