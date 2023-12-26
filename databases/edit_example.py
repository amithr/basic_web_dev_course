import sqlite3

conn = sqlite3.connect('companies.db')

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where rowid = 1")
# Variable example
row_id = 2
salary = 30000
conn.execute("UPDATE COMPANY set SALARY = ? where rowid = ?", (salary, row_id))

conn.execute("UPDATE COMPANY set SALARY = 60000 where salary < 40000")

conn.commit()
print ("Total number of rows updated :", conn.total_changes)

cursor = conn.execute("SELECT name, address, salary from COMPANY")
for row in cursor:
   print("NAME = ", row[0])
   print("ADDRESS = ", row[1])
   print("SALARY = ", row[2], "\n")

conn.close()