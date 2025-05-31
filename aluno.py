from turma import Turma

class Aluno:
    def __init__(self, id : int, nome : str, email: str, turma : Turma, pontuacao : int):
        self.id = id
        self.nome = nome
        self.email = email
        self.turma = turma
        self.pontuacao = pontuacao