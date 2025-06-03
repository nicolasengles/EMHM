import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
# import sys
# from TelaGameOver import TelaGameOver
from pergunta import Pergunta
# import janela
import app
import functools

LETRAS = ('A', 'B', 'C', 'D', 'E')

class TelaPartida(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0, pergunta : Pergunta = None, numero_pergunta_atual=1, dificuldade=0):
        self.pergunta = pergunta

        # inicializa e empacota
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # 1) carrega e mantém referências das imagens
        self.imagem_fundo = tk.PhotoImage(file='images/imagemfundo0.png')
        # raw_nivel = Image.open('images/NivelDeDificuldade.png').resize((300, 20), Image.LANCZOS)
        # self.imagem_nivel = ImageTk.PhotoImage(raw_nivel)
        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt)

        # 2) desenha o fundo e camadas de imagens
        self.create_image(0, 0, image=self.imagem_fundo, anchor='nw', tags=('bg',))
        # self.create_image(1000, 36, image=self.imagem_nivel, anchor='n')
        for i, (x, y) in enumerate([(380,280), (880,280), (380,380), (880,380), (630,480)]):
            btn_tag = 'btn_pergunta_' + str(i)
            self.create_image(x, y, image=self.imagem_alt, anchor='n', tags=(btn_tag))
            self.tag_bind(btn_tag, '<Button-1>', functools.partial(self._on_responder_pergunta, resposta=i))

        # 3) desenha textos fixos
        match dificuldade:
            case 0:
                self.create_text(1250, 32,
                    text="FÁCIL",
                    font=("IM FELL ENGLISH SC", 18, "bold"),
                    fill="green",
                    anchor='ne')
            case 1:
                self.create_text(1250, 32,
                    text="MÉDIA",
                    font=("IM FELL ENGLISH SC", 18, "bold"),
                    fill="yellow",
                    anchor='ne')
            case 2:
                self.create_text(1250, 32,
                    text="DIFÍCIL",
                    font=("IM FELL ENGLISH SC", 18, "bold"),
                    fill="orange",
                    anchor='ne')
            case 3:
                self.create_text(1250, 32,
                    text="PERGUNTA DO MILHÃO",
                    font=("IM FELL ENGLISH SC", 18, "bold"),
                    fill="red",
                    anchor='ne')
        
        self.create_text(width/2, 190,
            text=self.pergunta.enunciado,
            font=("Californian FB", 32, "bold"),
            fill="darkred",
            anchor='center',
            width=1000
            )
        
        self.create_text(50, 35,
            text="PERGUNTA " + str(numero_pergunta_atual),
            font=("Californian FB", 22, "bold"),
            fill="darkred",
            anchor='nw')

        # 4) desenha textos das alternativas
        alternativas = [
            (380,310, self.pergunta.alternativas[0]),
            (880,310, self.pergunta.alternativas[1]),
            (380,410, self.pergunta.alternativas[2]),
            (880,410, self.pergunta.alternativas[3]),
            (630,510, self.pergunta.alternativas[4])
        ]

        for i, (x, y, txt) in enumerate(alternativas):
            btn_tag = 'btn_pergunta_' + str(i)
            self.create_text(x, y,
                text=txt,
                font=("Californian FB", 13, "bold"),
                tags=(btn_tag))
            self.tag_bind(btn_tag, '<Button-1>', functools.partial(self._on_responder_pergunta, resposta=i))

        # 5) cria o “botão” DESISTIR usando tag para imagem+texto
        btn_tag = 'btn_desistir'
        self.create_image(630, 660,
            image=self.imagem_alt,
            anchor='center',
            tags=(btn_tag,))
        self.create_text(630, 660,
            text="DESISTIR",
            font=("Californian FB", 18, "bold"),
            fill="darkred",
            anchor='center',
            tags=(btn_tag,))

        # 6) vincula clique na tag para chamar handler
        self.tag_bind(btn_tag, '<Button-1>', self._on_desistir)

    def _on_responder_pergunta(self, event, resposta):
        res = messagebox.askquestion("Tem certeza?", "Você escolheu a opção:\n\""+ LETRAS[resposta] + ") " + self.pergunta.alternativas[resposta] + "\"\nDeseja confirmar?")
        if res == "yes":
            self.responder_pergunta(resposta=resposta)

    def responder_pergunta(self, resposta):
        if resposta == self.pergunta.resposta_correta:
            app.app.partida.proxima_pergunta()
            return
        # app.app.partida.finalizar_partida()

    def _on_desistir(self, event):
        self.desistir()

    def desistir(self):
        app.app.partida.desistir()
