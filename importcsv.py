# import from CSV

import csv
import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	# open the csv file and assign it to a variable
	employees = csv.reader(open("employees.csv", "rU"))

	#create a new table called employees
	c.execute("CREATE TABLE employees(firstname, lastname)")

	# insert data into table
	c.executemany("INSERT INTO employees(firstname, lastname) VALUES (?, ?)", employees)