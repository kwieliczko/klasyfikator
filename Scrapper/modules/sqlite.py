import pickle
import sqlite3
import numpy as np
import os

class db_sql_lite_class:
    def open_database(self, db_path):
        try:
            conn = sqlite3.connect(db_path)
        except:
            print("Database opening error:", db_path)
        return conn
        
    def save_data_in_database(self, conn, db_path, rating_star, text_review):
        try:
            conn = sqlite3.connect(db_path)
            sql = '''INSERT INTO reviews VALUES ('''+str(rating_star)+''',"'''+text_review+'''"); '''
            c = conn.cursor()
            c.execute(sql)
            c.execute('commit')
            conn.close()
        except:
            print("Failure to write to the database", db_path)
        
