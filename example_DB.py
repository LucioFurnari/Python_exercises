import sqlite3

## Connect to db
db = sqlite3.connect("FirstDB")

cursor = db.cursor()
# cursor.execute("CREATE TABLE PRODUCTS (Article_name VARCHAR(50), Price INTEGER, Section VARCHAR(20) )")
# cursor.execute("INSERT INTO PRODUCTS VALUES('Ball', 15, 'Sport')")
db.commit()
## Close db
db.close()