# import subprocess so we can run the other scripts from this menu
import subprocess
# import sys so we can use the same python that runs this program
import sys
# import os so we can find the folder this file is in
import os

# find the folder where main.py is, so the scripts find the database file
mappe = os.path.dirname(os.path.abspath(__file__))

# dictionary that connects each menu number to a script file
scripts = {
    "1": "1_create_database.py",
    "2": "2_bulk_insert.py",
    "3": "3_delete_incidents.py",
    "4": "4_show_incidents.py",
    "5": "5_filter_incidents.py",
    "6": "6_add_incident.py",
}


# show the main menu
def show_menu():
    # print the menu title
    print("\n=== CyberShield ===")
    # print option 1
    print("1. Opret database")
    # print option 2
    print("2. Indsæt hændelser (testdata eller CSV-fil)")
    # print option 3
    print("3. Slet alle hændelser")
    # print option 4
    print("4. Vis alle hændelser")
    # print option 5
    print("5. Filtrér hændelser")
    # print option 6
    print("6. Registrér ny hændelse")
    # print option 0
    print("0. Afslut programmet")


# run the menu until the user quits
def main():
    # keep showing the menu until the user chooses 0
    while True:
        # print the menu
        show_menu()
        # ask the user to choose an option and remove extra spaces
        valg = input("Vælg en mulighed: ").strip()

        # check if the user wants to quit
        if valg == "0":
            # say goodbye to the user
            print("Farvel!")
            # leave the loop
            break
        # check if the choice is one of the scripts
        elif valg in scripts:
            # run the chosen script and wait until it is done
            subprocess.run([sys.executable, scripts[valg]], cwd=mappe)
        # runs if the user typed anything else
        else:
            # tell the user the choice was not valid
            print("Ugyldigt valg, prøv igen")


# start the program
main()
