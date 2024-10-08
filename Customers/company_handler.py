"""
This file is help for the database connection
file contains CRUD operations for company class
CRUD = [ create , read , update , delete ]
5 main function [ get_all_companies() , get_company_id(company_id) , insert_company(company),
                    update_company(company) , delete_company(company_id) ]
"""
import mysql.connector

from Customers.company import Company
from DB.db_connection_factory import DBConnectionFactory


class CompanyHandler:
    @staticmethod
    def insert_company(company):
        my_connection = None
        try:  # try is used if the code may have any Error
            # 1. create db connection
            my_connection = DBConnectionFactory.create_connection()
            # 2. prepare sql statement
            sql_statement = ("insert into customers"
                             " (CUSTOMER_NAME, CUSTOMER_ADDRESS, CUSTOMER_PHONE, CUSTOMER_CONTACT, "
                             " CUSTOMER_DISCOUNT,CUSTOMER_TYPE_ID)"
                             " values"
                             " ( %s,%s,%s,%s,%s,1)")
            # 3. set parameters ( data )
            values_tuple = (company.get_customer_name(), company.get_customer_address(), company.get_customer_phone(),
                            company.get_contact(), company.get_discount())
            # 4. create cursor and execute sql statement
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values_tuple)
            # 5. commit
            my_connection.commit() # make commit in update , insert and delete only
        except mysql.connector.Error as msg:  # except is used to adjust the massage output when there is Error
            print("Error in insert_company : ", msg)
        finally:  # finally is used to let the code like ( commit ) to execute always
            if my_connection is not None:
                my_connection.close()

    @staticmethod
    def update_company(company):
        my_connection = None
        try:
            # 1. create db connection
            my_connection = DBConnectionFactory.create_connection()
            # 2. prepare sql statement
            sql_statement = ("update customers"
                             ' set customer_name = %s,'
                             ' customer_address = %s,'
                             ' customer_phone = %s,'
                             ' customer_contact = %s,'
                             ' customer_discount = %s'
                             " where customer_id = %s")
            # 3. set parameters ( data )
            values_tuple = (company.get_customer_name(), company.get_customer_address(), company.get_customer_phone(),
                            company.get_contact(), company.get_discount(), company.get_customer_id())
            # 4. create cursor and execute sql statement
            my_cursor = my_connection.cursor()
            my_cursor.execute(sql_statement, values_tuple)
            # 5. commit
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
            values = (customer_id,)  # we add ( , ) bec. the tuple will not accept one value
            # we didn't use get bec. he will give us number only not data
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
            # -------- New ( fetchall ) ---------
            rows = my_cursor.fetchall()  # return all the rows
            # loop on them
            for row in rows:
                customer_id = row[0]
                customer_name = row[1]
                customer_address = row[2]
                customer_phone = row[3]
                customer_contact = row[4]
                customer_discount = row[5]
                # create object from company
                new_company = Company(customer_id, customer_name, customer_phone, customer_address,
                                      customer_contact, customer_discount)
                # append to list
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
            # -------- fetchone() ---------
            rows = my_cursor.fetchone()  # return one row
            if rows is not None:
                customer_id = rows[0]
                customer_name = rows[1]
                customer_address = rows[2]
                customer_phone = rows[3]
                customer_contact = rows[4]
                customer_discount = rows[5]
                # create object from company
                new_company = Company(customer_id, customer_name, customer_phone, customer_address,
                                      customer_contact, customer_discount)
            my_connection.commit()
        except mysql.connector.Error as msg:
            print("Error in get_company_by_id : ", msg)
        finally:
            if my_connection is not None:
                my_connection.close()
        # return list of companies
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
