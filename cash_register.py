class CashRegister:
    def __init__(self, discount=0):
        if type(discount) != int or discount < 0 or discount > 100:
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total = self.total + price * quantity

        self.items.append({"item": item, "price": price, "quantity": quantity})

        self.previous_transactions.append(
            {"item": item, "price": price, "quantity": quantity}
        )

    def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)

        self.total = self.total - discount_amount

        last = self.previous_transactions.pop()
        self.items.pop()
        self.total = self.total - last["price"] * last["quantity"]

        print(f"After the discount, the total comes to ${self.total:.2f}.")

    def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("No transaction to void.")
            return

        last = self.previous_transactions.pop()
        self.items.pop()

        self.total = self.total - last["price"] * last["quantity"]
