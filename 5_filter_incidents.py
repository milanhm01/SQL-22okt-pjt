# import sqlite3 so python can talk to sqlite
import sqlite3

# open connection to the database file
conn = sqlite3.connect("cybershield.db")
# create cursor so we can run sql commands
cur = conn.cursor()

# keep showing the menu until the user chooses to quit
while True:
    # print the filter menu title
    print("\n=== Filtrer hændelser ===")
    # print option 1
    print("1. Alvorlighedsgrad (Lav, Mellem, Høj, Kritisk)")
    # print option 2
    print("2. Status (Åben, Undersøges, Lukket)")
    # print option 3
    print("3. Kategori")
    # print option 0
    print("0. Tilbage")
    # ask the user which filter they want
    valg = input("Vælg filter (0-3): ")

    # check if the user wants to leave
    if valg == "0":
        # leave the loop
        break
    # check if the user chose severity
    elif valg == "1":
        # we pick the column name ourselves
        kolonne = "severity"
    # check if the user chose status
    elif valg == "2":
        # we pick the column name ourselves
        kolonne = "status"
    # check if the user chose category
    elif valg == "3":
        # we pick the column name ourselves
        kolonne = "category"
    # runs if the user typed anything else
    else:
        # tell the user the choice was not valid
        print("Ugyldigt valg, skriv 0, 1, 2 eller 3")
        # go back to the menu and ask again
        continue

    # ask the user which value to search for and fix the capital letter
    soegeord = input("Skriv værdien du vil søge efter: ").strip().capitalize()

    # get all rows where the chosen column matches the value
    cur.execute(f"SELECT * FROM incidents WHERE {kolonne} = ?", (soegeord,))
    # put all the matching rows into a list
    rows = cur.fetchall()

    # check if no rows matched the search
    if len(rows) == 0:
        # tell the user nothing was found
        print(f"Ingen hændelser fundet for {kolonne} = {soegeord}")
    # runs if at least one row matched
    else:
        # tell the user how many incidents were found
        print(f"\nFandt {len(rows)} hændelser:\n")
        # print a header line with the column names
        print(f"{'ID':<4} {'Titel':<45} {'Kategori':<25} {'Alvor':<8} {'Status':<11} {'Dato':<11}")
        # print a line of dashes under the header
        print("-" * 110)
        # loop through every matching row
        for row in rows:
            # print one line with id, title, category, severity, status and date
            print(f"{row[0]:<4} {row[1]:<45} {row[2]:<25} {row[3]:<8} {row[4]:<11} {row[5]:<11}")
            # print the description on its own line, then an empty line
            print(f"     {row[6]}\n")

# close the connection to the database
conn.close()