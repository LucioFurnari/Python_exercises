import sqlite3
import bcrypt

class DataBaseManager:
  def __init__(self, db_name="Users"):
    self.db_name = db_name
    self.connection = sqlite3.connect(self.db_name)
    self.cursor = self.connection.cursor()

  def close(self):
    self.connection.close()

  def connect_and_init(self):

    try:
      self.cursor.execute('''
      CREATE TABLE IF NOT EXISTS DATA_USERS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        USER_NAME TEXT NOT NULL UNIQUE,
        PASSWORD TEXT NOT NULL,
        LAST_NAME TEXT,
        DIRECTION TEXT,
        COMMENT TEXT
      )
      ''')
      self.connection.commit()
      return True
    except sqlite3.Error as error:
        print("Error trying to create the table:", error)
        return False

  def create(self, user_name, password, last_name, direction, comment):
    try:
      hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
      self.cursor.execute(
          '''
          INSERT INTO DATA_USERS (USER_NAME, PASSWORD, LAST_NAME, DIRECTION, COMMENT)
          VALUES (?, ?, ?, ?, ?)
          ''',
          (user_name, hashed_password, last_name, direction, comment)
        )
      self.connection.commit()
      return True
    except sqlite3.IntegrityError:
      print("The name already exists.")
      return False
    except Exception as error:
      print(f"Error creating user: {error}")
      return False

  def read_user(self, user_id):
    try:
      self.cursor.execute(
        '''
          SELECT ID, USER_NAME, LAST_NAME, DIRECTION, COMMENT FROM DATA_USERS WHERE ID = ?
        ''',
        (user_id,)
      )

      return self.cursor.fetchone()
    except Exception as error:
      print(f"Error reading user: {error}")
      return None

  def update_user(self, user_id, user_name, password, last_name, direction, comment):
    try:
      hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
      self.cursor.execute(
        '''
        UPDATE DATA_USERS
        SET USER_NAME = ?, PASSWORD = ?, LAST_NAME = ?, DIRECTION = ?, COMMENT = ?
        WHERE ID = ?
        ''',
        (user_name, hashed_password, last_name, direction, comment, user_id)
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