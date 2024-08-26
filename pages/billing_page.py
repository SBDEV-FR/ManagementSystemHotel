
import tkinter as tk
from pages.base_page import BasePage

class BillingPage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller, "Facturation", 
                         "Gérez la facturation des séjours. "
                         "Vous pouvez créer des factures et suivre les paiements.")

