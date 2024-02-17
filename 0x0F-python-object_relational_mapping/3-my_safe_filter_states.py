#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa safely
    from MySQL injections
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Ensure the correct number of arguments is provided
    if len(sys.argv) != 5:
        sys.exit(1)

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        cur = db.cursor()

        # Prepare the query with placeholders to prevent MySQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute the query with the state name argument as a parameter
        cur.execute(query, (sys.argv[4],))

        # Fetch all the rows
        rows = cur.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
