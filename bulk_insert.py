# import sqlite3 so python can talk to sqlite
import sqlite3
# import the list of fake incidents from the data file
from bulk_ai_gen_data import incidents

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()