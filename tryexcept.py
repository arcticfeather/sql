# INSERT command with error handler

import sqlite3

with sqlite3.connect("new.db") as conn:
	cursor = conn.cursor()

	try:
		cursor.execute("INSERT INTO populations VALUES ('New York City', 'NY', 8200000)")
		cursor.execute("INSERT INTO populations VALUES ('San Francisco', 'CA', 8000000)")

	except sqlite3.OperationalError, e:
		print "Oops! Something went wrong.  Try again..."
		print e