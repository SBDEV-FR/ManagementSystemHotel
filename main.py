# main.py

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

from pages.home_page import HomePage
from pages.reservation_page import ReservationPage
from pages.rooms_page import RoomsPage
from pages.clients_page import ClientsPage
from pages.billing_page import BillingPage
from pages.settings_page import SettingsPage
from database import Database

class HotelApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Gestion d'Hôtel")
        self.geometry("800x600")
        self.configure(bg="#192734")

        # Initialize the database
        self.db = Database()

        # Define fonts here
        self.title_font = tkFont.Font(family="Verdana", size=24, weight="bold")
        self.normal_font = tkFont.Font(family="Verdana", size=12)

        # Create widgets after fonts are defined
        self.create_widgets()

    def create_widgets(self):
        # Frame principale
        self.main_frame = tk.Frame(self, bg="#192734")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Menu (à droite)
        menu_frame = tk.Frame(self.main_frame, bg="#2C3A47", width=200)
        menu_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Boutons du menu
        menu_buttons = [
            ("Accueil", self.show_home),
            ("Réservations", self.show_reservations),
            ("Chambres", self.show_rooms),
            ("Clients", self.show_clients),
            ("Facturation", self.show_billing),
            ("Paramètres", self.show_settings)
        ]

        for button_text, command in menu_buttons:
            button = tk.Button(menu_frame, text=button_text, bg="#3C3C50", fg="white", 
                               activebackground="#2C3A47", activeforeground="white", 
                               relief=tk.FLAT, padx=10, pady=5, command=command)
            button.pack(fill=tk.X, padx=5, pady=2)

        # Créer le conteneur pour les pages
        self.page_container = tk.Frame(self.main_frame, bg="#192734")
        self.page_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Créer les pages
        self.frames = {}
        for F in (HomePage, ReservationPage, RoomsPage, ClientsPage, BillingPage, SettingsPage):
            page_name = F.__name__
            frame = F(parent=self.page_container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    # Méthodes pour afficher chaque page
    def show_home(self):
        self.show_frame("HomePage")

    def show_reservations(self):
        self.show_frame("ReservationPage")

    def show_rooms(self):
        self.show_frame("RoomsPage")

    def show_clients(self):
        self.show_frame("ClientsPage")

    def show_billing(self):
        self.show_frame("BillingPage")

    def show_settings(self):
        self.show_frame("SettingsPage")

    def on_closing(self):
        self.db.close()
        self.destroy()

if __name__ == "__main__":
    app = HotelApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
