import tkinter as tk
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
                    font=("Sylfaen", 14, "bold"),
                    justify="center",
                    width=300,
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
                        font=("Sylfaen", 14, "bold"),
                        justify="center",
                        width=300,
                        tags=(btn_tag))
                    self.tag_bind(btn_tag, '<Button-1>', lambda event, resposta=i: self.responder_pergunta(event, resposta))

        match dificuldade:
            case 0:
                self.create_text(1250, 30,
                    text="FÁCIL",
                    font=("Sylfaen", 22, "bold"),
                    fill="green",
                    anchor='ne')
            case 1:
                self.create_text(1250, 30,
                    text="MÉDIA",
                    font=("Sylfaen", 22, "bold"),
                    fill="yellow",
                    anchor='ne')
            case 2:
                self.create_text(1250, 30,
                    text="DIFÍCIL",
                    font=("Sylfaen", 22, "bold"),
                    fill="red",
                    anchor='ne')
            case 3:
                self.create_text(1250, 30,
                    text="PERGUNTA DO MILHÃO",
                    font=("Sylfaen", 22, "bold"),
                    fill="purple",
                    anchor='ne')
        
        self.create_text(width/2, 180,
            text=self.pergunta.enunciado,
            font=("Sylfaen", 32, "bold"),
            fill="darkred",
            justify='center',
            width=1000
        )
        
        self.create_text(50, 30,
            text="PERGUNTA " + str(numero_pergunta_atual),
            font=("Sylfaen", 22, "bold"),
            fill="darkred",
            anchor='nw')
        
        self.create_text(50, 650,
            text="PRÊMIO: " + str(pontuacao),
            font=("Sylfaen", 22, "bold"),
            fill="black",
            anchor='nw')

        btn_tag = 'btn_desistir'
        self.create_image(1100, 660,
            image=self.imagem_alt,
            anchor='center',
            tags=(btn_tag,))
        self.create_text(1100, 660,
            text="DESISTIR",
            font=("Sylfaen", 18, "bold"),
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
                font=("Sylfaen", 18, "bold"),
                fill="black",
                anchor='center',
                tags=(btn_tag,)
            )
            self.tag_bind(btn_tag, '<Button-1>', self._on_utilizar_ajuda)
        elif ajuda == partida.Ajuda.DICA:
            self.create_text(630, 620,
                text="DICA: " + pergunta.dica,
                font=("Sylfaen", 14, "bold"),
                fill="black",
                anchor='center',
                width=600
            )
        elif ajuda == partida.Ajuda.PLATEIA:
            self.create_text(630, 620,
                text="PLATEIA:",
                font=("Sylfaen", 14, "bold"),
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
                font=("Sylfaen", 14, "bold"),
                fill="black",
                anchor='center',
                width=600
            )
        
        btn_mute_tag = 'btn_mute'
        self.create_text(120, 540,
            text="DESATIVAR MÚSICA",
            font=("Sylfaen", 15, "bold"),
            fill="brown",
            anchor='n',
            width=200,
            tags=(btn_mute_tag,),
            justify='center'
        )
        # binding corrigido:
        self.tag_bind(
            btn_mute_tag, '<Button-1>',
            lambda e: janela.janela.toggle_mute(self, btn_mute_tag)
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
        app.app.partida.exibir_tela_ajuda()

    def responder_pergunta(self, event, resposta):
        janela.janela.mudar_tela(lambda master: TelaConfirmarResposta(
            master=master,
            resposta=LETRAS[self.pergunta.resposta_correta] + ") " + self.pergunta.alternativas[resposta],
            correta=(resposta == self.pergunta.resposta_correta)
        ))

    def desistir(self, event):
        app.app.partida.desistir()
