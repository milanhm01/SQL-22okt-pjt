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

# check if the table has no rows
if len(rows) == 0:
    # tell the user the database is empty
    print("Databasen er tom, ingen hændelser fundet")
# runs if there is at least one row
else:
    # print a header line with the column names
    print(f"{'ID':<4} {'Titel':<40} {'Kategori':<25} {'Alvor':<8} {'Status':<11} {'Dato':<11}")
    # print a line of dashes under the header
    print("-" * 105)