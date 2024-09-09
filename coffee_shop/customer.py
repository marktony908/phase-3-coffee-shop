from order import Order

class Customer:
    def __init__(self, name):
        self.name = name
        self._validate_name()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def _validate_name(self):
        if not isinstance(self.name, str) or not (1 <= len(self.name) <= 15):
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        Order(self, coffee, price)
