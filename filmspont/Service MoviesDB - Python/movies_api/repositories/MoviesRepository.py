import pymysql
from db_config import mysql

class MoviesRepository(object):
    def __init__(self):
        self.conn = mysql.connect()

    def add_Movie(self,name,des,year):
        sql = "INSERT INTO movies(name,description,stars,year) VALUES(%s)"
        data = (name,des,0,year)
        cursor = self.conn.cursor()
        cursor.execute(sql, data)
        self.conn.commit()
        lastrowid = cursor.lastrowid
        cursor.close()
        return lastrowid

    def get_all_Movies(self, page, pagesize, name):
        print(pagesize)
        startat = page*pagesize
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        if name:
            cursor.execute("SELECT id, name, description, stars, year FROM movies WHERE name LIKE %s LIMIT %s, %s", (name,startat, pagesize))
        else:
            cursor.execute("SELECT id, name, description, stars, year FROM movies LIMIT %s, %s", (startat, pagesize))

        rows = cursor.fetchall()
        cursor.close()
        return rows

    def get_Movie_by_id(self, id):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, name, description, stars, year FROM movies WHERE id=%s", id)
        row = cursor.fetchone()
        cursor.close()
        return row

    def update_Movie(self, id, name):
        sql = "UPDATE movies SET name=%s WHERE id=%s"
        data = (name, id,)
        cursor = self.conn.cursor()
        rows_affected = cursor.execute(sql, data)
        self.conn.commit()
        cursor.close()
        return rows_affected

    def delete_Movie(self, id):
        cursor = self.conn.cursor()
        rows_affected = cursor.execute("DELETE FROM movies WHERE id=%s", (id,))
        self.conn.commit()
        cursor.close()
        return rows_affected

    def get_year(self,id):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT year FROM movies WHERE id=%s", id)
        row = cursor.fetchone()
        cursor.close()
        return row

    def get_stars(self,id):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT stars FROM movies WHERE id=%s", id)
        row = cursor.fetchone()
        cursor.close()
        return row

    def get_description(self,id):
        cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT description FROM movies WHERE id=%s", id)
        row = cursor.fetchone()
        cursor.close()
        return row