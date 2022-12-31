import sqlite3
from sqlite3 import Error

from models import Task

class SQliteRepository:
    def __init__(self):
        self.connection = self.connect()
        self._init(self.connection)



    def connect(self, db_file='./todo.db'):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

    def _init(self, conn):
        query = """CREATE TABLE IF NOT EXISTS tasks (
            id integer PRIMARY KEY,
            title text NOT NULL,
            description text,
            status text NOT NULL
        );"""
        try:
            c = conn.cursor()
            c.execute(query)
        except Error as e:
            print(e)

    def get_all(self):
        try:
            c = self.connection.cursor()
            c.execute("SELECT * FROM tasks")
            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)

    def add(self, task: Task):
        query = ''' INSERT INTO tasks(title,description,status) VALUES(?,?,?) '''
        try:
            c = self.connection.cursor()
            c.execute(query, (task.title, task.description, task.status))
            self.connection.commit()
            return True
        except Error as e:
            print(e)

    def change_status(self, task_id: int, status: str):
        query = ''' UPDATE tasks SET status = ? WHERE id = ?'''
        try:
            c = self.connection.cursor()
            c.execute(query, (status, task_id))
            self.connection.commit()
            return True
        except Error as e:
            print(e)

    def update(self, task_id: int, title: str, description: str, status: str):
        query = ''' UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?'''
        try:
            c = self.connection.cursor()
            c.execute(query, (title, description, status, task_id))
            self.connection.commit()
            return True
        except Error as e:
            print(e)
            print("Err")

    def delete(self, task_id: int):
        query = ''' DELETE FROM tasks WHERE id = ?'''
        try:
            c = self.connection.cursor()
            c.execute(query, (task_id,))
            self.connection.commit()
            return True
        except Error as e:
            print(e)
