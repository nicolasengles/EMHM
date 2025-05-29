import enum
from random import random

class Ajuda(enum):
    DICA = 0
    DUAS_OPCOES = 1
    PLATEIA = 2

class Partida:
    def __init__(self, materia):
        materia = materia
        rodada = 0
        pontuacao = 0
        ajudas_disponiveis = [Ajuda.DICA, Ajuda.DUAS_OPCOES, Ajuda.PLATEIA]
        numero_pergunta_atual = 1
        perguntas = [] #buscar_perguntas(materia, rodada)
        pergunta_atual = None
        perguntas_previas = []
    
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
        #self.perguntas = buscar_perguntas(materia, rodada)