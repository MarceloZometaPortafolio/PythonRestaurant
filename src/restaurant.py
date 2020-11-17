from src.user import User
from src.menu import Menu

class Restaurant:
    __admins = []
    __users = []
    __menu = Menu()

    def __init__(self):
        self.__initialize_Admins()
        self.__initialize_Users()

    def __initialize_Admins(self):
        admin = User(0, username="admin", password="adminpassword")
        self.__admins.append(admin)

    def __initialize_Users(self):
        user = User(0, username="user", password="userpassword")
        self.__users.append(user)

    def add_to_menu(self, admin, recipe):
        if admin in self.__admins:
            self.__menu.add_item(recipe)

    def get_admins(self):
        return self.__admins

    def get_users(self):
        return self.__users

    def get_menu(self):
        recipes = self.__menu.MenuList
        return recipes