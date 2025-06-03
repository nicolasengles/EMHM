import mysql.connector
from os import getenv
from dotenv import load_dotenv
from aluno import Aluno
from pergunta import Pergunta
from turma import Turma
from professor import Professor
import app
from enums import TipoUsuario

load_dotenv()

sgbd = mysql.connector.connect(
    host=getenv("HOST"),
    port=int(getenv("PORT")),
    user=getenv("USER"),
    password=getenv("PASSWORD"),
    database=getenv("DATABASE")
)

bd = sgbd.cursor()

def autenticar_usuario(tipo_usuario: TipoUsuario, email : str, senha : str):
    try:
        match tipo_usuario:
            case TipoUsuario.ALUNO:
                bd.execute(f"SELECT * FROM aluno WHERE email = '{email}' AND senha = '{senha}';")
                dados = bd.fetchall()[0]

                bd.execute(f"SELECT * FROM turma WHERE id = {dados[5]};")
                dados_turma = bd.fetchall()[0]

                app.app.usuario = Aluno(
                    id=dados[0],
                    email=dados[1],
                    nome=dados[3],
                    pontuacao=dados[4],
                    turma=Turma(
                        id=dados_turma[0],
                        nome=dados_turma[1],
                        professor_responsavel=None
                    )
                )

            case app.TipoUsuario.PROFESSOR:
                bd.execute(f"SELECT * FROM professor WHERE email = '{email}' AND senha = '{senha}';")
                dados = bd.fetchall()[0]

                app.usuario = Professor(
                    id=dados[0],
                    email=dados[1],
                    senha=dados[2],
                    nome=dados[3]
                )
    
    except IndexError:
        print("Email e/ou senha incorretos")
    except Exception as erro:
        print(erro)

def cadastrar_professor(nome : str, email : str, senha : str):
    if len(nome.split()) < 2:
        print("Por favor, insira nome e sobrenome")
        return
    
    if len(nome) > 100:
        print("O nome deve ter no máximo 100 caracteres")
        return
    
    if email[-20:] != "@sistemapoliedro.com":
        print("Email inválido. Por favor, utilize seu email institucional (@sistemapoliedro.com)")
        return
    
    if len(email) > 100:
        print("O email deve ter no máximo 100 caracteres")
        return

    if len(senha) < 8:
        print("A senha deve conter no mínimo 8 caracteres")
        return
    
    if len(senha) > 100:
        print("A senha deve conter no máximo 100 caracteres")
        return
    
    bd.execute(f"SELECT * FROM professor WHERE email = '{email}';")
    if len(bd.fetchall()) > 0:
        print("Já existe uma conta associada a este email.")
        return
    
    try:
        bd.execute(f"INSERT INTO professor (nome, email, senha) VALUES ('{nome}', '{email}', '{senha}');")
        sgbd.commit()
    except Exception as erro:
        print("Ops! Algo deu errado.")
        print(erro)
        return
    
    autenticar_usuario(app.TipoUsuario.PROFESSOR, email=email, senha=senha)

def editar_professor(id : int, nome : str, email : str, senha : str):
    if len(nome.split()) < 2:
        print("Por favor, insira nome e sobrenome")
        return
    
    if len(nome) > 100:
        print("O nome deve ter no máximo 100 caracteres")
        return
    
    if email[-20:] != "@sistemapoliedro.com":
        print("Email inválido. Por favor, utilize seu email institucional (@sistemapoliedro.com)")
        return
    
    if len(email) > 100:
        print("O email deve ter no máximo 100 caracteres")
        return

    if len(senha) > 0 and len(senha) < 8:
        print("A senha deve conter no mínimo 8 caracteres")
        return
    
    if len(senha) > 100:
        print("A senha deve conter no máximo 100 caracteres")
        return
    
    bd.execute(f"SELECT * FROM professor WHERE email = '{email}';")
    if len(bd.fetchall()) > 0:
        print("Já existe uma conta associada a este email.")
        return
    
    try:
        if senha == "":
            bd.execute(f"UPDATE professor SET nome = '{nome}', email = '{email}' WHERE id = {id};")
        else:
            bd.execute(f"UPDATE professor SET nome = '{nome}', email = '{email}', senha = '{senha}' WHERE id = {id};")
        sgbd.commit()
    except:
        print("Ops! Algo deu errado.")
        return
    
def buscar_alunos():
    bd.execute("SELECT * FROM aluno")
    resultados = bd.fetchall()

    alunos = []
    for resultado in resultados:
            turma = None
            for i in app.turmas:
                if i.id == resultado[5]:
                    turma = i
            
            if turma == None:
                bd.execute(f"SELECT * FROM turma WHERE id = {resultado[5]};")
                dados = bd.fetchall()[0]
                turma = Turma(
                    id=dados[0],
                    nome=dados[1],
                    professor_responsavel=app.usuario
                )

            aluno = Aluno(
                id=resultado[0],
                email=resultado[1],
                nome=resultado[3],
                pontuacao=resultado[4],
                turma=turma
            )
            alunos.append(aluno)
    return alunos

def cadastrar_aluno(nome : str, email : str, senha : str, turma : str):
    if len(nome.split()) < 2:
        print("Por favor, insira nome e sobrenome")
        return
    
    if len(nome) > 100:
        print("O nome deve ter no máximo 100 caracteres")
        return
    
    if email[-9:] != "@p4ed.com":
        print("Email inválido. Por favor, utilize o email institucional (@p4ed.com)")
        return
    
    if len(email) > 100:
        print("O email deve ter no máximo 100 caracteres")
        return

    if len(senha) < 8:
        print("A senha deve conter no mínimo 8 caracteres")
        return
    
    if len(senha) > 100:
        print("A senha deve conter no máximo 100 caracteres")
        return
    
    bd.execute(f"SELECT * FROM aluno WHERE email = '{email}';")
    if len(bd.fetchall()) > 0:
        print("Já existe uma conta associada a este email.")
        return
    
    try:
        bd.execute(f"INSERT INTO aluno (nome, email, senha, pontuacao, turma_id) VALUES ('{nome}', '{email}', '{senha}', 0, {turma.id});")
        sgbd.commit()
    except Exception as erro:
        print(erro)

def editar_aluno(id : int, nome : str, email : str, senha : str, turma : str):
    if len(nome.split()) < 2:
        print("Por favor, insira nome e sobrenome")
        return
    
    if len(nome) > 100:
        print("O nome deve ter no máximo 100 caracteres")
        return
    
    if email[-9:] != "@p4ed.com":
        print("Email inválido. Por favor, utilize o email institucional (@p4ed.com)")
        return
    
    if len(email) > 100:
        print("O email deve ter no máximo 100 caracteres")
        return

    if len(senha) > 0 and len(senha) < 8:
        print("A senha deve conter no mínimo 8 caracteres")
        return
    
    if len(senha) > 100:
        print("A senha deve conter no máximo 100 caracteres")
        return
    
    bd.execute(f"SELECT * FROM aluno WHERE email = '{email}';")
    if len(bd.fetchall()) > 0:
        print("Já existe uma conta associada a este email.")
        return
    
    try:
        if senha == "":
            bd.execute(f"UPDATE aluno SET nome = '{nome}', email = '{email}', turma_id = {turma.id} WHERE id = {id};")
        else:
            bd.execute(f"UPDATE aluno SET nome = '{nome}', email = '{email}', senha = '{senha}', turma_id = {turma.id} WHERE id = {id};")
        sgbd.commit()
    except:
        print("Ops! Algo deu errado.")

def excluir_aluno(aluno : Aluno):
    bd.execute(f"DELETE FROM aluno WHERE id = {aluno.id}")
    sgbd.commit()

def buscar_perguntas(materia, dificuldade):
    if dificuldade == -1:
        bd.execute(f"SELECT * FROM pergunta;")
    elif materia == 2:
        bd.execute(f"SELECT * FROM pergunta WHERE dificuldade = {dificuldade};")
    else:
        bd.execute(f"SELECT * FROM pergunta WHERE materia = '{materia}' AND dificuldade = {dificuldade};")

    resultados = bd.fetchall()
    
    perguntas = []
    for resultado in resultados:
            pergunta = Pergunta(
                id=resultado[0],
                materia=resultado[1],
                dificuldade=resultado[2],
                enunciado=resultado[3],
                dica=resultado[4],
                resposta_correta=resultado[5],
                alternativas=[
                    resultado[6],
                    resultado[7],
                    resultado[8],
                    resultado[9],
                    resultado[10]
                ]
            )
            perguntas.append(pergunta)
    return perguntas

def cadastrar_pergunta(materia : int, dificuldade : int, enunciado : str, dica : str, resposta_correta : int, alternativas : tuple[str]):
    try:
        bd.execute(f"INSERT INTO pergunta (materia, dificuldade, enunciado, dica, resposta_correta, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e) VALUES ({materia}, {dificuldade}, '{enunciado}', '{dica}', {resposta_correta}, '{alternativas[0]}', '{alternativas[1]}', '{alternativas[2]}', '{alternativas[3]}', '{alternativas[4]}');")
        sgbd.commit()
    except Exception as erro:
        print(erro)

def editar_pergunta(id : int, materia : int, dificuldade : int, enunciado : str, dica : str, resposta_correta : int, alternativas : tuple[str]):
    try:
        bd.execute(f"UPDATE pergunta SET materia = {materia}, dificuldade = {dificuldade}, enunciado = '{enunciado}', dica = '{dica}', resposta_correta = {resposta_correta}, alternativa_a = '{alternativas[0]}', alternativa_b = '{alternativas[1]}', alternativa_c = '{alternativas[2]}', alternativa_d = '{alternativas[3]}', alternativa_e ='{alternativas[4]}' WHERE id = {id};")
        sgbd.commit()
    except Exception as erro:
        print(erro)

def excluir_pergunta(pergunta : Pergunta):
    bd.execute(f"DELETE FROM pergunta WHERE id = {pergunta.id}")
    sgbd.commit()

def buscar_turmas():
    bd.execute(f"SELECT * FROM turma")
    resultados = bd.fetchall()

    turmas = []
    for resultado in resultados:
            turma = Turma(
                id=resultado[0],
                nome=resultado[1],
                professor_responsavel=app.usuario
            )
            turmas.append(turma)
    return turmas

def cadastrar_turma(nome : str, id_professor : int):
    if len([turma for turma in buscar_turmas() if nome == turma.nome]) > 0:
        print("Já existe uma turma com este nome.")
        return

    bd.execute(f"INSERT INTO turma (nome, professor_id) VALUES ('{nome}', {id_professor});")
    sgbd.commit()

def editar_turma(id : int, nome : str):
    bd.execute(f"UPDATE turma SET nome = '{nome}' WHERE id = {id};")
    sgbd.commit()
    turma = [turma for turma in app.turmas if turma.id == id][0]
    turma.nome = nome

def excluir_turma(turma : Turma):
    bd.execute(f"DELETE FROM turma WHERE id = {turma.id}")
    sgbd.commit()
    app.turmas.remove(turma)
