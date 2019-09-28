import pymysql
from db_config import mysql

class PersonsRepository(object):
    def __init__(self):
        self.conn = mysql.connect()

    def add_Person(self, name):
        sql = "INSERT INTO persons(name) VALUES(%s)"
        data = (name,)
        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()
        lastrowid = cursor.lastrowid
        cursor.close()
        return lastrowid

    def get_all_Persons(self, page, pagesize, name):
        startat = page*pagesize
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        if name:
            cursor.execute("SELECT id, name FROM persons WHERE name LIKE %s LIMIT %s, %s", (name,startat, pagesize))
        else:
            cursor.execute("SELECT id, name FROM persons LIMIT %s, %s", (startat, pagesize))

        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_Person_by_id(self, id):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name FROM persons WHERE id=%s", id)
        row = cursor.fetchone()
        cursor.close()
        return row

    def update_Person(self, id, name):
        sql = "UPDATE persons SET name=%s WHERE id=%s"
        data = (name, id,)
        cursor = self.conn.cursor()
        rows_affected = cursor.execute(sql, data)
        self.conn.commit()
        cursor.close()
        return rows_affected

    def delete_Person(self, id):
        cursor = self.conn.cursor()
        rows_affected = cursor.execute("DELETE FROM persons WHERE id=%s", (id,))
        self.conn.commit()
        cursor.close()
        return rows_affected
