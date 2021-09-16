#Create Retail Item class
class RetailItem:
    #Intialize object with data attributes
    def __init__(self, descr, inv, price):
        self.__description = descr
        self.__units = inv
        self.__price = price
    #Mutator methods
    def set_descr(self, descr):
        self.__description = descr
    
    def set_inventory(self, units):
        self.__units = units
    
    def set_price(self, price):
        self.__price = price
    #Accessor methods
    def get_descr(self):
        return self.__description

    def get_inventory(self):
        return self.__units
    
    def get_price(self):
        return self.__price