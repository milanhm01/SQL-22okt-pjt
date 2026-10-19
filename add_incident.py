# import sqlite3 so python can talk to sqlite
import sqlite3
# import datetime so we can check if a date is real
from datetime import datetime

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()

# list of the categories we allow
tilladte_kategorier = ["Phishing", "Malware", "Mistænkeligt loginforsøg", "Uautoriseret adgang", "Databrud"]
# list of the severity levels we allow
tilladte_alvor = ["Lav", "Mellem", "Høj", "Kritisk"]
# list of the statuses we allow
tilladte_status = ["Åben", "Undersøges", "Lukket"]

# print the title of the program
print("\n=== Registrer ny hændelse ===")
# print the allowed categories at the start
print("Tilladte kategorier:", ", ".join(tilladte_kategorier))
# print the allowed severity levels at the start
print("Tilladte alvorlighedsgrader:", ", ".join(tilladte_alvor))
# print the allowed statuses at the start
print("Tilladte statusser:", ", ".join(tilladte_status))
# print an empty line before the questions start
print()

# keep asking until the user gives a valid title
while True:
    # ask the user for the title and remove extra spaces
    titel = input("Titel: ").strip()
    # check if the title is empty
    if titel == "":
        # tell the user the title cannot be empty
        print("Titlen må ikke være tom")
        # go back and ask again
        continue
    # leave the loop because the title is valid
    break

# keep asking until the user gives a valid category
while True:
    # ask the user for the category, remove spaces and fix the capital letter
    kategori = input("Kategori: ").strip().capitalize()
    # check if the category is not in the allowed list
    if kategori not in tilladte_kategorier:
        # tell the user the category is not allowed
        print("Ugyldig kategori, vælg en fra listen")
        # go back and ask again
        continue
    # leave the loop because the category is valid
    break

# keep asking until the user gives a valid severity
while True:
    # ask the user for the severity, remove spaces and fix the capital letter
    alvor = input("Alvorlighed: ").strip().capitalize()
    # check if the severity is not in the allowed list
    if alvor not in tilladte_alvor:
        # tell the user the severity is not allowed
        print("Ugyldig alvorlighed, vælg en fra listen")
        # go back and ask again
        continue
    # leave the loop because the severity is valid
    break

# keep asking until the user gives a valid status
while True:
    # ask the user for the status, remove spaces and fix the capital letter
    status = input("Status: ").strip().capitalize()
    # check if the status is not in the allowed list
    if status not in tilladte_status:
        # tell the user the status is not allowed
        print("Ugyldig status, vælg en fra listen")
        # go back and ask again
        continue
    # leave the loop because the status is valid
    break

# keep asking until the user gives a valid date
while True:
    # ask the user for the date and remove extra spaces
    dato = input("Dato (YYYY-MM-DD): ").strip()
    # try to read the text as a real date in the right format
    try:
        # this fails with ValueError if the date is wrong
        datetime.strptime(dato, "%Y-%m-%d")
    # runs if the date is not valid
    except ValueError:
        # tell the user what is wrong
        print("Ugyldig dato, brug formatet YYYY-MM-DD, fx 2026-10-19")
        # go back and ask again
        continue
    # leave the loop because the date is valid
    break

# keep asking until the user gives a valid description
while True:
    # ask the user for the description and remove extra spaces
    beskrivelse = input("Beskrivelse: ").strip()
    # check if the description is empty
    if beskrivelse == "":
        # tell the user the description cannot be empty
        print("Beskrivelsen må ikke være tom")
        # go back and ask again
        continue
    # leave the loop because the description is valid
    break

# save the new incident in the table, the ? are filled in from the tuple
cur.execute(
    "INSERT INTO incidents (title, category, severity, status, reported_date, description) VALUES (?, ?, ?, ?, ?, ?)",
    (titel, kategori, alvor, status, dato, beskrivelse),
)
# save the new row to the database file
conn.commit()
# tell the user the incident was saved, with its new id
print(f"Hændelsen er gemt med ID {cur.lastrowid}")

# close the connection to the database
conn.close()
