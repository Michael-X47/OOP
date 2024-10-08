import mysql.connector

from DB.db_connection_factory import DBConnectionFactory
from Products.software import Software


class SoftwareHandler:
    @staticmethod
    def insert_software(software):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("insert into products"
                             " (PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC)"
                             " values"
                             " (%s,%s,%s)")
            values = (software.get_product_name(), software.get_product_retail_price(),
                      software.get_product_description())
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            v_last_product_id = my_cursor.lastrowid  # lastrowid to get the last parameter he put it
            sql_statement2 = ("insert into software"
                              " (SOFTWARE_LICENCE, PRODUCT_ID)"
                              " values"
                              " (%s,%s)")
            values_tuple = (software.get_licence(), v_last_product_id)
            my_cursor.execute(sql_statement2, values_tuple)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in insert_software : ", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def update_software(software):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("update products"
                             " set product_name = %s,"
                             " product_retail_price = %s,"
                             " product_desc = %s"
                             " where product_id = %s")
            values = (software.get_product_name(), software.get_product_retail_price(),
                      software.get_product_description(), software.get_product_id())
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            sql_statement2 = ("update software "
                              " set software_licence = %s"
                              " where product_id = %s")
            values2 = (software.get_licence(), software.get_product_id())
            my_cursor.execute(sql_statement2, values2)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in update_software :", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def delete_software(product_id):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            value = (product_id,)
            my_cursor = my_connection.cursor()
            sql_statement = ("delete from software"
                             " where product_id =%s")
            my_cursor.execute(sql_statement, value)
            sql_statement2 = ("delete from products"
                              " where product_id = %s")
            my_cursor.execute(sql_statement2, value)
            my_connection.commit()
            pass
        except mysql.connector.Error as msg:
            print("Error in delete_software :", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def get_all_software():
        my_connection = None
        list_of_software = []
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("select products.PRODUCT_ID, PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC,"
                             " SOFTWARE_LICENCE"
                             " from products,software"
                             " where software.product_id = products.product_id")
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement)
            rows = my_cursor.fetchall()
            for j in rows:
                new = Software(j[0], j[1], j[2], j[3], j[4])
                list_of_software.append(new)
        except mysql.connector.Error as msg:
            print("Error in get_all_software:", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        return list_of_software

    @staticmethod
    def get_software_by_id(product_id):
        my_connection = None
        list_for_one = []
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = (" select PRODUCT_NAME, PRODUCT_RETAIL_PRICE, PRODUCT_DESC, SOFTWARE_LICENCE"
                             " from products,software"
                             " where software.product_id = products.product_id "
                             " and products.product_id = %s")
            values = (product_id,)
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            rows = my_cursor.fetchone()
            new = Software(product_name=rows[0], product_retail_price=rows[1], product_description=rows[2],
                           license=rows[3])
            list_for_one.append(new)
        except mysql.connector.Error as msg:
            print("Error in get_software_by_id:", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        return list_for_one


# main program

# Insert
# my_software = Software(product_name='Office 2022', product_retail_price=300, product_description='My Office',
#                        license='126-7855-98')
# SoftwareHandler.insert_software(my_software)

# Update
# update = Software(license="48175-95", product_id=10, product_name="Office2025", product_retail_price=600,
#                product_description="New office")
# SoftwareHandler.update_software(update)

# Delete
# SoftwareHandler.delete_software(13)

# Get all software
# software_list = SoftwareHandler.get_all_software()
# for i in software_list:
#     print("product id :", i.get_product_id())
#     print("product name :", i.get_product_name())
#     print("product price =", i.get_product_retail_price())
#     print("product description :", i.get_product_description())
#     print("licence :", i.get_licence())
#     print("---------------")

# Get by product_id
# result = SoftwareHandler.get_software_by_id(11)
# for i in result:
#     print("product name :", i.get_product_name())
#     print("product price =", i.get_product_retail_price())
#     print("product description :", i.get_product_description())
#     print("licence :", i.get_licence())
#     print("---------------")
