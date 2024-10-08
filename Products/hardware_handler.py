import mysql.connector

from DB.db_connection_factory import DBConnectionFactory
from Products.hardware import Manual


class HardwareHandler:
    @staticmethod
    def insert_hardware(hardware):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("insert into products"
                             " (PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC)"
                             " values"
                             " (%s,%s,%s)")
            values = (hardware.get_product_name(),
                      hardware.get_product_retail_price()+hardware.get_tax(hardware.get_product_retail_price()),
                      hardware.get_product_description())
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            v_last_product_id = my_cursor.lastrowid  
            sql_statement2 = ("insert into hardware"
                              " (HARDWARE_WARRANTY_PRD, PRODUCT_ID)"
                              " values"
                              " (%s,%s)")
            values_tuple = (hardware.get_warranty_period(), v_last_product_id)
            my_cursor.execute(sql_statement2, values_tuple)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in insert_Hardware : ", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def update_hardware(hardware):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("update products"
                             " set product_name = %s,"
                             " product_retail_price = %s,"
                             " product_desc = %s"
                             " where product_id = %s")
            values = (hardware.get_product_name(),
                      hardware.get_product_retail_price()+hardware.get_tax(hardware.get_product_retail_price()),
                      hardware.get_product_description(), hardware.get_product_id())
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            sql_statement2 = ("update hardware "
                              " set HARDWARE_WARRANTY_PRD = %s"
                              " where product_id = %s")
            values2 = (hardware.get_warranty_period(), hardware.get_product_id())
            my_cursor.execute(sql_statement2, values2)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in update_hardware :", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def delete_hardware(product_id):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            value = (product_id,)
            my_cursor = my_connection.cursor()
            sql_statement = ("delete from hardware"
                             " where product_id =%s")
            my_cursor.execute(sql_statement, value)
            sql_statement2 = ("delete from products"
                              " where product_id = %s")
            my_cursor.execute(sql_statement2, value)
            my_connection.commit()
            pass
        except mysql.connector.Error as msg:
            print("Error in delete_hardware :", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def get_all_hardware():
        my_connection = None
        list_of_hardware = []
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("select products.PRODUCT_ID, PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC,"
                             " HARDWARE_WARRANTY_PRD"
                             " from products,hardware"
                             " where hardware.product_id = products.product_id")
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement)
            rows = my_cursor.fetchall()
            for j in rows:
                new = Manual(j[0], j[1], j[2], j[3], j[4])
                list_of_hardware.append(new)
        except mysql.connector.Error as msg:
            print("Error in get_all_hardware:", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        return list_of_hardware

    @staticmethod
    def get_hardware_by_id(product_id):
        my_connection = None
        list_for_one = []
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = (" select PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC, HARDWARE_WARRANTY_PRD"
                             " from products,hardware"
                             " where hardware.product_id = products.product_id "
                             " and products.product_id = %s")
            values = (product_id,)
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            rows = my_cursor.fetchone()
            new = Manual(product_name=rows[0], product_retail_price=rows[1], product_description=rows[2],
                         warranty_period=rows[3])
            list_for_one.append(new)
        except mysql.connector.Error as msg:
            print("Error in get_hardware_by_id:", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        return list_for_one


# main program

# Insert
# my_hardware = Hardware(product_name='Printer 2020', product_retail_price=400, product_description='Printer',
#                        warranty_period=1)
# HardwareHandler.insert_software(my_hardware)

# Update
# update = Hardware(warranty_period=2, product_id=20, product_name="Printer-2020", product_retail_price=250,
#                   product_description="Printer")
# HardwareHandler.update_hardware(update)

# Delete
# HardwareHandler.delete_hardware(19)

# Get all hardware
# hardware_list = HardwareHandler.get_all_hardware()
# for i in hardware_list:
#     print("product id :", i.get_product_id())
#     print("product name :", i.get_product_name())
#     print("product price =", i.get_product_retail_price())
#     print("product description :", i.get_product_description())
#     print("warranty  :", i.get_warranty_period())
#     print("---------------")

# Get by product_id
# result = HardwareHandler.get_hardware_by_id(20)
# for i in result:
#     print("product name :", i.get_product_name())
#     print("product price =", i.get_product_retail_price())
#     print("product description :", i.get_product_description())
#     print("warranty :", i.get_warranty_period())
#     print("---------------")
