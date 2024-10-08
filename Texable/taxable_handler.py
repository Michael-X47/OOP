import mysql.connector

from DB.db_connection_factory import DBConnectionFactory


class TaxableHandler:
    @staticmethod
    def get_value_by_param_name(name):
        my_connection = None
        param_value = -1
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("select PARAM_VALUE"
                             " from parameters"
                             " where PARAM_NAME = %s")
            values = (name,)
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            row = my_cursor.fetchone()
            param_value = row[0]
        except mysql.connector.Error as msg:
            print("Error in get_value_by_param_name :", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        return param_value

    @staticmethod
    def update_value_by_param_name(name, value):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("update parameters "
                             " set PARAM_VALUE=%s "
                             " where PARAM_NAME =%s")
            values = (value, name)
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in get_update_value_by_param_name :", msg)
        finally:
            if my_connection is not None:
                my_connection.close()


# Main
# get by Param name
# print("Vat = ", TaxableHandler.get_value_by_param_name("VAT_PCT"))

# update vat
TaxableHandler.update_value_by_param_name("VAT_PCT", 14)
