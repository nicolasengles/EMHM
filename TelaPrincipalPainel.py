import tkinter as tk
from PIL import Image, ImageTk
import app

class TelaPrincipalPainel(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        raw_fundo = Image.open(r'images\black-solid-background-2920-x-1642-jk98dr7udfcq3hqj.jpg')\
            .resize((width, height), Image.LANCZOS)
        self.imagem_fundo = ImageTk.PhotoImage(raw_fundo)
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

        self.create_text(640, 100,
            text="PAINEL DO PROFESSOR",
            font=("Arial", 24, "bold"),
            fill="white",
            anchor='n'
        )

        self.create_text(640, 150,
            text="Bem-vindo(a), " + app.app.usuario.nome.split()[0] + "!",
            font=("Arial", 18),
            fill="white",
            anchor='n'
        )

        btn_perguntas_tag = 'btn_perguntas'
        self.create_text(640, 300,
            text="GERENCIAR PERGUNTAS",
            font=("Arial", 18, "bold"),
            fill="light green",
            anchor='n',
            tags=(btn_perguntas_tag,)
        )

        btn_turmas_tag = 'btn_turmas'
        self.create_text(640, 400,
            text="GERENCIAR TURMAS",
            font=("Arial", 18, "bold"),
            fill="white",
            anchor='n',
            tags=(btn_turmas_tag,)
        )
