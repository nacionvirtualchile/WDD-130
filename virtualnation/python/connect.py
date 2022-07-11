import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode




def main():
  cnx = conection_to_db()
  create_table(cnx)
  insert_records(cnx)
  print_records(cnx)



## function to connect to the database
## no parameters
## return the conection
def conection_to_db():
  try:
    # cnx = connection.MySQLConnection(user='', password='',
    #                              host='50.16.238.195',
    #                              database='integritech.cl_14180')
    cnx = mysql.connector.connect(user='111_user', password='_savr3131N_',
                              host='15.223.66.26', port='3306',
                              database='111_bd')

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  # else:
  #   cnx.close()
  return cnx


## function to create the table in case the table doesn't exist
## cnx parameter: the conection
## no return
def create_table(cnx):

  cursor = cnx.cursor()

  TABLES = {}
  TABLES['pressing_buttons'] = (
    "CREATE TABLE `pressing_buttons` ("
    "  `id_action` int(11) NOT NULL AUTO_INCREMENT,"
    "  `date` date NOT NULL,"
    "  `action_name` varchar(16) NOT NULL,"
    "  `user_name` varchar(16) NOT NULL,"
    "  PRIMARY KEY (`id_action`)"
    ") ENGINE=InnoDB")


  for table_name in TABLES:
      table_description = TABLES[table_name]
      try:
          print("Creating table {}: ".format(table_name), end='')
          cursor.execute(table_description)
      except mysql.connector.Error as err:
          if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
              print("already exists.")
          else:
              print(err.msg)
      else:
          print("OK")

  # cursor.close()
  # cnx.close()



## function to insert an example in the database
## cnx parameter: the conection
## no return
def insert_records(cnx):

  cursor = cnx.cursor()

  try:
      cursor.execute("insert into pressing_buttons (date, action_name, user_name) VALUES ('2022-07-09', 'Contact_button', 'user_1')")
  except mysql.connector.Error as err:
      if err.errno:
        print(err.msg)
  else:
      print("OK insert_records")
      cnx.commit()




## function to print the records in the table
## cnx parameter: the conection
## no return
def print_records(cnx):

  cursor = cnx.cursor()

  try:
      cursor.execute("select * from pressing_buttons")
  except mysql.connector.Error as err:
      if err.errno:
          print(err.msg)
  else:
      print("OK print_records")
      for record in cursor:
        print(record)



if __name__ == "__main__":
    main()


##OPTION 2
# import requests
# import json

# url="https://integritech.cl/graphql"
# query='{pages{edges{node{title}}}}'
# r=requests.post(url,json={'query': query})
# yjson=json.loads(r.text)

# if r.status_code == 200:
#     for article in yjson['data']['pages']['edges']:
#         print("Titulo: " + article["node"]['title'])
# else:
#   print(r.status_code)
