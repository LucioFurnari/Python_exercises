import sqlite3

class DataBaseManager:
  def __init__(self, db_name="Users"):
    self.db_name = db_name
    self.connection = None
    self.cursor = None

  def connect_and_init(self):
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()

    try:
      self.cursor.execute('''
      CREATE TABLE DATA_USERS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_NAME VARCHAR(50),
        PASSWORD VARCHAR(50),
        LAST_NAME VARCHAR(50),
        DIRECTION VARCHAR(50),
        COMMENT VARCHAR(100)
      )
      ''')
      self.connection.commit()
      return True
    except sqlite3.OperationalError as error:
      if "already exists" in str(error):
        return False
      else:
        raise