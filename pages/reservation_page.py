import tkinter as tk
from pages.base_page import BasePage

class ReservationPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Réservations", 
                         "Gérez les réservations de l'hôtel ici. "
                         "Vous pouvez ajouter, modifier ou supprimer des réservations.")

