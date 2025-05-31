class Pergunta:
    def __init__(self, id : int, materia : int, dificuldade : int, enunciado : str, dica : str, resposta_correta : int, alternativas : tuple[str]):
        self.id = id
        self.materia = materia
        self.dificuldade = dificuldade
        self.enunciado = enunciado
        self.dica = dica
        self.resposta_correta = resposta_correta
        self.alternativas = alternativas