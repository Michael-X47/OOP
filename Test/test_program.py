from Customers.company import Company
from Orders.order import Order
from Products.hardware import Hardware
from Products.manual import Manual

# create products objects
my_keyboard = Hardware(1, 100, "Keyboard asus", 250
                       , "gaming keyboard")
my_office = Hardware(5, 200, "Office2021", 30
                     , "Office Use")
my_magazine = Manual("taha hasan", 1, "the way", 50
                     , "help u to know ur way")
my_printer = Hardware(5, 101, "Sony printer", 1000
                      , "A4 printer")
my_scanner = Hardware(5, 102, "Hp scanner", 500
                      , "high quality scanner")

# create customers
raya_company = Company(100, 20, 1, "Mohamed", "0124525"
                       , "Cairo")
vodafone_company = Company(101, 10, 1, "zayad", "0125485"
                           , "Alex.")
# create orders
order1000 = Order(1000, raya_company)

# add products
order1000.add_product_to_cart(my_office)
order1000.add_product_to_cart(my_printer)
order1000.add_product_to_cart(my_printer)
order1000.add_product_to_cart(my_printer)
order1000.add_product_to_cart(my_printer)
order1000.add_product_to_cart(my_printer)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_to_cart(my_magazine)
order1000.add_product_quantity_to_cart(my_office, 5)
# preview receipt
order1000.preview_order_receipt()

