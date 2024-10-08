from Customers.customer import Customer


class Company(Customer):
    def __init__(self, customer_id=None, customer_name=None, customer_phone=None,
                 customer_address=None, contact=None, discount=None):
        self.__contact = contact
        self.__discount = discount
        super().__init__(customer_id, customer_name, customer_phone, customer_address)

    def get_contact(self):
        return self.__contact

    def get_discount(self):
        return self.__discount
