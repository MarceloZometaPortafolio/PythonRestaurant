import py.test
from src.user import User

class Test_User:

    def test_user_can_login_as_admin(self):
        admin = User(1)

        expected = True       
        actual = admin.login("username", "password")

        assert expected == actual

    def test_user_cant_login_as_admin(self):
        admin = User(1)

        expected = False       
        actual = admin.login("notValid", "password")

        assert expected == actual

    def test_user_can_register(self):
        user = User(1)

        expected = True       
        actual = user.register("username", "password")

        assert expected == actual