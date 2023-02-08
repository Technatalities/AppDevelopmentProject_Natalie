from flask_login import UserMixin
import json
import shelve

class Account(UserMixin):
    def __init__(self, fname, lname, email, password, username, birthdate, age, admin):
        self.fname = fname
        self.lname = lname
        self.__email = email
        self.password = password
        self.username = username
        self.birthdate = birthdate
        self.age = age
        self.__admin = admin
        self.__id = Account.id_gen(self)

    def __repr__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def id_gen(self):
        total = 0
        for i in self.__email:
            total = ord(i) + total
        id = hex(total)
        return id + "00"

    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email

    def get_admin(self):
        return self.__admin