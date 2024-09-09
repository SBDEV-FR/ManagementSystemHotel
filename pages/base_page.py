import tkinter as tk

class BasePage(tk.Frame):
    def __init__(self, parent, controller, title, presentation_text):
        super().__init__(parent, bg="#572649")  # Couleur de fond de la page
        self.controller = controller

        # Cadre pour le titre
        title_frame = tk.Frame(self, bg="#79305a", pady=10)
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(title_frame, text=title, font=controller.title_font, bg="#79305a", fg="white")
        title_label.pack()

        # Cadre pour la présentation
        presentation_frame = tk.Frame(self, bg="#bf6b99", pady=20, padx=20)
        presentation_frame.pack(fill=tk.X, pady=10)

        presentation_label = tk.Label(presentation_frame, text=presentation_text, 
                                      font=controller.normal_font, bg="#bf6b99", fg="white", 
                                      wraplength=500, justify="left")
        presentation_label.pack()

        # Cadre pour le contenu futur
        self.content_frame = tk.Frame(self, bg="#572649", pady=20, padx=20)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
