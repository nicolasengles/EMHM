import mysql.connector
from os import getenv
from dotenv import load_dotenv
from aluno import Aluno
from pergunta import Pergunta
from turma import Turma
from professor import Professor
import app

load_dotenv('.env')

def conectar_sgbd():
    sgbd = mysql.connector.connect(
        host=getenv("DB_HOST"),
        port=int(getenv("DB_PORT")),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        database=getenv("DB_DATABASE")
    )
    return sgbd

def autenticar_usuario(tipo_usuario: int, email : str, senha : str):
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        match tipo_usuario:
            case 0:
                bd.execute("SELECT * FROM aluno WHERE email = %s AND senha = %s;", (email, senha))
                dados = bd.fetchall()[0]

                bd.execute("SELECT * FROM turma WHERE id = %s;", (dados[5],))
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

            case 1:
                bd.execute("SELECT * FROM professor WHERE email = %s AND senha = %s;", (email, senha))
                dados = bd.fetchall()[0]

                app.app.usuario = Professor(
                    id=dados[0],
                    email=dados[1],
                    senha=dados[2],
                    nome=dados[3]
                )

        return None
    except IndexError:
        return "Email e/ou senha incorretos"
    except Exception as erro:
        print(erro)
        return "Ops! Algo deu errado!"
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def cadastrar_professor(nome : str, email : str, senha : str):
    if len(nome.split()) < 2:
        return "Por favor, insira nome e sobrenome"
    
    if len(nome) > 100:
        return "O nome deve ter no máximo 100 caracteres"
    
    if email[-20:] != "@sistemapoliedro.com":
        return "Email inválido. Por favor, utilize seu email institucional (@sistemapoliedro.com)"
    
    if len(email) > 100:
        return "O email deve ter no máximo 100 caracteres"

    if len(senha) < 8:
        return "A senha deve conter no mínimo 8 caracteres"
    
    if len(senha) > 100:
        return "A senha deve conter no máximo 100 caracteres"
    
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()

        bd.execute("SELECT * FROM professor WHERE email = %s;", (email,))
        if len(bd.fetchall()) > 0:
            return "Já existe uma conta associada a este email."
        
        bd.execute("INSERT INTO professor (nome, email, senha) VALUES (%s, %s, %s);", (nome, email, senha))
        sgbd.commit()
        autenticar_usuario(1, email=email, senha=senha)
    except Exception as erro:
        print(erro)
        return "Ops! Algo deu errado."
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def editar_professor(id : int, nome : str, email : str, senha : str):
    if len(nome.split()) < 2:
        return "Por favor, insira nome e sobrenome"   
    
    if len(nome) > 100:
        return "O nome deve ter no máximo 100 caracteres"
    
    if email[-20:] != "@sistemapoliedro.com":
        return "Email inválido. Por favor, utilize seu email institucional (@sistemapoliedro.com)"
    
    if len(email) > 100:
        return "O email deve ter no máximo 100 caracteres"

    if len(senha) > 0 and len(senha) < 8:
        return "A senha deve conter no mínimo 8 caracteres"
    
    if len(senha) > 100:
        return "A senha deve conter no máximo 100 caracteres"
    
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()

        bd.execute("SELECT * FROM professor WHERE email = %s;", (email,))
        if len(bd.fetchall()) > 0:
            return "Já existe uma conta associada a este email."
    
        if senha == "":
            bd.execute("UPDATE professor SET nome = %s, email = %s WHERE id = %s;", (nome, email, id))
        else:
            bd.execute("UPDATE professor SET nome = %s, email = %s, senha = %s WHERE id = %s;", (nome, email, senha, id))
        sgbd.commit()
    except:
        return "Ops! Algo deu errado."
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()
    
def buscar_alunos():
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("SELECT * FROM aluno")
        resultados = bd.fetchall()

        alunos = []
        for resultado in resultados:
                turma = None
                for i in app.app.turmas:
                    if i.id == resultado[5]:
                        turma = i
                
                if turma == None:
                    bd.execute("SELECT * FROM turma WHERE id = %s;", (resultado[5],))
                    dados = bd.fetchall()[0]
                    turma = Turma(
                        id=dados[0],
                        nome=dados[1],
                        professor_responsavel=app.app.usuario
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
    finally:
            if bd:
                bd.close()
            if sgbd:
                sgbd.close()

def cadastrar_aluno(nome : str, email : str, senha : str, turma : str):
    if len(nome.split()) < 2:
        return "Por favor, insira nome e sobrenome"
    
    if len(nome) > 100:
        return "O nome deve ter no máximo 100 caracteres"
    
    if email[-9:] != "@p4ed.com":
        return "Email inválido. Por favor, utilize o email institucional (@p4ed.com)"
    
    if len(email) > 100:
        return "O email deve ter no máximo 100 caracteres"

    if len(senha) < 8:
        return "A senha deve conter no mínimo 8 caracteres"
    
    if len(senha) > 100:
        return "A senha deve conter no máximo 100 caracteres"
    
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()

        bd.execute(f"SELECT * FROM aluno WHERE email = %s;", (email,))
        if len(bd.fetchall()) > 0:
            return "Já existe uma conta associada a este email."
        
        bd.execute("INSERT INTO aluno (nome, email, senha, pontuacao, turma_id) VALUES (%s, %s, %s, 0, %s);", (nome, email, senha, turma.id))
        sgbd.commit()
    except Exception as erro:
        print(erro)
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def editar_aluno(id : int, nome : str, email : str, senha : str, turma : str):
    if len(nome.split()) < 2:
        return "Por favor, insira nome e sobrenome"
    
    if len(nome) > 100:
        return "O nome deve ter no máximo 100 caracteres"
    
    if email[-9:] != "@p4ed.com":
        return "Email inválido. Por favor, utilize o email institucional (@p4ed.com)"
    
    if len(email) > 100:
        return "O email deve ter no máximo 100 caracteres"

    if len(senha) > 0 and len(senha) < 8:
        return "A senha deve conter no mínimo 8 caracteres"
    
    if len(senha) > 100:
        return "A senha deve conter no máximo 100 caracteres"
    
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()

        bd.execute("SELECT * FROM aluno WHERE email = %s;", (email,))
        if len(bd.fetchall()) > 1:
            return "Já existe uma conta associada a este email."
        
        if senha == "":
            bd.execute("UPDATE aluno SET nome = %s, email = %s, turma_id = %s WHERE id = %s;", (nome, email, turma.id, id))
        else:
            bd.execute("UPDATE aluno SET nome = %s, email = %s, senha = %s, turma_id = %s WHERE id = %s", (nome, email, senha, turma.id, id))
        sgbd.commit()
    except:
        return "Ops! Algo deu errado."
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def excluir_aluno(aluno : Aluno):
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("DELETE FROM aluno WHERE id = %s", (aluno.id,))
        sgbd.commit()
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def buscar_perguntas(materia, dificuldade):
    query = "SELECT * FROM pergunta"
    params = []
    condicoes = []

    if materia != 2:
        condicoes.append("materia = %s")
        params.append(materia)

    if dificuldade != -1:
        condicoes.append("dificuldade = %s")
        params.append(dificuldade)

    if condicoes:
        query += " WHERE " + " AND ".join(condicoes)

    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute(query, tuple(params))
        resultados = bd.fetchall()

        perguntas = []
        for r in resultados:
            perguntas.append(Pergunta(
                id=r[0],
                materia=r[1],
                dificuldade=r[2],
                enunciado=r[3],
                dica=r[4],
                resposta_correta=r[5],
                alternativas=[r[6], r[7], r[8], r[9], r[10]]
            ))
        return perguntas
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def cadastrar_pergunta(materia : int, dificuldade : int, enunciado : str, dica : str, resposta_correta : int, alternativas : tuple[str]):
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("INSERT INTO pergunta (materia, dificuldade, enunciado, dica, resposta_correta, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (materia, dificuldade, enunciado, dica, resposta_correta, alternativas[0], alternativas[1], alternativas[2], alternativas[3], alternativas[4]))
        sgbd.commit()
    except Exception as erro:
        print(erro)
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def editar_pergunta(id : int, materia : int, dificuldade : int, enunciado : str, dica : str, resposta_correta : int, alternativas : tuple[str]):
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("UPDATE pergunta SET materia = %s, dificuldade = %s, enunciado = %s, dica = %s, resposta_correta = %s, alternativa_a = %s, alternativa_b = %s, alternativa_c = %s, alternativa_d = %s, alternativa_e = %s WHERE id = %s;", (materia, dificuldade, enunciado, dica, resposta_correta, alternativas[0], alternativas[1], alternativas[2], alternativas[3], alternativas[4]))
        sgbd.commit()
    except Exception as erro:
        print(erro)
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def excluir_pergunta(pergunta : Pergunta):
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("DELETE FROM pergunta WHERE id = %s", (pergunta.id,))
        sgbd.commit()
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def buscar_turmas():
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("SELECT * FROM turma")
        resultados = bd.fetchall()

        turmas = []
        for resultado in resultados:
                turma = Turma(
                    id=resultado[0],
                    nome=resultado[1],
                    professor_responsavel=app.app.usuario
                )
                turmas.append(turma)
        return turmas
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def cadastrar_turma(nome : str, id_professor : int):
    if len([turma for turma in buscar_turmas() if nome == turma.nome]) > 0:
        return "Já existe uma turma com este nome."
    
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("INSERT INTO turma (nome, professor_id) VALUES (%s, %s);", (nome, id_professor))
        sgbd.commit()
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def editar_turma(id : int, nome : str):
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("UPDATE turma SET nome = %s WHERE id = %s;", (nome, id))
        sgbd.commit()
        turma = [turma for turma in app.app.turmas if turma.id == id][0]
        turma.nome = nome
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def excluir_turma(turma : Turma):
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("DELETE FROM turma WHERE id = %s", (turma.id,))
        sgbd.commit()
        app.app.turmas.remove(turma)
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()

def incrementar_pontuacao_aluno(aluno : Aluno, pontuacao : int):
    try:
        sgbd = conectar_sgbd()
        bd = sgbd.cursor()
        bd.execute("SELECT pontuacao FROM aluno WHERE id = %s;", (aluno.id,))
        pontuacao_antiga = bd.fetchall()[0][0]
        pontuacao_nova = pontuacao_antiga + pontuacao
        bd.execute("UPDATE aluno SET pontuacao = %s WHERE id = %s;", (pontuacao_nova, aluno.id))
        sgbd.commit()
        app.app.usuario.pontuacao = pontuacao_nova
    finally:
        if bd:
            bd.close()
        if sgbd:
            sgbd.close()