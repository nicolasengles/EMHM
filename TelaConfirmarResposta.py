import tkinter as tk
from PIL import Image, ImageTk
import app

class TelaConfirmarResposta(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0, resposta="", correta=False):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        self.correta = correta

        img = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img)
        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt)

        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)
        self.create_text(640, 100,
            text="TEM CERTEZA?",
            font=("Californian FB", 48, "bold"),
            fill="darkred",
            anchor='n'
        )
        
        self.create_text(640, 200,
            text="Sua resposta final é: " + resposta,
            font=("Californian FB", 30, "bold"),
            fill="black",
            anchor='n'
        )

        btn_tag = 'btn_sim'
        self.create_image(640, 300,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_tag,)
        )
        self.create_text(640, 315,
            text="SIM",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )
        self.tag_bind(btn_tag, '<Button-1>', self.confirmar)

        btn_tag = 'btn_nao'
        self.create_image(640, 400,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_tag,)
        )
        self.create_text(640, 415,
            text="NAO",
            font=("Californian FB", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )
        self.tag_bind(btn_tag, '<Button-1>', self.voltar)

    def confirmar(self, event):
        if self.correta:
            app.app.partida.acerto()

    def voltar(self, event):
        app.app.partida.exibir_tela_partida()
