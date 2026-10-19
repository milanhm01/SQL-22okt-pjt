# import sqlite3 so python can talk to sqlite
import sqlite3

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()
