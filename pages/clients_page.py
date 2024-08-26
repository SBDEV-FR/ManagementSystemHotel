 
import tkinter as tk
from pages.base_page import BasePage

class ClientsPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Clients", 
                         "Gérez les informations des clients. "
                         "Vous pouvez ajouter de nouveaux clients ou modifier les informations existantes.")

