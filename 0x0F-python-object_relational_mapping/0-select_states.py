import MySQLdb
import sys


def list_states(username, password, database_name):
    # Connect to MySQL server
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database_name, host='localhost', port=3306)
        cursor = db.cursor()
        # Execute the query
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
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
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    list_states(username, password, database_name)
