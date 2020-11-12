import py.test
from src.order import Order 
from src.user import User
from src.menu import Menu

class Test_Order:

    def test_user_can_order_something_by_name(self):
        order = Order()
        user = User(1)
        menu = Menu()
        
        order.add_to_order("Cheeseburger", menu.get_price_by_item("Cheeseburger"), 2, user.get_id())

        expected = 1
        actual = len(order.get_orders_by_user(user.get_id()))

        assert expected == actual