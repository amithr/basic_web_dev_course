import sqlite3

conn = sqlite3.connect('companies.db')
cursor = conn.execute("SELECT name, address, salary from COMPANY")
for row in cursor:
   print("NAME = ", row[0])
   print("ADDRESS = ", row[1])
   print("SALARY = ", row[2], "\n")

# Try this out with a variable too!
# Practice writing queries
salary_upper_limit = 20000
cursor = conn.execute("SELECT name from COMPANY where salary > ?", (salary_upper_limit,))
for row in cursor:
   print("NAME = ", row[0])

cursor = conn.execute("SELECT rowid, * from COMPANY")
for row in cursor:
   print(row)

conn.close()