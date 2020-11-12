import pytest
from src.menu import Menu

class Test_Menu:
    menu = "Cheeseburger\t\t$5.5\nDouble Stack Bacon Cheeseburger\t\t$7.5\nSalad\t\t$2.5\n"    

    def test_user_can_see_menu(self):
        MenuObject = Menu()
        print(self.menu)
        assert MenuObject.get_menu() == self.menu

    def test_can_get_price(self):
        MenuObject = Menu()

        expected = 5.5
        actual = MenuObject.get_price_by_item("Cheeseburger")

        assert expected == actual