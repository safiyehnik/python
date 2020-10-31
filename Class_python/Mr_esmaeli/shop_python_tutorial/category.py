import itertools
from session import Session


class Category:
    __db = []
    __id = itertools.count(1)

    def save(self, name: str = None) -> (bool, str):
        if not Session.is_admin():
            return False, "you don't have any permission "
        # self.__db.append({"id": next(self.__id), "name": name})
        if name:
            return False, "you forgot enter name"
        if not self.exist(name):
                id = next(self.__id)
                self.__db.append({"id": id, "name": name})
                return True, ""
        else:
            return False, f"category {name} exists "

    def exist(self, name: str = None) -> bool:
        if name:
            # for category in self.get_all_category()
            for category in self.__db:
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

    def delete(self, id):
        if not Session.is_admin():
            return False, "you don't have any permission "
        for num, category in enumerate(self.__db, 0):
            if category.get("id") == id:
                del self.__db[num]
                return True
        return False

    @classmethod
    def update(cls, new_name, id: int):
        if not Session.is_admin():
            return False, "you don't have any permission "
        for num, category in enumerate(cls.__db, 0):
            if category.get("id") == id:
                category["name"] = new_name
                return True
        return False




    @classmethod
    def get_all_category(cls):
        return cls.__db


#a = Category()
#print(a.save("shoes"))
#a.save("cloth")
#print(a.exist("shoes"))
# a.delete(1)

#print(a.get_all_category())
#a.update("bag", 1)
#print(a.get_all_category())