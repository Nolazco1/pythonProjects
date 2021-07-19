class RetailItem:
    def __init__(self, desc, inventory, price):
        self.__desc=desc
        self.__inventory=inventory
        self.__price=price

#mutators
    def set_desc (self, desc):
        self.__desc=desc
    def set_inventory (self, inventory):
        self.__inventory=inventory
    def set_price (self, price):
        self.__price = price

#accessors
    def get_desc(self):
        return self.__desc
    def get_inventory(self):
        return self.__inventory
    def get_price(self):
        return self.__price

    def __str__(self):
        return 'Item Description:' + self.__desc, \
              '\tNumber of Units:' + self.__inventory, \
              '\tPrice: $' + self.__price

