import sqlite3

def connectionDb():
  db = sqlite3.connect("Users")
  cursor = db.cursor()

  try:
    cursor.execute('''
      CREATE TABLE DATA_USERS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_NAME VARCHAR(50),
        PASSWORD VARCHAR(50),
        LAST_NAME VARCHAR(50),
        DIRECTION VARCHAR(50),
        COMMENT VARCHAR(100)
      )
    ''')

    return True
  except:
    return False