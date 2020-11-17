import py.test
from src.user import User

class Test_User:

    def test_user_can_login(self):
        admin = User(1, username="username", password="password")

        expected = True       
        actual = admin.login("username", "password")

        assert expected == actual

    def test_user_cant_login(self):
        admin = User(1, username="username", password="password")

        expected = False       
        actual = admin.login("notValid", "password")

        assert expected == actual

    def test_user_can_register(self):             
        actual = User.register("username", "password")

        assert isinstance(actual, User) == True