#!/usr/bin/python3
"""Takes in an argument and display all values in the state
    table where  name matches the argument
"""
import MySQLdb
import sys


def search_states(username, password, database_name, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(user=username,
                             passwd=password,
                             db=database_name,
                             host='localhost', port=3306)
        cursor = db.cursor()

        # Execute the query
        query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, database_name, state_name)
