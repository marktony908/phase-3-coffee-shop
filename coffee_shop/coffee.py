from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name
        self._validate_name()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise ValueError("Name must be a string of at least 3 characters.")

    def _validate_name(self):
        if not isinstance(self.name, str) or len(self.name) < 3:
            raise ValueError("Name must be a string of at least 3 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        total_price = sum(order.price for order in self.orders())
        num_orders = self.num_orders()
        return total_price / num_orders if num_orders > 0 else 0.0
