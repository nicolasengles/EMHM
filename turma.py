from professor import Professor

class Turma:
    def __init__(self, id : int, nome : str, professor_responsavel: Professor):
        self.id = id
        self.nome = nome
        self.professor_responsavel = professor_responsavel