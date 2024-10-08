from abc import ABC, abstractmethod

from Texable.taxable_handler import TaxableHandler


class Taxable(ABC):
    # static attribute
    __vat_pct = TaxableHandler.get_value_by_param_name("VAT_PCT")

    @staticmethod
    def get_vat_pct():
        return Taxable.__vat_pct

    @abstractmethod
    def get_tax(self, amount):
        pass


Taxable.get_vat_pct()
