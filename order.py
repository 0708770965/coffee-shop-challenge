class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer,):
            raise TypeError("coffee")
        if not isinstance(coffee,):
            raise TypeError("customer")
        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("11.5")

        self._customer = customer
        self._coffee = coffee
        self._price = price

    def customer(self):
        return self._customer

    def coffee(self):
        return self._coffee

    def price(self):
        return self._price
