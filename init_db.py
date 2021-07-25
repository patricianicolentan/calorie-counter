# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="Joyisacutepotato",
        host="localhost",
        port=3306,
        database="calories"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()


# Try stuff

cur.execute(
	"SELECT servinggrams, caloriesperserving FROM calorielog WHERE food=?", 
	("Adobo",))

for (servinggrams, caloriesperserving) in cur:
	print(f"Serving Size in Grams: {servinggrams}, Calories per Serving: {caloriesperserving}")

#cur.execute("INSERT INTO diary (date, weight) VALUES (2025-03-03, 120)")

conn.commit()

# close connection

conn.close()