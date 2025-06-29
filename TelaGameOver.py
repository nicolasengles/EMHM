import tkinter as tk
from PIL import Image, ImageTk
import janela

class TelaGameOver(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0, pontuacao=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        img = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img)
        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt)

        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)
        self.create_text(640, 160,
            text="GAME OVER",
            font=("Sylfaen", 48, "bold"),
            fill="darkred",
            anchor='n'
        )
        
        self.create_text(640, 265,
            text="PONTUAÇÃO FINAL: R$" + str(pontuacao),
            font=("Sylfaen", 30, "bold"),
            fill="black",
            anchor='n'
        )

        btn_tag = 'btn_reiniciar'
        self.create_image(640, 365,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_tag,)
        )
        self.create_text(640, 380,
            text="REINICIAR JOGO",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )
        self.tag_bind(btn_tag, '<Button-1>', self.reiniciar)

        btn_tag = 'btn_voltar'
        self.create_image(640, 465,
            image=self.imagem_alt,
            anchor='n',
            tags=(btn_tag,)
        )
        self.create_text(640, 480,
            text="VOLTAR AO MENU",
            font=("Sylfaen", 20, "bold"),
            fill="black",
            anchor='n',
            tags=(btn_tag,)
        )
        self.tag_bind(btn_tag, '<Button-1>', self.voltar)

    def reiniciar(self, event):
        from TelaIniciarPartida import TelaIniciarPartida
        janela.janela.mudar_tela(TelaIniciarPartida)

    def voltar(self, event):
        from TelaMenuPrincipal import TelaMenuPrincipal
        janela.janela.mudar_tela(TelaMenuPrincipal)
