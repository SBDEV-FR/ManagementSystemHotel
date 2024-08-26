import tkinter as tk
from tkinter import ttk
from pages.base_page import BasePage
from models.room import Room
from tkinter import messagebox
import sqlite3

class RoomsPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Chambres", 
                         "Consultez et gérez les chambres de l'hôtel. "
                         "Vous pouvez voir l'état des chambres et leurs caractéristiques.")
        
        self.create_room_table()

    def create_room_table(self):
        # Create a frame for the table
        table_frame = ttk.Frame(self)
        table_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Create the Treeview widget
        self.room_table = ttk.Treeview(table_frame, columns=("id", "numero", "type", "status"), show="headings")

        # Define column headings
        self.room_table.heading("id", text="ID")
        self.room_table.heading("numero", text="Numéro")
        self.room_table.heading("type", text="Type")
        self.room_table.heading("status", text="Statut")

        # Define column widths
        self.room_table.column("id", width=50)
        self.room_table.column("numero", width=100)
        self.room_table.column("type", width=150)
        self.room_table.column("status", width=100)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.room_table.yview)
        self.room_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.room_table.pack(expand=True, fill=tk.BOTH)

        # Add a refresh button
        refresh_button = ttk.Button(self, text="Rafraîchir", command=self.refresh_table)
        refresh_button.pack(pady=10)

        # Initial population of the table
        self.refresh_table()


    def refresh_table(self):
        # Clear the existing data
        for item in self.room_table.get_children():
            self.room_table.delete(item)

        # Fetch rooms from the database
        rooms = self.fetch_rooms_from_database()

        print(f"Nombre de chambres récupérées : {len(rooms)}")  # Débogage

        if not rooms:
            messagebox.showerror("Erreur", "Impossible de récupérer les données des chambres.")
            return

        # Insert the rooms into the table
        for room in rooms:
            print(f"Insertion de la chambre : {room}")  # Débogage
            self.room_table.insert("", tk.END, values=(room.id, room.numero, room.type, room.status))
    
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
