from Customers.customer import Customer


class Individual(Customer):
    def __init__(self, customer_id=None, customer_name=None, customer_phone=None,
                 customer_address=None, lic_number=None):
        self.__lic_number = lic_number
        super().__init__(customer_id, customer_name, customer_phone, customer_address)

    def get_lic_number(self):
        return self.__lic_number
