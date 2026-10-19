# import sqlite3 so python can talk to sqlite
import sqlite3

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()

# ask the user to confirm and clean up the answer
svar = input("Er du sikker på, at du vil slette alle hændelser? (ja/nej): ").strip().lower()

# check if the user confirmed with ja
if svar == "ja":
    # delete all rows from the incidents table
    cur.execute("DELETE FROM incidents")
    # save the deletion to the database file
    conn.commit()
    # tell the user how many rows were deleted
    print(f"{cur.rowcount} hændelser er slettet")
# runs if the user typed anything else
else:
    # tell the user nothing was deleted
    print("Sletning afbrudt, ingen data er slettet")

# close the connection to the database
conn.close()