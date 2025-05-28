import tkinter as tk
from PIL import Image, ImageTk

class TelaPartida(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master)
        
        # --- Load & resize images ---
        bg_img = tk.PhotoImage(file='images/imagemfundo0.png')

        # --- Create canvas and draw background & title ---
        self.pack(fill="both", expand=True)

        # --- Keep references to prevent GC ---
        master.bg_img = bg_img
