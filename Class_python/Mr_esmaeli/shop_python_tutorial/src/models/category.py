import itertools


class Category:
    __db = []
    __id = itertools.count(1)

    @classmethod
    def save(cls, name: str = None) -> (bool, str):
        # self.__db.append({"id": next(self.__id), "name": name})
        if not cls.exist(name):
            _id = next(cls.__id)
            cls.__db.append({"id": _id, "name": name})
            return True
        else:
            return False

    @classmethod
    def exist(cls, name: str = None) -> bool:
        if name:
            # for category in self.get_all_category()
            for category in cls.__db:
                if category.get("name") == name:
                    return True
            return False
        else:
            return False

    @classmethod
    def get_one_category(cls, name: str = None) -> dict:
        if name:
            # for category in self.get_all_category()
            for category in cls.__db:
                if category.get("name") == name:
                    return category
            return {}
        else:
            return {}

    @classmethod
    def delete(cls, _id: int):
        for num, category in enumerate(cls.__db, 0):
            if category.get("id") == int(_id):
                del cls.__db[num]
                return True
        return False

    @classmethod
    def update(cls, new_name: str, _id: int) -> (bool, str):
        if Category.exist(new_name):
            return False, "The name is a duplicate"
        for num, category in enumerate(cls.__db, 0):
            if category.get("id") == int(_id):
                category["name"] = new_name
                return True, "update successfully"
        return False, f"sorry,category's {_id} not found"

    @classmethod
    def get_all_category(cls):
        return cls.__db

# a = Category()
# print(a.save("shoes"))
# a.save("cloth")
# print(a.exist("shoes"))
# a.delete(1)


# a.update("bag", 1)
# print(a.get_all_category())
# Category.save("shoes")
# print(Category.get_all_category())
