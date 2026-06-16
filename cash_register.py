class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int):
            print("Not valid discount")
            self._discount = 0
            return
        if value < 0 or value > 100:
            print("Not valid discount")
            self._discount = 0
            return
        self._discount = value

    def add_item(self, item, price, quantity):
        self.total += price * quantity
        self.items.append({"item": item, "price": price, "quantity": quantity})
        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

        last = self.previous_transactions.pop()
        self.items.pop()
        self.total -= last["price"] * last["quantity"]

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("No transaction to void.")
            return

        last = self.previous_transactions.pop()
        self.items.pop()
        self.total -= last["price"] * last["quantity"]
