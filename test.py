from cash_register import CashRegister

cr = CashRegister(20)
print("Initial total:", cr.total)
print("Discount:", cr.discount)

cr.add_item("eggs", 2.0, 3)
print("After eggs - total:", cr.total)
print("Items:", cr.items)

cr.add_item("milk", 3.5, 1)
print("After milk - total:", cr.total)
print("Previous transactions:", cr.previous_transactions)

cr.apply_discount()
print("After apply_discount - total:", cr.total)
print("Items left:", cr.items)
print("Previous transactions left:", cr.previous_transactions)

cr.void_last_transaction()
print("After void_last_transaction - total:", cr.total)
print("Items left:", cr.items)
print("Previous transactions left:", cr.previous_transactions)
