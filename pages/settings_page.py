 
import tkinter as tk
from pages.base_page import BasePage

class SettingsPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Paramètres", 
                         "Configurez les paramètres de l'application. "
                         "Vous pouvez ajuster les options selon vos besoins.")
