#!/usr/bin/python3

""" Importing MySQLdb for database tasks. """

import MySQLdb

""" script that lists all states with a name starting with N """

if __name__ == "__main__":
    """ Connects with database and creates cursor """
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="hbtn_0e_0_usa")
    cur = db.cursor()

    """ Selects all the states with a name starting with N """
    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()

    """ Clean up """
    for row in rows:
        print(row)

    """ Close cursor and connection to database """
    cur.close()
    db.close()
