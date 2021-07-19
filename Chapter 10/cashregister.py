#CashRegister Class

class CashRegister:
    def __init__(self, purchase, total, lister, inv, cost):
        self.__purchase=purchase
        self.__total=total
        self.__lister=[]
        self.__inv=[]
        self.__cost=[]


#mutators
    def purchase_item(self, purchase, lister):
        self.__purchase=purchase
        lister.append(purchase)
        return lister

    def set_total(self, price):
        self.__total+=price


    def show_item(self, lister, inventory, price):
        i=0
        while i<len(lister):
            s=('Item # %i\t%s\t\t\t\t%i\t\t\t%4.2f') % ((i+1),lister[i],inventory[i],price[i])
            s = s.strip(' \t\n\r')
            print(s)
            i+=1

    def show_items(self, lister):
        i=0
        print('You have purchased the following items')
        while i<len(lister):
            print(lister[i])
            i+=1

    def clear(self, lister):
        i=0
        while i<len(lister):
            del lister[i]
            i+=1
            return lister

    def get_list(self, lister):
        return lister
#accessors
    def acc_purchase(self):
        return self.__purchase
    def cost_total(self):
        return self.__total
    def acc_show(self):
        return self.__show
    def acc_clear(self):
        return self.__clear
