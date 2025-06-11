# TelaManterAlunos.py

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import janela
import app

from sgbd import (
    buscar_alunos,
    cadastrar_aluno,
    editar_aluno,
    excluir_aluno,
    buscar_turmas
)

class TelaManterAlunos(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # Fundo e cabeçalho
        raw = Image.open(r'images\imagemfundo1.jpg')\
            .resize((width, height), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(raw)
        self.create_image(0, 0, image=self.bg, anchor='nw')
        self.create_text(640, 100, text="Manutenção de Alunos", font=("Arial",24,"bold"),
                         fill="white", anchor='n')
        self.create_text(640, 150, text="Filtre, selecione e use os botões abaixo",
                         font=("Arial",16), fill="white", anchor='n')

        # --- Filtro por nome/email ---
        frm_filtros = tk.Frame(self, bg="black")
        tk.Label(frm_filtros, text="Buscar:", fg="white", bg="black").pack(side="left", padx=5)
        self.ent_filtro = tk.Entry(frm_filtros, width=40)
        self.ent_filtro.pack(side="left")
        tk.Button(frm_filtros, text="Filtrar", command=self.apply_filters).pack(side="left", padx=10)
        self.create_window(640, 200, window=frm_filtros, anchor='n')

        # --- Lista e scrollbar ---
        self.listbox = tk.Listbox(self, font=("Arial",12), width=80, height=15)
        sb = tk.Scrollbar(self, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=sb.set)
        self.create_window(640, 300, window=self.listbox, anchor='n')
        self.create_window(1040, 300, window=sb, anchor='n')

        # --- Botões CRUD e Voltar ---
        frm_botoes = tk.Frame(self, bg="black")
        tk.Button(frm_botoes, text="Cadastrar", command=self.novo_aluno).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Editar",    command=self.editar_selecionado).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Excluir",   command=self.excluir_selecionado).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Voltar",    command=self.voltar).pack(side="left", padx=5)
        self.create_window(640, 620, window=frm_botoes, anchor='n')

        # Dados
        self.alunos = []
        self.apply_filters()

    def apply_filters(self):
        termo = self.ent_filtro.get().strip().lower()
        todos = buscar_alunos()
        if termo:
            self.alunos = [a for a in todos
                           if termo in a.nome.lower() or termo in a.email.lower()]
        else:
            self.alunos = todos
        self.listbox.delete(0, tk.END)
        for a in self.alunos:
            self.listbox.insert(tk.END, f"{a.id}: {a.nome} ({a.email}) — Turma {a.turma.nome}")

    def get_selecao(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Nenhum aluno selecionado.")
            return None
        return self.alunos[sel[0]]

    def novo_aluno(self):
        AlunoForm(self, title="Cadastrar Aluno", callback=self._cadastrar)

    def editar_selecionado(self):
        aluno = self.get_selecao()
        if aluno:
            AlunoForm(self, aluno=aluno, title="Editar Aluno", callback=self._editar)

    def excluir_selecionado(self):
        aluno = self.get_selecao()
        if aluno and messagebox.askyesno("Confirmar", f"Excluir aluno {aluno.nome}?"):
            excluir_aluno(aluno)
            self.apply_filters()

    def _cadastrar(self, dados):
        resp = cadastrar_aluno(dados['nome'], dados['email'], dados['senha'], dados['turma'])
        if resp != None:
            messagebox.showerror("Erro", resp)
        else:
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        self.apply_filters()

    def _editar(self, dados):
        resp = editar_aluno(dados['id'], dados['nome'], dados['email'], dados['senha'], dados['turma'])
        if resp != None:
            messagebox.showerror("Erro", resp)
        else:
            messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
        self.apply_filters()

    def voltar(self):
        from TelaPrincipalPainel import TelaPrincipalPainel
        janela.janela.mudar_tela(TelaPrincipalPainel)


class AlunoForm(tk.Toplevel):
    def __init__(self, parent, aluno=None, title="Formulário", callback=None):
        super().__init__(parent)
        self.title(title)
        self.callback = callback
        self.aluno = aluno

        frm = tk.Frame(self, padx=10, pady=10)
        frm.pack()

        # Nome, Email, Senha
        tk.Label(frm, text="Nome:").grid(row=0, column=0, sticky="w")
        self.ent_nome  = tk.Entry(frm, width=40); self.ent_nome.grid(row=0, column=1, pady=5)
        tk.Label(frm, text="Email:").grid(row=1, column=0, sticky="w")
        self.ent_email = tk.Entry(frm, width=40); self.ent_email.grid(row=1, column=1, pady=5)
        tk.Label(frm, text="Senha:").grid(row=2, column=0, sticky="w")
        self.ent_senha = tk.Entry(frm, width=40, show="*"); self.ent_senha.grid(row=2, column=1, pady=5)

        # Dropdown de Turma
        tk.Label(frm, text="Turma:").grid(row=3, column=0, sticky="w")
        self.turmas = buscar_turmas()
        nomes = [t.nome for t in self.turmas]
        self.var_turma = tk.StringVar(value=nomes[0] if nomes else "")
        tk.OptionMenu(frm, self.var_turma, *nomes).grid(row=3, column=1, sticky="w", pady=5)

        # Pré-popula se for edição
        if aluno:
            self.ent_nome.insert(0, aluno.nome)
            self.ent_email.insert(0, aluno.email)
            # não preenche senha (por segurança)
            self.var_turma.set(aluno.turma.nome)

        tk.Button(self, text="Salvar", command=self.on_save).pack(pady=10)

    def on_save(self):
        nome  = self.ent_nome.get().strip()
        email = self.ent_email.get().strip()
        senha = self.ent_senha.get().strip()
        if not nome or not email:
            messagebox.showwarning("Aviso", "Nome e email são obrigatórios.")
            return
        # Seleciona objeto Turma
        turma_nome = self.var_turma.get()
        turma = next((t for t in self.turmas if t.nome == turma_nome), None)
        dados = {'nome': nome, 'email': email, 'senha': senha, 'turma': turma}
        if self.aluno:
            dados['id'] = self.aluno.id
        self.callback(dados)
        self.destroy()
