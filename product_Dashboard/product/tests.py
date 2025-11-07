from django.test import TestCase

# Create your tests here.

import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="root",
    db="product_dashboard"
)

cursor = db.cursor()
cursor.execute("SHOW TABLES;")
print(cursor.fetchall())
db.close()
