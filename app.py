# from enum import Enum
from aluno import Aluno
from professor import Professor
from turma import Turma
from partida import Partida
# from janela import Janela

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

    def finalizar_partida(self):
        self.partida = None

app = App()
