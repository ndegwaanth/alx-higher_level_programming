#!/usr/bin/python3
"""
    script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             password=sys.argv[2], database=sys.argv[3],
                             port=3306)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")

        cities = cursor.fetchall()

        for city in cities:
            print(city)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: ", e)
        sys.argv(1)
