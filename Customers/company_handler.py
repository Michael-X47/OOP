import mysql.connector

from Customers.company import Company
from DB.db_connection_factory import DBConnectionFactory


class CompanyHandler:
    @staticmethod
    def insert_company(company):
        my_connection = None
        try:  
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("insert into customers"
                             " (CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE, CUSTOMER_CONTACT, "
                             " CUSTOMER_DISCOUNT,CUSTOMER_TYPE_ID)"
                             " values"
                             " ( %s,%s,%s,%s,%s,1)")
            values_tuple = (company.get_customer_name(), company.get_customer_address(), company.get_customer_phone(),
                            company.get_contact(), company.get_discount())
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values_tuple)
            my_connection.commit() # make commit in update , insert and delete only
        except mysql.connector.Error as msg: 
            print("Error in insert_company : ", msg)
        finally:  
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def update_company(company):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("update customers"
                             ' set customer_name = %s,'
                             ' customer_address = %s,'
                             ' customer_phone = %s,'
                             ' customer_contact = %s,'
                             ' customer_discount = %s'
                             " where customer_id = %s")
            values_tuple = (company.get_customer_name(), company.get_customer_address(), company.get_customer_phone(),
                            company.get_contact(), company.get_discount(), company.get_customer_id())
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values_tuple)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in update_company : ", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def delete_company(customer_id):
        my_connection = None
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("delete from customers "
                             "where CUSTOMER_ID = %s")
            values = (customer_id,)  
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in delete_company : ", msg)
        finally:
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def get_all_company():
        my_connection = None
        my_companies_list = []
        try:
            my_connection = DBConnectionFactory.create_connection()
            sql_statement = ("select CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE"
                             ", CUSTOMER_CONTACT, CUSTOMER_DISCOUNT"
                             " from customers"
                             " where customer_type_id = 1")
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement)
            rows = my_cursor.fetchall()  # return all the rows
            for row in rows:
                customer_id = row[0]
                customer_name = row[1]
                customer_address = row[2]
                customer_phone = row[3]
                customer_contact = row[4]
                customer_discount = row[5]
                new_company = Company(customer_id, customer_name, customer_phone, customer_address,
                                      customer_contact, customer_discount)
                my_companies_list.append(new_company)
                my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in get_all_company : ", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        # return list of companies
        return my_companies_list

    @staticmethod
    def get_company_by_id(company_id):
        my_connection = None
        new_company = None
        try:
            my_connection = DBConnectionFactory.create_connection()

            sql_statement = ('select CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE, '
                             ' CUSTOMER_CONTACT, CUSTOMER_DISCOUNT'
                             ' from customers'
                             ' where customer_type_id = 1'
                             ' and customer_id = %s')
            values = (company_id,)
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values)
            rows = my_cursor.fetchone()  # return one row
            if rows is not None:
                customer_id = rows[0]
                customer_name = rows[1]
                customer_address = rows[2]
                customer_phone = rows[3]
                customer_contact = rows[4]
                customer_discount = rows[5]
                new_company = Company(customer_id, customer_name, customer_phone, customer_address,
                                      customer_contact, customer_discount)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in get_company_by_id : ", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        return new_company


# Main program
# test insert

# my_company = Company(customer_name="the end", customer_phone="01235648", customer_address="Cairo",
#            contact="Omar", discount=10)
# if we use None in the class we must write the attribute name
# CompanyHandler.insert_company(my_company)

# test update

# my_company = Company(2, "hero_tech-advanced", "777-999-888",
#             "As suit-eg", "Hussein mohamed", 17)
# CompanyHandler.update_company(my_company)

# test delete
# CompanyHandler.delete_company(9)

# test get_all_companies
companies_list = CompanyHandler.get_all_company()
print(len(companies_list))
for company in companies_list:
    print('id = ', company.get_customer_id())
    print('name = ', company.get_customer_name())
    print('phone = ', company.get_customer_phone())
    print('address = ', company.get_customer_address())
    print('contact = ', company.get_contact())
    print('discount = ', company.get_discount())
    print('----')

# test get_company_by_id
# my_company = CompanyHandler.get_company_by_id(1)
# print('id = ', my_company.get_customer_id())
# print('name = ', my_company.get_customer_name())
# print('phone = ', my_company.get_customer_phone())
# print('address = ', my_company.get_customer_address())
# print('contact = ', my_company.get_contact())
# print('discount = ', my_company.get_discount())
