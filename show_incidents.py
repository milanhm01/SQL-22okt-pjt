# import sqlite3 so python can talk to sqlite
import sqlite3

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()

# get all rows from the incidents table
cur.execute("SELECT * FROM incidents")
# put all the rows into a list
rows = cur.fetchall()