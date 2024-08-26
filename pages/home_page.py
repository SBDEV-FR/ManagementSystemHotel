 # pages/home_page.py

import tkinter as tk
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Accueil", 
                         "Bienvenue dans l'application de gestion d'hôtel. "
                         "Utilisez le menu à droite pour naviguer entre les différentes fonctionnalités.")
