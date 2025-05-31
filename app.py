from enum import Enum
from aluno import Aluno
from professor import Professor
from turma import Turma

class TipoUsuario(Enum):
    ALUNO = 0
    PROFESSOR = 1

usuario = None
    
turmas = []
perguntas = []

def get_turma(nome : str):
    try:
        return [turma for turma in turmas if turma.nome == nome][0]
    except IndexError:
        return None
