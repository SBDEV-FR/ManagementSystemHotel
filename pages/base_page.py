# pages/base_page.py

import tkinter as tk

class BasePage(tk.Frame):
    def __init__(self, parent, controller, title, presentation_text):
        super().__init__(parent, bg="#192734")
        self.controller = controller

        # Cadre pour le titre
        title_frame = tk.Frame(self, bg="#2C3A47", pady=10)
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text=title, font=controller.title_font, bg="#2C3A47", fg="white")
        title_label.pack()

        # Cadre pour la présentation
        presentation_frame = tk.Frame(self, bg="#3C3C50", pady=20, padx=20)
        presentation_frame.pack(fill=tk.X, pady=10)

        presentation_label = tk.Label(presentation_frame, text=presentation_text, 
                                      font=controller.normal_font, bg="#3C3C50", fg="white", 
                                      wraplength=500, justify="left")
        presentation_label.pack()

        # Cadre pour le contenu futur
        self.content_frame = tk.Frame(self, bg="#192734", pady=20, padx=20)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
