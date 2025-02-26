import sqlite3
import sys


def query_table(query):
    con = sqlite3.connect("housing_data.sqlite")

    cur = con.cursor()

    return cur.execute(query).fetchall()