from sgbd import *
import app
import unittest

class Teste_SGBD(unittest.TestCase):
    def test_autenticar_aluno(self):
        autenticar_usuario(app.TipoUsuario.ALUNO, "marciopereira@p4ed.com", "123456789")
        self.assertEqual(app.usuario.id, 1)
        self.assertEqual(app.usuario.nome, "Marcio Pereira")
        self.assertEqual(app.usuario.email, "marciopereira@p4ed.com")
        self.assertEqual(app.usuario.pontuacao, 0)
        app.usuario = None
    
    def test_autenticar_professor(self):
        autenticar_usuario(app.TipoUsuario.PROFESSOR, "flaviosantos@sistemapoliedro.com", "123456789")
        self.assertEqual(app.usuario.id, 1)
        self.assertEqual(app.usuario.nome, "Flavio Santos")
        self.assertEqual(app.usuario.email, "flaviosantos@sistemapoliedro.com")
        app.usuario = None

    def test_buscar_turma(self):
        app.turmas = buscar_turmas()
        self.assertGreater(len(app.turmas), 0)

    def test_cadastrar_turma(self):
        autenticar_usuario(app.TipoUsuario.PROFESSOR, "flaviosantos@sistemapoliedro.com", "123456789")
        cadastrar_turma("3 ANO C - PAULISTA", app.usuario.id)
        turma = [turma for turma in buscar_turmas() if turma.nome == "3 ANO C - PAULISTA"]
        self.assertGreater(len(turma), 0)
        app.usuario = None

    def test_editar_turma(self):
        app.turmas = buscar_turmas()
        turma = app.get_turma("3 ANO C - PAULISTA")
        editar_turma(turma.id, "2 ANO A - PARAISO")
        self.assertTrue(app.get_turma("2 ANO A - PARAISO"))

    def test_buscar_alunos(self):
        alunos = buscar_alunos()
        self.assertGreater(len(alunos), 0)

    def test_cadastrar_aluno(self):
        app.turmas = buscar_turmas()
        turma = app.get_turma("1 ANO A - PAULISTA")
        cadastrar_aluno("Marcelo Silva", "marcelosilva@p4ed.com", "123456789", turma)
        self.assertGreater(len([aluno for aluno in buscar_alunos() if aluno.nome == "Marcelo Silva"]), 0)

    def test_editar_aluno(self):
        autenticar_usuario(app.TipoUsuario.ALUNO, "marcelosilva@p4ed.com", "123456789")
        app.turmas = buscar_turmas()
        editar_aluno(app.usuario.id, "Ronaldo Pereira", "ronaldopereira@p4ed.com", "", app.get_turma("1 ANO A - PAULISTA"))
        self.assertGreater(len([aluno for aluno in buscar_alunos() if aluno.nome == "Ronaldo Pereira"]), 0)
        app.usuario = None

    def test_excluir_aluno(self):
        autenticar_usuario(app.TipoUsuario.ALUNO, "ronaldopereira@p4ed.com", "123456789")
        excluir_aluno(app.usuario)
        self.assertNotIn(app.usuario, buscar_alunos())
        app.usuario = None

    def test_excluir_turma(self):
        turma = app.get_turma("2 ANO A - PARAISO")
        excluir_turma(turma)
        self.assertEqual(len([turma for turma in buscar_turmas() if turma.nome == "2 ANO A - PARAISO"]), 0)
        self.assertFalse(app.get_turma("2 ANO A - PARAISO"))

    def test_cadastrar_professor(self):
        cadastrar_professor("Rogerio Fahur", "rogeriofahur@sistemapoliedro.com", "123456789")
        autenticar_usuario(app.TipoUsuario.PROFESSOR, "rogeriofahur@sistemapoliedro.com", "123456789")
        self.assertEqual(app.usuario.nome, "Rogerio Fahur")
        self.assertEqual(app.usuario.email, "rogeriofahur@sistemapoliedro.com")
        app.usuario = None

    def test_editar_professor(self):
        autenticar_usuario(app.TipoUsuario.PROFESSOR, "rogeriofahur@sistemapoliedro.com", "123456789")
        id_prof = app.usuario.id
        editar_professor(id_prof, "Maria Souza", "mariasouza@sistemapoliedro.com", "")
        app.usuario = None
        autenticar_usuario(app.TipoUsuario.PROFESSOR, "mariasouza@sistemapoliedro.com", "123456789")
        self.assertEqual(app.usuario.nome, "Maria Souza")
        self.assertEqual(app.usuario.email, "mariasouza@sistemapoliedro.com")
        self.assertEqual(app.usuario.id, id_prof)

    def test_buscar_perguntas(self):
        app.perguntas = buscar_perguntas(-1, -1)
        self.assertGreater(len(app.perguntas), 0)

    def test_cadastrar_pergunta(self):
        cadastrar_pergunta(
            0, 
            0, 
            "Em que ano terminou a segunda guerra mundial?",
            "Entre 1940 e 1950",
            2,
            (
                "1930",
                "1939",
                "1945",
                "1942",
                "1951"
            )
        )
        self.assertGreater(len([pergunta for pergunta in buscar_perguntas(-1, -1) if pergunta.enunciado == "Em que ano terminou a segunda guerra mundial?"]), 0)

    def test_editar_pergunta(self):
        app.perguntas = buscar_perguntas(-1, -1)
        pergunta = app.perguntas[1]
        editar_pergunta(
            pergunta.id,
            pergunta.materia,
            pergunta.dificuldade, 
            "Em que ano foi proclamada a independência?",
            "Século IX",
            0,
            (
                "1822",
                "1832",
                "1944",
                "1671",
                "1500"
            )
        )
        app.perguntas = buscar_perguntas(-1, -1)
        pergunta = app.perguntas[1]
        self.assertEqual(pergunta.enunciado, "Em que ano foi proclamada a independência?")
        self.assertEqual(pergunta.dica, "Século IX")

    def test_excluir_pergunta(self):
        excluir_pergunta(app.perguntas[1])
        self.assertNotIn(app.perguntas[1], buscar_perguntas(-1, -1))