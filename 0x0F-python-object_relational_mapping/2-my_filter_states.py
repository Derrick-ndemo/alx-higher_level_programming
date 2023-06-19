#!/usr/bin/python3

""" displays all values in the states where name matches argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Connection to database """
    db = MySQLdb.connect(host="localhost", port=3306, user=sargv[1],
                         passwd=argv[2], db=argv[3])

    """ Cursor that execure the query """
    cur = db.cursor()

    """ Query to the database """
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY \
                '{}' ORDER BY id ASC".format(sys.argv[4]))

    """ shows rows in the database """
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """ Close cursor """
    cur.close()

    """ Close connection to database """
    db.close()
