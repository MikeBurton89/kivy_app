import sqlite3
#connect to the database
db_conn = sqlite3.connect('database_address.db')
#cursor object
cur = db_conn.cursor()

#create table
cur.execute('''CREATE TABLE IF NOT EXISTS address(
    id integer PRIMARY KEY,
    street text,
    city text
)''')

db_conn.commit()


