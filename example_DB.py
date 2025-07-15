import sqlite3

## Connect to db
db = sqlite3.connect("FirstDB")

cursor = db.cursor()
# cursor.execute("CREATE TABLE PRODUCTS (Article_name VARCHAR(50), Price INTEGER, Section VARCHAR(20) )")
# cursor.execute("INSERT INTO PRODUCTS VALUES('Ball', 15, 'Sport')")

variousProducts = [
  ("Shirt", 10, "Sport"),
  ("Jar", 90, "Ceramic"),
  ("Toy Truck", 20, "Toy")
]

# cursor.executemany("INSERT INTO PRODUCTS VALUES (?,?,?)", variousProducts)

db.commit()
## Close db
db.close()