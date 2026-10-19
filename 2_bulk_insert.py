# import sqlite3 so python can talk to sqlite
import sqlite3
# import the list of fake incidents from the data file
from data.bulk_ai_gen_data import incidents

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()

# insert all incidents from the list into the table
cur.executemany(
    "INSERT INTO incidents (title, category, severity, status, reported_date, description) VALUES (?, ?, ?, ?, ?, ?)",
    incidents,
)

# save the inserted rows to the database file
conn.commit()

# count how many rows are in the table now
cur.execute("SELECT COUNT(*) FROM incidents")
# get the count from the result
antal = cur.fetchone()[0]
# show how many incidents are in the database
print(f"Antal hændelser i databasen: {antal}")

# close the connection to the database
conn.close()