from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('C:/Users/vignesh/Documents/Flssk-Tutorial_26-Aug/membership/members.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

    # C:/Users/vignesh/Documents/Flssk-Tutorial_26-Aug/membership/questions.db