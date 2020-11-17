import py.test
from src.user import User
from src.restaurant import Restaurant

class Test_Admins:
    def test_there_are_admins_in_the_restaurant(self):
        restaurant = Restaurant()

        expected = 1
        actual = len(restaurant.get_admins())

        assert expected == actual

    def test_there_are_users_in_the_restaurant(self):
        restaurant = Restaurant()

        expected = 1
        actual = len(restaurant.get_users())

        assert expected == actual

    def test_admins_can_add_recipes_to_menu(self):
        restaurant = Restaurant()
        admin = restaurant.get_admins()[0]
        recipe = {
            "Steak" : 10.50
        }

        restaurant.add_to_menu(admin, recipe)

        expected = 4
        actual = len(restaurant.get_menu())

        assert expected == actual

    def test_users_cant_add_recipes_to_menu(self):
        restaurant = Restaurant()
        user = restaurant.get_users()[0]
        recipe = {
            "Steak" : 10.50
        }

        restaurant.add_to_menu(user, recipe)

        expected = 3
        actual = len(restaurant.get_menu())

        assert expected == actual