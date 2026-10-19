import sqlite3

conn = sqlite3.connect("cybershield.db")
cur = conn.cursor()

#unique id for each incident incident_id INTEGER PRIMARY KEY
cur.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    incident_id INTEGER PRIMARY KEY,
    title TEXT,
    category TEXT,
    severity TEXT,
    status TEXT,
    reported_date TEXT,
    description TEXT
)
""")

#saves to the database and closes the connection
conn.commit()
conn.close()
print("Database og tabel er oprettet")
