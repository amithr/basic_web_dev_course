import sqlite3

conn = sqlite3.connect('companies.db')

row_id = 1
conn.execute("DELETE from COMPANY where rowid = ?",(row_id,))
conn.commit()
print("Total number of rows deleted :", conn.total_changes)


cursor = conn.execute("SELECT name, address, salary from COMPANY")
for row in cursor:
   print("NAME = ", row[0])
   print("ADDRESS = ", row[1])
   print("SALARY = ", row[2], "\n")

conn.close()