#!/usr/bin/python3

""" Importing necessary modules """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ Script that takes in arguments and displays all values in the states
        table of hbtn_0e_0_usa where name matches the argument.
        But this time, write one that is safe from MySQL injections!
    """
    # Connecting to a MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    # Creating cursor
    cur = db.cursor()
    # Executing query
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (argv[4],))
    # Obtaining query results
    query_rows = cur.fetchall()
    # Printing the results
    for row in query_rows:
        print(row)
    # Close cursor
    cur.close()
    # Close connection to database
    db.close()
