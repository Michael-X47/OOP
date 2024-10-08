import mysql.connector


class DBConnectionFactory:
    user = "root"
    password = "root"
    host = "localhost"
    database = "oe"

    @staticmethod
    def create_connection():
        db_connection = mysql.connector.connect(user=DBConnectionFactory.user,
                                                password=DBConnectionFactory.password,
                                                host=DBConnectionFactory.host,
                                                database=DBConnectionFactory.database)
        db_connection.autocommit = False
        return db_connection

# main program
# my_connection = DBConnectionFactory.create_connection()
# print(my_connection)
