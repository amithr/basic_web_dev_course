import sqlite3

conn = sqlite3.connect('companies.db')
query = (''' CREATE TABLE COMPANY
            (NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            ADDRESS        CHAR(50),
            SALARY         REAL);''')
conn.execute(query)
conn.close()