from item import Item


class Phone(Item):
    def __int__(self, name: str, price: float, quantity: 0, broken_phones: 0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones


# Item.instantiate_from_csv()
# phone1 = Phone('Iphone 12', 999.99, 10)
# phone2 = Phone('Iphone 14', 1299.99, 100)
# print(phone1.calculate_total_price())
# # print(Phone.all)
# print(Item.all)
