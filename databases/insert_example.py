import sqlite3

conn = sqlite3.connect('companies.db')

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
VALUES ('Paul', 32, 'California', 20000.00 )");

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Allen', 25, 'Texas', 15000.00 )");

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Teddy', 23, 'Norway', 20000.00 )");

conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Mark', 25, 'Rich-Mond ', 65000.00 )");

company_5_array = ['Amith', 28, 'Kyrgyzstan', 100000]

# Example for inserting with variable
conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) \
VALUES (?,?,?,?)", (company_5_array[0],company_5_array[1],company_5_array[2], company_5_array[3]))



conn.commit()
conn.close()