# import psycopg2
# import os
# from psycopg2 import Error
#
# # def SaveClientData(FirstName, LastName, PhoneNumber):
# #     con = psycopg2.connect(database=os.getenv('PDB_NAME'),
# #                            user=os.getenv('PDB_USER'),
# #                            password=os.getenv('DB_PASSWORD'),
# #                            host=os.getenv('PDB_HOST'),
# #                            port="5433"
# #                            )
# #     print("Database opened successfully")
# #
# #     cur = con.cursor()
# #     cur.execute('''CREATE TABLE clients_details
# #           (ID INT PRIMARY KEY     NOT NULL,
# #           FIRST_NAME           TEXT    NOT NULL,
# #           LAST_NAME            INT     NOT NULL,
# #           PHONE_NUMBER        CHAR(50);''')
# #     print("Table created successfully")
# #
# #     con.commit()
# #     con.close()
#
#
# def SaveClientData(fName, lName, eMail, pNumber):
#     try:
#         conn = psycopg2.connect(database=os.getenv('PDB_NAME'),
#                                 user=os.getenv('PDB_USER'),
#                                 password=os.getenv('DB_PASSWORD'),
#                                 host=os.getenv('PDB_HOST'),
#                                 port="5433"
#                                 )
#
#         cursor = conn.cursor()
#         # SQL query to create a new table
#         create_table_query = ("""CREATE TABLE IF NOT EXISTS clients_details
#               (
#               FirstName VARCHAR (50) NOT NULL,
#               LastName VARCHAR (50) NOT NULL,
#               Email VARCHAR (50) NOT NULL,
#               PhoneNumber text
#               )
#               """)
#
#         insert_table_data = f"INSERT INTO clients_details (FirstName, LastName, Email, PhoneNumber) VALUES ('{fName}', '{lName}', '{eMail}','{pNumber}');"
#         # Execute a command: this creates a new table
#         cursor.execute(create_table_query)
#         cursor.execute(insert_table_data)
#         conn.commit()
#         print("Table created successfully in PostgreSQL ")
#
#     except (Exception, Error) as error:
#         print("Error while connecting to PostgreSQL", error)
#     finally:
#         if conn:
#             cursor.close()
#             conn.close()
#             print("PostgreSQL connection is closed")
#
#
# if __name__ == "__main__":
#     SaveClientData = ("Sagar", "Budhathoki", "sbmagar.sbm99@gmail.com", "1235547854")
