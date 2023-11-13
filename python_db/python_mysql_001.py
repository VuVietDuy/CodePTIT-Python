import mysql.connector

cnx = mysql.connector.connect(user='root', password='vuvietduy1234',
                              host='127.0.0.1',
                              database='demo')
print(cnx)
cnx.close()



# Installation
# pip install mysql-connector-python

# Upgrade
# pip install mysql-connector-python --upgrade