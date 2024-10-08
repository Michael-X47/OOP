from Customers.individual import Individual
from DB.db_connection_factory import DBConnectionFactory


class IndividualHandler:
    @staticmethod
    def insert_individual(individual):
        my_connection = DBConnectionFactory.create_connection()
        sql_statement = ("insert into customers"
                         " ( CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE,LIC_NUMBER,CUSTOMER_TYPE_ID )"
                         " values"
                         " (%s,%s,%s,%s,2)")
        values = (individual.get_customer_name(), individual.get_customer_address(), individual.get_customer_phone(),
                  individual.get_lic_number())
        my_cursor = my_connection.cursor()
        my_cursor.execute(sql_statement, values)
        my_connection.commit()

    @staticmethod
    def update_individual(individual):
        my_connection = DBConnectionFactory.create_connection()
        sql_statement = ("update customers"
                         " set customer_name = %s,"
                         " customer_address = %s,"
                         " customer_phone = %s,"
                         " lic_number = %s"
                         " where customer_id = %s ")
        values = (individual.get_customer_name(), individual.get_customer_address(), individual.get_customer_phone(),
                  individual.get_lic_number(), individual.get_customer_id())
        my_cursor = my_connection.cursor()
        my_cursor.execute(sql_statement, values)
        my_connection.commit()

    @staticmethod
    def delete_individual(individual):
        my_connection = DBConnectionFactory.create_connection()
        sql_statement = ("delete from customers "
                         " where CUSTOMER_ID = %s")
        values = (individual,)
        my_cursor = my_connection.cursor()
        my_cursor.execute(sql_statement, values)
        my_connection.commit()


# Main program
# test insert
# individual_info = Individual(2, "mona", "011262468",
#                          "Cairo","111")
# IndividualHandler.insert_individual(individual_info)

# test update
# individual_info = Individual(7, "soha", "01245568",
#                            "Giza","179")
# IndividualHandler.update_individual(individual_info)
# test delete
individual_info = Individual(7, "mona", "01245568",
                             "Giza","161")
IndividualHandler.delete_individual(individual_info)
