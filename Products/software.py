from Products.product import Product


class Software(Product):
    def __init__(self,  product_id=None, product_name=None, product_retail_price=None,
                 product_description=None,license=None):
        self.__license = license
        super().__init__(product_id, product_name, product_retail_price, product_description)

    def get_licence(self):
        return self.__license
