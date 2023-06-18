#!/usr/bin/python3


import MySQLdb
import sys

if __name__ == "__main__":
    """script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY %S ORDER BY id ASC")
    value = (sys.argv[4], )
    cur.execute(query, value)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
