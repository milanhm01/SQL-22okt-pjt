# import sqlite3 so python can talk to sqlite
import sqlite3
# import csv so python can read csv files
import csv
# import datetime so we can check if a date is real
from datetime import datetime
# import the list of fake incidents from the data file
from data.bulk_ai_gen_data import incidents

# the columns a csv file must have, in this order
kolonner = ["title", "category", "severity", "status", "reported_date", "description"]
# list of the categories we allow
tilladte_kategorier = ["Phishing", "Malware", "Mistænkeligt loginforsøg", "Uautoriseret adgang", "Databrud"]
# list of the severity levels we allow
tilladte_alvor = ["Lav", "Mellem", "Høj", "Kritisk"]
# list of the statuses we allow
tilladte_status = ["Åben", "Undersøges", "Lukket"]


# check one csv row and return an error text, or an empty text if the row is ok
def tjek_raekke(raekke):
    # check that the row has exactly 6 values
    if len(raekke) != 6:
        # return the error text
        return "der skal være præcis 6 kolonner"
    # remove spaces and fix capital letters, same as in 6_add_incident.py
    titel = raekke[0].strip()
    kategori = raekke[1].strip().capitalize()
    alvor = raekke[2].strip().capitalize()
    status = raekke[3].strip().capitalize()
    dato = raekke[4].strip()
    beskrivelse = raekke[5].strip()
    # check that the title is not empty
    if titel == "":
        return "titlen er tom"
    # check that the category is allowed
    if kategori not in tilladte_kategorier:
        return f"ugyldig kategori '{kategori}'"
    # check that the severity is allowed
    if alvor not in tilladte_alvor:
        return f"ugyldig alvorlighed '{alvor}'"
    # check that the status is allowed
    if status not in tilladte_status:
        return f"ugyldig status '{status}'"
    # check that the date is real and in the right format
    try:
        # this fails with ValueError if the date is wrong
        datetime.strptime(dato, "%Y-%m-%d")
    # runs if the date is not valid
    except ValueError:
        return f"ugyldig dato '{dato}' (brug YYYY-MM-DD)"
    # check that the description is not empty
    if beskrivelse == "":
        return "beskrivelsen er tom"
    # the row is ok
    return ""


# print the menu title
print("\n=== Indsæt hændelser ===")
# print option 1
print("1. Indsæt de 100 indbyggede testhændelser")
# print option 2
print("2. Importér hændelser fra en CSV-fil")
# ask the user which option they want
valg = input("Vælg (1-2): ").strip()

# check if the user chose the built-in test data
if valg == "1":
    # use the list from the data file
    rows = incidents
# check if the user chose a csv file
elif valg == "2":
    # tell the user how the csv file must look
    print("\nCSV-filen skal have denne første linje (overskrifter):")
    # show the header line
    print(",".join(kolonner))
    # tell the user how the following lines must look
    print("og derefter én hændelse pr. linje, fx:")
    # show an example row
    print('Falsk mail,Phishing,Mellem,Lukket,2026-10-19,"Linket blev blokeret, ingen skade"')
    # remind the user about commas in text
    print("Tekst med komma skal stå i citationstegn. Se også data/example_incidents.csv")
    # ask for the path and remove spaces and quotes
    sti = input("\nSti til CSV-filen: ").strip().strip("'\"")
    # try to open and read the file
    try:
        # open the file, utf-8-sig also accepts files saved from excel
        fil = open(sti, encoding="utf-8-sig", newline="")
        # read all lines into a list of rows
        alle = list(csv.reader(fil))
        # close the file again
        fil.close()
    # runs if the file does not exist
    except FileNotFoundError:
        # tell the user and stop
        print("Filen blev ikke fundet")
        exit()
    # check that the first line is the right header
    if len(alle) == 0 or [navn.strip() for navn in alle[0]] != kolonner:
        # tell the user and stop
        print("Første linje skal være overskrifterne vist ovenfor")
        exit()
    # empty list for the rows that are ok
    rows = []
    # counter for the rows with errors
    antal_fejl = 0
    # go through every line after the header, line numbers start at 2
    for nr, raekke in enumerate(alle[1:], start=2):
        # check the row and get an error text
        fejl = tjek_raekke(raekke)
        # check if the row has an error
        if fejl != "":
            # show which line is wrong and why
            print(f"Linje {nr}: {fejl}")
            # count the error
            antal_fejl = antal_fejl + 1
        # runs if the row is ok
        else:
            # add the cleaned row to the list
            rows.append((raekke[0].strip(), raekke[1].strip().capitalize(), raekke[2].strip().capitalize(),
                         raekke[3].strip().capitalize(), raekke[4].strip(), raekke[5].strip()))
    # check if any row had an error
    if antal_fejl > 0:
        # insert nothing, so the file can be fixed and tried again
        print(f"{antal_fejl} fejl fundet, ingen hændelser er indsat")
        exit()
    # check that the file had at least one row
    if len(rows) == 0:
        # tell the user and stop
        print("Filen indeholder ingen hændelser")
        exit()
# runs if the user typed anything else
else:
    # tell the user the choice was not valid and stop
    print("Ugyldigt valg, skriv 1 eller 2")
    exit()

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()

# insert all incidents from the list into the table
cur.executemany(
    "INSERT INTO incidents (title, category, severity, status, reported_date, description) VALUES (?, ?, ?, ?, ?, ?)",
    rows,
)

# save the inserted rows to the database file
conn.commit()

# tell the user how many incidents were inserted
print(f"{len(rows)} hændelser er indsat")

# count how many rows are in the table now
cur.execute("SELECT COUNT(*) FROM incidents")
# get the count from the result
antal = cur.fetchone()[0]
# show how many incidents are in the database
print(f"Antal hændelser i databasen: {antal}")

# close the connection to the database
conn.close()
