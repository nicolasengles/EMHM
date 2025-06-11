import tkinter as tk
from PIL import Image, ImageTk
import app

LETRAS = ('A', 'B', 'C', 'D', 'E')

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
        self.create_text(640, 130,
            text="TEM CERTEZA?",
            font=("Sylfaen", 48, "bold"),
            fill="darkred",
            anchor='center'
        )
        
        self.create_text(640, 275,
            text="Sua resposta final é:\n" + resposta,
            font=("Sylfaen", 30, "bold"),
            justify="center",
            fill="black",
            anchor='center'
        )

        btn_tag = 'btn_sim'
        self.create_image(640, 375,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_tag,)
        )
        self.create_text(640, 390,
            text="SIM",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )
        self.tag_bind(btn_tag, '<Button-1>', self.confirmar)

        btn_tag = 'btn_nao'
        self.create_image(640, 475,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_tag,)
        )
        self.create_text(640, 490,
            text="NAO",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )
        self.tag_bind(btn_tag, '<Button-1>', self.voltar)

    def confirmar(self, event):
        if self.correta:
            app.app.partida.acerto()
            return
        app.app.partida.erro()

    def voltar(self, event):
        app.app.partida.exibir_tela_partida()
