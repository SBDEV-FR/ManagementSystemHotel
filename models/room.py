# models/room.py
import sqlite3

class Room:
    def __init__(self, id, numero, occupee, type):
        self.id = id
        self.numero = numero
        self.occupee = occupee
        self.type = type

    def __str__(self):
        status = "Occupée" if self.occupee else "Libre"
        return f"Chambre {self.numero} ({self.type}) - {status}"

    @property
    def status(self):
        return "Occupée" if self.occupee else "Libre"
    
    def fetch_rooms_from_database(self):
        rooms = []
        try:
            conn = sqlite3.connect('hotel_management.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, numero, occupee, type FROM chambres")
            for row in cursor.fetchall():
                rooms.append(Room(*row))
            conn.close()
        except sqlite3.Error as e:
            print(f"Erreur de base de données : {e}")
        return rooms





