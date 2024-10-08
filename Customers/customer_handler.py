from Customers.customer import Customer
from DB.db_connection_factory import DBConnectionFactory


class CustomerHandler:
    @staticmethod
    def insert_customer(customer):
        my_connection = DBConnectionFactory.create_connection()
        sql_statement = ("insert into customers"
                         " ( CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE,CUSTOMER_TYPE_ID )"
                         " values"
                         " (%s,%s,%s,0)")
        values = (customer.get_customer_name(), customer.get_customer_address(), customer.get_customer_phone())
        my_cursor = my_connection.cursor()
        my_cursor.execute(sql_statement, values)
        my_connection.commit()

    @staticmethod
    def update_customer(customer):
        my_connection = DBConnectionFactory.create_connection()
        sql_statement = ("update customers"
                         " set customer_name = %s,"
                         " customer_address = %s,"
                         " customer_phone = %s"
                         " where customer_id = %s ")
        values = (customer.get_customer_name(), customer.get_customer_address(), customer.get_customer_phone(),
                  customer.get_customer_id())
        my_cursor = my_connection.cursor()
        my_cursor.execute(sql_statement, values)
        my_connection.commit()

    @staticmethod
    def delete_customer(customer):
        my_connection = DBConnectionFactory.create_connection()
        sql_statement = ("delete from customers "
                         "where CUSTOMER_ID = %s")
        values = (customer,)
        my_cursor = my_connection.cursor()
        my_cursor.execute(sql_statement, values)
        my_connection.commit()


# Main program
# test insert
# customer_info = Customer(2, "Ahmed", "012458468", "Cairo")
# CustomerHandler.insert_customer(customer_info)

# test update
# customer_info = Customer(4, "zayad", "01245568", "Giza")
# CustomerHandler.update_customer(customer_info)

# test delete
customer_info = Customer(2, "zayad", "01245568", "Giza")
CustomerHandler.delete_customer(customer_info)
