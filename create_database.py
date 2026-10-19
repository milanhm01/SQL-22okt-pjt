# data model for cybershield: one table called incidents
# incident_id   - unique id for each incident (INTEGER, primary key)
# title         - title of the incident (TEXT)
# category      - type of security incident (TEXT)
# severity      - Lav, Mellem, Høj or Kritisk (TEXT)
# status        - Åben, Undersøges or Lukket (TEXT)
# reported_date - date reported, format YYYY-MM-DD (TEXT)
# description   - description of the incident (TEXT)

# import sqlite3 so python can talk to sqlite
import sqlite3

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()

# create the incidents table if it doesn't exist yet
cur.execute("""
CREATE TABLE IF NOT EXISTS incidents (
    -- unique id for each incident
    incident_id INTEGER PRIMARY KEY,
    -- title of the incident
    title TEXT,
    -- type of security incident
    category TEXT,
    -- how serious the incident is
    severity TEXT,
    -- current status of the incident
    status TEXT,
    -- date the incident was reported
    reported_date TEXT,
    -- longer description of the incident
    description TEXT
)
""")

# save the changes to the database file
conn.commit()
# close the connection to the database
conn.close()
# tell the user the table is ready
print("Database og tabel er oprettet")
