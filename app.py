from aluno import Aluno
from professor import Professor
from turma import Turma
from partida import Partida
import sgbd

class App():
    def __init__(self):
        self.usuario = None
        self.partida = None
        self.turmas = []
        self.perguntas = []

    def get_turma(self, nome : str):
        try:
            return [turma for turma in self.turmas if turma.nome == nome][0]
        except IndexError:
            return None
        
    def iniciar_partida(self, materia):
        self.partida = Partida(materia)

    def finalizar_partida(self, pontuacao : int):
        self.partida = None
        if pontuacao > 0:
            sgbd.incrementar_pontuacao_aluno(self.usuario, pontuacao)

app = App()
