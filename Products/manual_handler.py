import mysql.connector

from DB.db_connection_factory import DBConnectionFactory
from Products.manual import Manual


class ManualHandler:
    @staticmethod
    def insert_manual(manual):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("insert into products"
                             " (PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC)"
                             " values"
                             " (%s,%s,%s)")
            values = (manual.get_product_name(), manual.get_product_retail_price(),
                      manual.get_product_description())
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            # ----- Again steps for manual tabel --------
            v_last_product_id = my_cursor.lastrowid  # lastrowid to get the last parameter he put it
            sql_statement2 = ("insert into manual"
                              " (MANUAL_PUBLISHER, PRODUCT_ID)"
                              " values"
                              " (%s,%s)")
            values_tuple = (manual.get_publisher(), v_last_product_id)
            my_cursor.execute(sql_statement2, values_tuple)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in insert_manual : ", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def update_manual(manual):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("update products"
                             " set product_name = %s,"
                             " product_retail_price = %s,"
                             " product_desc = %s"
                             " where product_id = %s")
            values = (manual.get_product_name(), manual.get_product_retail_price(),
                      manual.get_product_description(), manual.get_product_id())
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            # ------- software table --------
            sql_statement2 = ("update manual "
                              " set MANUAL_PUBLISHER = %s"
                              " where product_id = %s")
            values2 = (manual.get_publisher(), manual.get_product_id())
            my_cursor.execute(sql_statement2, values2)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in update_manual :", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def delete_manual(product_id):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            value = (product_id,)
            my_cursor = my_connection.cursor()
            sql_statement = ("delete from manual"
                             " where product_id =%s")
            my_cursor.execute(sql_statement, value)
            sql_statement2 = ("delete from products"
                              " where product_id = %s")
            my_cursor.execute(sql_statement2, value)
            my_connection.commit()
            pass
        except mysql.connector.Error as msg:
            print("Error in delete_manual :", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def get_all_manual():
        my_connection = None
        list_of_manual = []
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("select products.PRODUCT_ID, PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC,"
                             " MANUAL_PUBLISHER"
                             " from products,manual"
                             " where manual.product_id = products.product_id")
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement)
            rows = my_cursor.fetchall()
            for j in rows:
                new = Manual(j[0], j[1], j[2], j[3], j[4])
                list_of_manual.append(new)
        except mysql.connector.Error as msg:
            print("Error in get_all_manual:", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        return list_of_manual

    @staticmethod
    def get_hardware_by_id(product_id):
        my_connection = None
        list_for_one = []
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = (" select PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC, MANUAL_PUBLISHER"
                             " from products,manual"
                             " where manual.product_id = products.product_id "
                             " and products.product_id = %s")
            values = (product_id,)
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            rows = my_cursor.fetchone()
            new = Manual(product_name=rows[0], product_retail_price=rows[1], product_description=rows[2],
                         publisher=rows[3])
            list_for_one.append(new)
        except mysql.connector.Error as msg:
            print("Error in get_manual_id:", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        return list_for_one


# main program

# Insert
# my_hardware = Manual(product_name='Manual for pc', product_retail_price=50, product_description='Manual',
#                      publisher="Mac")
# ManualHandler.insert_manual(my_hardware)

# Update
# update = Manual(publisher="dell", product_id=24, product_name="Manual for pc", product_retail_price=35,
#                 product_description="Manual")
# ManualHandler.update_manual(update)

# Delete
# ManualHandler.delete_manual(24)

# Get all hardware
# manual_list = ManualHandler.get_all_manual()
# for i in manual_list:
#     print("product id :", i.get_product_id())
#     print("product name :", i.get_product_name())
#     print("product price =", i.get_product_retail_price())
#     print("product description :", i.get_product_description())
#     print("publisher :", i.get_publisher())
#     print("---------------")

# Get by product_id
# result = ManualHandler.get_hardware_by_id(25)
# for i in result:
#     print("product name :", i.get_product_name())
#     print("product price =", i.get_product_retail_price())
#     print("product description :", i.get_product_description())
#     print("publisher :", i.get_publisher())
#     print("---------------")
