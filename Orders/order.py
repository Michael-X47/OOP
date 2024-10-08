from datetime import datetime

from Orders.order_item import OrderItem


class Order:
    def __init__(self, order_id, customer):
        self.__order_id = order_id
        self.__customer = customer
        self.__items_list = []
        self.__items_list_quantity = []
        self.__order_date = datetime.now().date()  # today date
        self.__order_total = 0.0

    def get_order_id(self):
        return self.__order_id

    def get_customer(self):
        return self.__customer

    def get_item_list(self):
        return self.__items_list

    def get_items_list_quantity(self):
        return self.__items_list_quantity

    def get_order_date(self):
        return self.__order_date

    def get_order_total(self):
        total = 0
        for i in self.__items_list:
            total = total + i.calc_item_total()
            self.__order_total = total
        return self.__order_total

    # Methods

    def preview_order_receipt(self):
        print("---------- Order data -------")
        print("order id : ", self.__order_id)
        print("order date : ", self.__order_date)
        print("customer : ", self.__customer.get_customer_name())
        print("total = ", self.get_order_total())
        print("------ item list -------")
        for item in self.__items_list:
            print("line number :", item.get_line_nbr())
            print("product name : ", item.get_product().get_product_name())
            print("quantity : ", item.get_quantity())
            print("unit price = ", item.calc_unit_price())
            print("item tax = ", item.calc_item_tax())
            print("item total = ", item.calc_item_total())
            print("---------------")

    def add_product_to_cart(self, new_product):
        if_found = False  
        for i in self.__items_list:
            if i.get_product().get_product_id() == new_product.get_product_id(): 
                current_quantity = i.get_quantity()
                i.set_quantity(current_quantity + 1)
                if_found = True
                break
        if not if_found: 
            item_object = OrderItem(new_product, 1)  
            self.__items_list.append(item_object)

    def add_product_quantity_to_cart(self, product, quantity):
        self.__items_list_quantity.append((product, quantity))
