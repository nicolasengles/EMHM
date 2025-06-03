import tkinter as tk
from PIL import Image, ImageTk

class TelaManterPerguntas(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master)

        # Carrega e desenha o fundo
        raw_fundo = Image.open(r'images\black-solid-background-2920-x-1642-jk98dr7udfcq3hqj.jpg')\
            .resize((width, height), Image.LANCZOS)
        self.imagem_fundo = ImageTk.PhotoImage(raw_fundo)
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)

        # Título do painel
        self.create_text(640, 100,
            text="Selecionar Entre as opções de Manutenção",
            font=("Arial", 24, "bold"),
            fill="white",
            anchor='n'
        )
        # Instruções da tela
        self.create_text(640, 200,
            text="Selecione a pergunta que deseja editar ou excluir.",
            font=("Arial", 16),
            fill="white",
            anchor='n',
        )