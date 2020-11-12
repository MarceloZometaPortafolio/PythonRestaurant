class Item_Ordered:
    item = ""
    price = 0.0
    quantity = 0
    customer_id = 0

    def __init__(self, item_value, price_value, quantity_value, id):
        super().__init__()
        self.item = item_value
        self.price = price_value
        self.quantity = quantity_value
        self.customer_id = id

class Ticket():
    pass

class Order:
    __orders_list = []

    def add_to_order(self, item_name, price, quantity, customer_id):
        new_item = Item_Ordered(item_name, price, quantity, customer_id)

        self.__orders_list.append(new_item)

    def get_orders_by_user(self, user_id):
        orders = []
        
        for item in self.__orders_list:
            if item.customer_id == user_id:
                orders.append(item)

        return orders

    def get_ticket_by_user(self, user):
        ticket = Ticket()
        
        ticket.items_ordered = self.get_orders_by_user(user.get_id())
        ticket.total_price = self.get_total_price(ticket.items_ordered)
        ticket.client = user

        return ticket


    def get_total_price(self, items_ordered):
        total = 0.0

        for item in items_ordered:
            total += (item.price * item.quantity)

        return total

