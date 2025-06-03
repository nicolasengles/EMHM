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
        self.rodada = 0
        self.pontuacao = 0
        self.ajudas_disponiveis = [Ajuda.DICA, Ajuda.DUAS_OPCOES, Ajuda.PLATEIA]
        self.numero_pergunta_atual = 1
        self.perguntas = sgbd.buscar_perguntas(self.materia, self.rodada)
        self.pergunta_atual = None
        self.perguntas_previas = []
        janela.janela.mudar_tela(TelaPartida(master=janela.janela.janela, pergunta=self.perguntas[random.randint(0, len(self.perguntas) - 1)]))
    
    def proxima_pergunta(self):
        aux = self.perguntas[random(len[self.perguntas])]
        if aux not in self.perguntas:
            self.pergunta_atual = aux
            self.numero_pergunta_atual += 1
            return        
        self.proxima_pergunta()
    
    def proxima_rodada(self):
        self.rodada += 1
        self.perguntas = []
        self.perguntas = sgbd.buscar_perguntas(self.materia, self.rodada)

    def desistir(self):
        janela.janela.mudar_tela(TelaGameOver(janela.janela.janela))
        app.app.finalizar_partida()