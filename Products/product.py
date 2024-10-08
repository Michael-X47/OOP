class Product:
    def __init__(self, product_id=None, product_name=None, product_retail_price=None, product_description=None):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__product_retail_price = product_retail_price
        self.__product_description = product_description

    def get_product_id(self):
        return self.__product_id

    def get_product_name(self):
        return self.__product_name

    def get_product_retail_price(self):
        return self.__product_retail_price

    def get_product_description(self):
        return self.__product_description
