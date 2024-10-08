from Products.product import Product


class Manual(Product):
    def __init__(self, product_id=None, product_name=None, product_retail_price=None,
                 product_description=None, publisher=None):
        self.__publisher = publisher
        super().__init__(product_id, product_name, product_retail_price, product_description)

    def get_publisher(self):
        return self.__publisher
