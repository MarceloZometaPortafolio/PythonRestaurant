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


    def test_user_can_see_its_total(self):
        order = Order()
        user_one = User(1)
        user_two = User(2)
        menu = Menu()
        
        order.add_to_order("Cheeseburger", menu.get_price_by_item("Cheeseburger"), 2, user_one.get_id())
        order.add_to_order("Double Stack Bacon Cheeseburger", menu.get_price_by_item("Double Stack Bacon Cheeseburger"), 1, user_two.get_id())

        expected = 11
        actual = order.get_ticket_by_user(user_one).total_price

        assert expected == actual