import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from pergunta import Pergunta
import app
import partida
import janela
from TelaConfirmarResposta import TelaConfirmarResposta
from random import randint, choice

LETRAS = ('A', 'B', 'C', 'D', 'E')

class TelaPartida(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0, pergunta : Pergunta = None, numero_pergunta_atual=1, dificuldade=0, pontuacao=0, ajuda=None):
        self.pergunta = pergunta

        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        self.imagem_fundo = tk.PhotoImage(file='images/imagemfundo0.png')
        raw_alt = Image.open('images/Alternativa.png').resize((330, 62), Image.LANCZOS)
        self.imagem_alt = ImageTk.PhotoImage(raw_alt) 

        if ajuda != partida.Ajuda.DUAS_OPCOES:
            self.create_image(0, 0, image=self.imagem_fundo, anchor='nw', tags=('bg',))
            for i, (x, y) in enumerate([(380,280), (880,280), (380,380), (880,380), (630,480)]):
                btn_tag = 'btn_pergunta_' + str(i)
                self.create_image(x, y, image=self.imagem_alt, anchor='n', tags=(btn_tag))
                self.tag_bind(btn_tag, '<Button-1>', lambda event, resposta=i: self.responder_pergunta(event, resposta))
                
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
                    text=LETRAS[i] + ") " + txt,
                    font=("Californian FB", 13, "bold"),
                    tags=(btn_tag))
                self.tag_bind(btn_tag, '<Button-1>', lambda event, resposta=i: self.responder_pergunta(event, resposta))

        else:
            opcoes = list(self.pergunta.alternativas)
            opcoes.pop(self.pergunta.resposta_correta)
            opcao_errada_disponivel = choice(opcoes)

            self.create_image(0, 0, image=self.imagem_fundo, anchor='nw', tags=('bg',))
            for i, (x, y) in enumerate([(380,280), (880,280), (380,380), (880,380), (630,480)]):
                if i == self.pergunta.resposta_correta or self.pergunta.alternativas[i] == opcao_errada_disponivel:
                    btn_tag = 'btn_pergunta_' + str(i)
                    self.create_image(x, y, image=self.imagem_alt, anchor='n', tags=(btn_tag))
                    self.tag_bind(btn_tag, '<Button-1>', lambda event, resposta=i: self.responder_pergunta(event, resposta))

            alternativas = [
                (380,310, self.pergunta.alternativas[0]),
                (880,310, self.pergunta.alternativas[1]),
                (380,410, self.pergunta.alternativas[2]),
                (880,410, self.pergunta.alternativas[3]),
                (630,510, self.pergunta.alternativas[4])
            ]

            for i, (x, y, txt) in enumerate(alternativas):
                if i == self.pergunta.resposta_correta or self.pergunta.alternativas[i] == opcao_errada_disponivel:
                    btn_tag = 'btn_pergunta_' + str(i)
                    self.create_text(x, y,
                        text=LETRAS[i] + ") " + txt,
                        font=("Californian FB", 13, "bold"),
                        tags=(btn_tag))
                    self.tag_bind(btn_tag, '<Button-1>', lambda event, resposta=i: self.responder_pergunta(event, resposta))

        match dificuldade:
            case 0:
                self.create_text(1250, 30,
                    text="FÁCIL",
                    font=("IM FELL ENGLISH SC", 18, "bold"),
                    fill="green",
                    anchor='ne')
            case 1:
                self.create_text(1250, 30,
                    text="MÉDIA",
                    font=("IM FELL ENGLISH SC", 18, "bold"),
                    fill="yellow",
                    anchor='ne')
            case 2:
                self.create_text(1250, 30,
                    text="DIFÍCIL",
                    font=("IM FELL ENGLISH SC", 18, "bold"),
                    fill="red",
                    anchor='ne')
            case 3:
                self.create_text(1250, 30,
                    text="PERGUNTA DO MILHÃO",
                    font=("IM FELL ENGLISH SC", 18, "bold"),
                    fill="purple",
                    anchor='ne')
        
        self.create_text(width/2, 190,
            text=self.pergunta.enunciado,
            font=("Californian FB", 32, "bold"),
            fill="darkred",
            anchor='center',
            width=1000
        )
        
        self.create_text(50, 30,
            text="PERGUNTA " + str(numero_pergunta_atual),
            font=("Californian FB", 22, "bold"),
            fill="darkred",
            anchor='nw')
        
        self.create_text(50, 650,
            text="PRÊMIO: " + str(pontuacao),
            font=("Californian FB", 22, "bold"),
            fill="black",
            anchor='nw')

        btn_tag = 'btn_desistir'
        self.create_image(1100, 660,
            image=self.imagem_alt,
            anchor='center',
            tags=(btn_tag,))
        self.create_text(1100, 660,
            text="DESISTIR",
            font=("Californian FB", 18, "bold"),
            fill="darkred",
            anchor='center',
            tags=(btn_tag,))
        self.tag_bind(btn_tag, '<Button-1>', self.desistir)

        if ajuda == None:
            btn_tag = 'btn_ajuda'
            self.create_image(630, 620,
                image=self.imagem_alt,
                anchor='center',
                tags=(btn_tag,)
            )
            self.create_text(630, 620,
                text="PEDIR AJUDA",
                font=("Californian FB", 18, "bold"),
                fill="black",
                anchor='center',
                tags=(btn_tag,)
            )
            self.tag_bind(btn_tag, '<Button-1>', self._on_utilizar_ajuda)
        elif ajuda == partida.Ajuda.DICA:
            self.create_text(630, 620,
                text="DICA: " + pergunta.dica,
                font=("Californian FB", 14, "bold"),
                fill="black",
                anchor='center',
                width=600
            )
        elif ajuda == partida.Ajuda.PLATEIA:
            self.create_text(630, 620,
                text="PLATEIA:",
                font=("Californian FB", 14, "bold"),
                fill="black",
                anchor='center',
                width=600
            )
            porcentagens = self.gerar_porcentagens_plateia()
            text_plateia = ""
            for i, porcentagem in enumerate(porcentagens):
                text_plateia += LETRAS[i] + ") " + str(porcentagem) + "% "
            self.create_text(630, 650,
                text=text_plateia,
                font=("Californian FB", 14, "bold"),
                fill="black",
                anchor='center',
                width=600
            )

    def gerar_porcentagens_plateia(self):
        porcentagens = [0, 0, 0, 0, 0]
        porcentagens[self.pergunta.resposta_correta] = randint(40, 100)
        for i in range(len(porcentagens)):
            if i == self.pergunta.resposta_correta:
                continue
            porcentagens[i] = randint(0, 100 - sum(porcentagens))
        return porcentagens

    def get_ajudas_disponiveis(self):
        return app.app.partida.ajudas_disponiveis

    def _on_utilizar_ajuda(self, event):
        if len(app.app.partida.ajudas_disponiveis) < 1:
            self.create_text(630, 700,
                text="Você não possui mais ajudas disponíveis.",
                font=("Californian FB", 12, "bold"),
                fill="red",
                anchor='center',
            )
        app.app.partida.exibir_tela_ajuda()

    def responder_pergunta(self, event, resposta):
        janela.janela.mudar_tela(lambda master: TelaConfirmarResposta(
            master=master,
            resposta=self.pergunta.alternativas[resposta],
            correta=(resposta == self.pergunta.resposta_correta)
        ))

    def desistir(self, event):
        app.app.partida.desistir()
