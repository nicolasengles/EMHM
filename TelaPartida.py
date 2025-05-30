import tkinter as tk
from PIL import Image, ImageTk

class TelaPartida(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master)
        
        # --- Load & resize images ---
        imagem_fundo         = tk.PhotoImage(file='images/imagemfundo0.png')
        arquivo_nivel_de_dificuldade = Image.open(r"images/NivelDeDificuldade.png").resize((120, 52), Image.LANCZOS)
        imagem_nivel_de_dificuldade = ImageTk.PhotoImage(arquivo_nivel_de_dificuldade)
    
        # --- Create canvas and draw background & title ---
        self.pack(fill="both", expand=True)
        self.create_image(0, 0, image= imagem_fundo, anchor=tk.NW)
        self.create_image(320, 100, image=ImageTk.PhotoImage(imagem_nivel_de_dificuldade), anchor='n')
        # --- Keep references to prevent GC ---
        master.fundo = imagem_fundo
        master.nivel = imagem_nivel_de_dificuldade