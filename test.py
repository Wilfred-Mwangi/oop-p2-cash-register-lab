from cash_register import CashRegister

cr = CashRegister(20)
print("Initial total:", cr.total)
print("Items:", cr.items)

cr.add_item("eggs", 2.0, 3)
cr.add_item("milk", 3.5)
print("Total after adding:", cr.total)

print("All items:", cr.items)

cr.apply_discount()
print("Total after discount:", cr.total)

cr.void_last_transaction()
print("Total after void:", cr.total)
print("Items left:", cr.items)
