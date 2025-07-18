import sqlite3

class DataBaseManager:
  def __init__(self, db_name="Users"):
    self.db_name = db_name
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()

  def connect_and_init(self):

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

  def create(self, user_name, password, last_name, direction, comment):
    try:
      self.cursor.execute(
          '''
          INSERT INTO DATA_USERS (USER_NAME, PASSWORD, LAST_NAME, DIRECTION, COMMENT)
          VALUES (?, ?, ?, ?, ?)
          ''',
          (user_name, password, last_name, direction, comment)
        )
      self.connection.commit()
      return True
    except Exception as error:
      print(f"Error creating user: {error}")
      return False

  def read_user(self, user_id):
    try:
      self.cursor.execute(
        '''
          SELECT * FROM DATA_USERS WHERE ID = ?
        ''',
        (user_id)
      )

      return self.cursor.fetchone()
    except Exception as error:
      print(f"Error reading user: {error}")
      return None

  def update_user(self, user_id, user_name, password, last_name, direction, comment):
    try:
      self.cursor.execute(
        '''
        UPDATE DATA_USERS
        SET USER_NAME = ?, PASSWORD = ?, LAST_NAME = ?, DIRECTION = ?, COMMENT = ?
        WHERE ID = ?
        ''',
        (user_name, password, last_name, direction, comment, user_id)
      )
      self.connection.commit()
      return True
    except Exception as error:
      print(f"Error updating the user: {error}")
      return False

  def delete_user(self, user_id):
    try:
      self.cursor.execute(
        '''
        DELETE FROM DATA_USERS WHERE ID = ?
        ''',
        (user_id)
      )
      self.connection.commit()
      return True
    except Exception as error:
      print(f"Error deleting the user: {error}")
      return False