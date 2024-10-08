from Products.product import Product
from Texable.taxable import Taxable


class Manual(Product, Taxable):
    def __init__(self, product_id=None, product_name=None, product_retail_price=None,
                 product_description=None,warranty_period=None):
        self.__warranty_period = warranty_period
        super().__init__(product_id, product_name, product_retail_price, product_description)

    def get_warranty_period(self):
        return self.__warranty_period

    def get_tax(self, amount):
        return amount * Taxable.get_vat_pct() / 100
