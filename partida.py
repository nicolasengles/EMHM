from enum import Enum
from random import random
import sgbd
import janela
from TelaPartida import TelaPartida
import random
from TelaGameOver import TelaGameOver
import app

class Ajuda(Enum):
    DICA = 0
    DUAS_OPCOES = 1
    PLATEIA = 2

class Partida:
    def __init__(self, materia):
        self.materia = materia
        self.dificuldade = -1
        self.pontuacao = 0
        self.numero_pergunta_atual = 0
        self.ajudas_disponiveis = [Ajuda.DICA, Ajuda.DUAS_OPCOES, Ajuda.PLATEIA]
        self.perguntas = sgbd.buscar_perguntas(self.materia, self.dificuldade)
        self.pergunta_atual = None
        self.perguntas_previas = []

        self.proxima_pergunta()
    
    def proxima_pergunta(self):
        if self.numero_pergunta_atual % 5 == 0:
            self.proxima_rodada()
            self.perguntas_previas = []
        else:
            self.perguntas_previas.append(self.pergunta_atual)

        aux = self.perguntas[random.randint(0, len(self.perguntas) - 1)]
        if aux not in self.perguntas_previas:
            self.pergunta_atual = aux
            self.numero_pergunta_atual += 1
            janela.janela.mudar_tela(TelaPartida(master=janela.janela.janela, pergunta=self.pergunta_atual, numero_pergunta_atual=self.numero_pergunta_atual, dificuldade=self.dificuldade))
            return        
        self.proxima_pergunta()
    
    def proxima_rodada(self):
        self.dificuldade += 1
        self.perguntas = sgbd.buscar_perguntas(self.materia, self.dificuldade)

    def desistir(self):
        janela.janela.mudar_tela(TelaGameOver(janela.janela.janela))
        app.app.finalizar_partida()