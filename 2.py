class Item:
    # Class level attribute
    pay_rate = 0.8  # Pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: 0):
        # Run validations on received arguments
        assert price >= 0, f'Price {price} is not greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Execute actions
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # pay_rate should be access from instance level so that we can use instance attributes when they are provided
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f'Item(\'{self.name}\', {self.price}, {self.quantity})'


# item1 = Item('Phone', 99.99, 5)
# item2 = Item('Laptop', 999.99, 2)
# t = item1.calculate_total_price()
# print(t)
# item1.pay_rate = 0.9
# print(Item.__dict__)
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item1.__dict__)
# print(item2.pay_rate)
# item1.apply_discount()
# print(item1.price)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name)

print(Item.all)
