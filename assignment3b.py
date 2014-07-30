import sqlite3

with sqlite3.connect("newnum.db") as conn:
	c = conn.cursor()

	while True:
		print "Choose an option below: "
		print "1: Average"
		print "2: Max"
		print "3: Min"
		print "4: Sum"
		print "5: Exit"

		sql = {'average': "SELECT avg(num) FROM numbers",
			'maximum': "SELECT max(num) FROM numbers",
			'minimum': "SELECT min(num) FROM numbers",
			'sum': "SELECT sum(num) FROM numbers"}

		input = raw_input("Type a number: ")

		if input == "1":
			c.execute(sql['average'])
			result=c.fetchone()
			print "Average is "+str(result[0])
		elif input == "2":
			c.execute(sql['maximum'])
			result=c.fetchone()
			print "Maximum is "+str(result[0])
		elif input == "3":
			c.execute(sql['minimum'])
			result=c.fetchone()
			print "Minimum is "+str(result[0])
		elif input == "4":
			c.execute(sql['sum'])
			result=c.fetchone()
			print "Sum is "+str(result[0])
		elif input == "5":
			break
		else:
			print
			print "Command not understood"
			print