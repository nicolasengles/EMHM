from enum import Enum
from random import random
import sgbd
import janela
from TelaPartida import TelaPartida
import random
from TelaGameOver import TelaGameOver
import app
from TelaAjuda import TelaAjuda

VALORES_PERGUNTAS = (1000, 10000, 100000, 445000)

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
            self.exibir_tela_partida()
            return        
        self.proxima_pergunta()

    def exibir_tela_partida(self):
        janela.janela.mudar_tela(lambda master: TelaPartida(
            master=master,
            pergunta=self.pergunta_atual,
            numero_pergunta_atual=self.numero_pergunta_atual,
            dificuldade=self.dificuldade,
            pontuacao=self.pontuacao
        ))
    
    def proxima_rodada(self):
        self.dificuldade += 1
        self.perguntas = sgbd.buscar_perguntas(self.materia, self.dificuldade)

    def exibir_tela_ajuda(self):
        janela.janela.mudar_tela(TelaAjuda)

    def acerto(self):
        self.pontuacao += VALORES_PERGUNTAS[self.dificuldade]
        self.proxima_pergunta()
    
    def erro(self):
        if self.dificuldade == 0:
            janela.janela.mudar_tela(lambda master: TelaGameOver(master=master, pontuacao=0))
            app.app.finalizar_partida(0)
            return
        
        janela.janela.mudar_tela(lambda master: TelaGameOver(master=master, pontuacao=VALORES_PERGUNTAS[self.dificuldade]))
        app.app.finalizar_partida(VALORES_PERGUNTAS[self.dificuldade])

    def desistir(self):
        janela.janela.mudar_tela(lambda master: TelaGameOver(master=master, pontuacao=self.pontuacao))
        app.app.finalizar_partida(self.pontuacao)

    def utilizar_ajuda(self, ajuda : Ajuda):
        self.ajudas_disponiveis.remove(ajuda)
        janela.janela.mudar_tela(lambda master: TelaPartida(
            master=master,
            pergunta=self.pergunta_atual,
            numero_pergunta_atual=self.numero_pergunta_atual,
            dificuldade=self.dificuldade,
            pontuacao=self.pontuacao,
            ajuda=ajuda
        ))
