import pytest
from src.menu import Menu

class Test_Menu:
    menu = "Cheeseburger\nDouble Stack Bacon Cheeseburger\nSalad"    

    def test_user_can_see_menu(self):
        MenuObject = Menu()
        assert MenuObject.get_menu() == self.menu

