# Football Club - Management System

This project enables the management of the **Feyenoord Rotterdam** football club through a command-line interface. The system allows managers and coaches to access and interact with player data, statistics, and manage club staff.

---

## Contents

- `main.py` – Main application entry point and menu logic for manager and coach roles  
- `Zaposleni.py` – Handles data related to players, coaches, and manager (loading, adding, editing, displaying)  
- `Statistika.py` – Calculates and formats football statistics (goals, assists, ratings, clean sheets)  
- `xgll.csv` – CSV file with Expected Goals (xG) data  
- Data files used by the system:  
  - `igraci.txt` – Players  
  - `treneri.txt` – Coaches  
  - `menadzer.txt` – Manager  
  - `golovi.txt` – Goals  
  - `asistencije.txt` – Assists  
  - `cleansheet.txt` – Clean sheets  
  - `ocene.txt` – Match ratings  
  - `statistika.txt` – Final player statistics  

---

## User Roles

The system allows login for the following user types:

- **Manager**
  - Full system access
  - Can add, update, and remove coaches
  - Can add new players

- **Coaches**
  - Can view players and statistics
  - Cannot modify staff or player data

---

## Features

### Shared Features (Manager and Coach):

1. Search player by username  
2. View all players  
3. View statistics for all players  
4. View statistics for a specific player  
5. View club information  
6. View xG graph (Expected Goals)  
7. View coach list (for manager) / manager info (for coaches)

### Manager-Only Features:

8. Add a new coach  
9. Update coach information  
10. Remove a coach  
11. Add a new player  

---

## Player Statistics

Player stats are calculated based on the last 10 matches:

- **Rating**: Average of last 10 ratings from `ocene.txt`  
- **Goals**: Total from `golovi.txt`  
- **Assists**: Total from `asistencije.txt`  
- **Clean sheets**: Total from `cleansheet.txt`

Results are saved to `statistika.txt`.

---

## xG Analysis

The Expected Goals (xG) chart is displayed using data from `xgll.csv`, with the help of the `matplotlib` library. It shows how both home and away teams accumulated xG throughout the match.

---

## Running the Application

Run the app using the following command:

```bash
python main.py
```

---

## Required Libraries

```bash
pip install pandas matplotlib prettytable
```

---

## File Structure
    .
    ├── main.py                         # Entry point – login menu and user interface logic
    ├── Zaposleni.py                    # Handles employees (players, coaches, manager) data
    ├── Statistika.py                   # Calculates player statistics (goals, assists, ratings, etc.)
    ├── xgll.csv                        # CSV file containing expected goals (xG) data
    ├── igraci.txt                      # List of all players with personal and position data
    ├── treneri.txt                     # List of coaches with training type and login data
    ├── menadzer.txt                    # Manager login credentials
    ├── golovi.txt                      # Number of goals per player over 10 matches
    ├── asistencije.txt                 # Number of assists per player over 10 matches
    ├── cleansheet.txt                  # Clean sheets per player over 10 matches
    ├── ocene.txt                       # Player ratings per match in over 10 matches
    ├── statistika.txt                  # Final calculated statistics (rating, goals, assists, clean sheets)
    └── README.md                       # This documentation file
    
