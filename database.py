# database.py

import sqlite3

class Database:
    def __init__(self, db_name="hotel_management.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Table des clients
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                email TEXT UNIQUE,
                telephone TEXT
            )
        """)

        # Table des réservations
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                room_number INTEGER,
                check_in_date TEXT,
                check_out_date TEXT,
                tarif REAL,  -- Utilisation de REAL pour représenter un décimal
                FOREIGN KEY(client_id) REFERENCES clients(id),
                FOREIGN KEY(room_number) REFERENCES chambres(id)
            )
        """)

        # Table des factures
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS factures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                reservation_id INTEGER,
                tarif REAL,  -- Utilisation de REAL pour représenter un décimal
                paye INTEGER CHECK(paye IN (0, 1)),  -- Booléen : 0 pour non, 1 pour oui
                FOREIGN KEY(client_id) REFERENCES clients(id),
                FOREIGN KEY(reservation_id) REFERENCES reservations(id)
            )
        """)

        # Table des chambres
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS chambres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER UNIQUE,
                occupee INTEGER CHECK(occupee IN (0, 1))  -- Booléen : 0 pour non, 1 pour oui
            )
        """)

        self.connection.commit()

    def close(self):
        self.connection.close()

# Exemple d'utilisation
if __name__ == "__main__":
    db = Database()
    db.close()
