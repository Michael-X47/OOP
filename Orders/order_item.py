from Products.hardware import Manual


class OrderItem:
    __static_line_number = 1

    def __init__(self, product, quantity):
        self.__line_nbr = OrderItem.__static_line_number  
        OrderItem.__static_line_number = OrderItem.__static_line_number + 1
        self.__product = product  
        self.__quantity = quantity 

    def get_line_nbr(self):
        return self.__line_nbr

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

    # Extra methods
    def calc_unit_price(self):
        return self.__product.get_product_retail_price()

    def calc_item_tax(self): 
        amount = self.calc_unit_price() * self.get_quantity()
        if isinstance(self.__product, Manual):
            return self.__product.get_tax(amount)
        else:
            return 0

    def calc_item_total(self):
        return self.calc_item_tax() + self.__quantity * self.calc_unit_price()
