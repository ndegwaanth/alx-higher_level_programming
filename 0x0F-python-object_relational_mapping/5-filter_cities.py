#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             port=3306)
        cur = db.cursor()

        # Prepare the query with a placeholder to prevent SQL injection
        query = "SELECT * FROM cities WHERE state_id=(SELECT id FROM states WHERE name=%s) ORDER BY cities.id ASC"

        # Execute the query with the state name provided as a parameter
        cur.execute(query, (sys.argv[4],))

        # Fetch all the rows
        cities = cur.fetchall()

        # Display the results
        for city in cities:
            print(city)

        # Close cursor and database connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
