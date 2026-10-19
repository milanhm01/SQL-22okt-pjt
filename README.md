# CyberShield

CyberShield er et konsolprogram i Python, der registrerer og håndterer cybersikkerhedshændelser i en SQLite-database.
Projektet er en obligatorisk caseopgave i Programmering (PB Cyber, Sommer 2026): *Database og inputvalidering med Python*.

## Gruppen

- Derar
- Milan
- Saad

## Teknologier

- Python 3
- SQLite (via Pythons indbyggede `sqlite3`-bibliotek)
- Git og GitHub (feature branches og pull requests)

Der bruges ingen eksterne biblioteker.

## Datamodel

Databasen `cybershield.db` har én tabel, `incidents`:

| Felt | Datatype | Beskrivelse |
|---|---|---|
| `incident_id` | INTEGER, primærnøgle | Unikt ID, som SQLite tildeler automatisk |
| `title` | TEXT | Hændelsens titel |
| `category` | TEXT | Phishing, Malware, Mistænkeligt loginforsøg, Uautoriseret adgang eller Databrud |
| `severity` | TEXT | Lav, Mellem, Høj eller Kritisk |
| `status` | TEXT | Åben, Undersøges eller Lukket |
| `reported_date` | TEXT | Dato for registrering, format `YYYY-MM-DD` |
| `description` | TEXT | Beskrivelse af hændelsen |

## Filer

Scripts er nummereret efter de seks krav i opgaveformuleringen:

| Fil | Formål | SQL |
|---|---|---|
| `1_create_database.py` | Opretter databasen og tabellen | `CREATE TABLE` |
| `2_bulk_insert.py` | Indsætter 100 kunstige hændelser, eller importerer hændelser fra en CSV-fil | `INSERT INTO` |
| `3_delete_incidents.py` | Tømmer tabellen (efter bekræftelse) | `DELETE FROM` |
| `4_show_incidents.py` | Viser alle hændelser pænt i konsollen | `SELECT` |
| `5_filter_incidents.py` | Filtrerer efter alvorlighed, status eller kategori | `SELECT ... WHERE` |
| `6_add_incident.py` | Registrerer én ny hændelse med inputvalidering | `INSERT INTO` |
| `main.py` | Hovedmenu, der samler alle scripts | |
| `data/bulk_ai_gen_data.py` | 100 hændelser genereret af en LLM | |
| `data/example_incidents.csv` | Eksempel på en CSV-fil, der kan importeres | |
| `cybershield.db` | SQLite-databasen | |

## Sådan kører du programmet

Programmet kræver Python 3. Kør det fra projektmappen:

```bash
python main.py
```

Menuen:

```
1. Opret database
2. Indsæt hændelser (testdata eller CSV-fil)
3. Slet alle hændelser
4. Vis alle hændelser
5. Filtrér hændelser
6. Registrér ny hændelse
0. Afslut programmet
```

Første gang: vælg **1** og derefter **2**. Hvert script kan også køres alene, fx `python 4_show_incidents.py`.

Bemærk: vælger man **2** flere gange, indsættes de 100 hændelser igen. Vælg **3** for at tømme tabellen først.

## Inputvalidering

- Titel og beskrivelse må ikke være tomme (mellemrum alene tæller som tomt).
- Kategori, alvorlighed og status skal være en af de tilladte værdier. Der rettes automatisk for store og små bogstaver.
- Dato skal være en rigtig dato i formatet `YYYY-MM-DD` (fx afvises `2026-02-30`).
- Ugyldige indtastninger giver en fejlbesked, og brugeren får lov at prøve igen.
- Brugerens tekst sættes ind i SQL via `?`-parametre, aldrig direkte i SQL-teksten.
- Sletning kræver, at brugeren skriver `ja`.

## Samarbejde

Hvert script er udviklet i sin egen branch og lagt ind i `main` via en pull request.
