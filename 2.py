import csv


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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            cls(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        if isinstance(num, float):
            # Count out the floats that are point zero
            print(num)
            return num.is_integer()
        elif isinstance(num, int):
            return True
        return False

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

# for instance in Item.all:
#     print(instance.name)

# Item.instantiate_from_csv()
# print(Item.all)

print(Item.is_integer(7.9))
