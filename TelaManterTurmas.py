# TelaManterTurmas.py

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import janela
import app

from sgbd import (
    buscar_turmas,
    cadastrar_turma,
    editar_turma,
    excluir_turma
)


class TelaManterTurmas(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # Carrega fundo e textos
        raw = Image.open(r'images\black-solid-background-2920-x-1642-jk98dr7udfcq3hqj.jpg')\
            .resize((width, height), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(raw)
        self.create_image(0, 0, image=self.bg, anchor='nw')
        self.create_text(640, 100, text="Manutenção de Turmas", font=("Arial",24,"bold"), fill="white", anchor='n')
        self.create_text(640, 150, text="Filtre, selecione e use os botões abaixo", font=("Arial",16), fill="white", anchor='n')

        # --- Filtro por nome ---
        frm_filtros = tk.Frame(self, bg="black")
        tk.Label(frm_filtros, text="Nome:", fg="white", bg="black").pack(side="left", padx=5)
        self.ent_nome = tk.Entry(frm_filtros, width=30)
        self.ent_nome.pack(side="left")
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
        tk.Button(frm_botoes, text="Cadastrar", command=self.nova_turma).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Editar",    command=self.editar_selecionada).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Excluir",   command=self.excluir_selecionada).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Voltar",    command=self.voltar).pack(side="left", padx=5)
        self.create_window(640, 620, window=frm_botoes, anchor='n')

        # Dados
        self.turmas = []
        self.apply_filters()

    def apply_filters(self):
        filtro = self.ent_nome.get().strip().lower()
        self.load_turmas(filtro)

    def load_turmas(self, filtro_nome):
        self.listbox.delete(0, tk.END)
        all_turmas = buscar_turmas()
        if filtro_nome:
            self.turmas = [t for t in all_turmas if filtro_nome in t.nome.lower()]
        else:
            self.turmas = all_turmas
        for t in self.turmas:
            self.listbox.insert(tk.END, f"{t.id}: {t.nome}")

    def get_selecao(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Nenhuma turma selecionada.")
            return None
        return self.turmas[sel[0]]

    def nova_turma(self):
        TurmaForm(self, title="Cadastrar Turma", callback=self._cadastrar_callback)

    def editar_selecionada(self):
        t = self.get_selecao()
        if t:
            TurmaForm(self, turma=t, title="Editar Turma", callback=self._editar_callback)

    def excluir_selecionada(self):
        t = self.get_selecao()
        if t and messagebox.askyesno("Confirmar", f"Excluir turma {t.id}?"):
            excluir_turma(t)
            self.apply_filters()

    def voltar(self):
        from TelaPrincipalPainel import TelaPrincipalPainel
        janela.janela.mudar_tela(TelaPrincipalPainel)

    def _cadastrar_callback(self, dados):
        # dados: {'nome': ...}
        cadastrar_turma(dados['nome'], app.app.usuario.id)
        self.apply_filters()

    def _editar_callback(self, dados):
        # dados: {'id': ..., 'nome': ...}
        editar_turma(dados['id'], dados['nome'])
        self.apply_filters()


class TurmaForm(tk.Toplevel):
    def __init__(self, parent, turma=None, title="Formulário", callback=None):
        super().__init__(parent)
        self.title(title)
        self.callback = callback
        self.turma = turma

        tk.Label(self, text="Nome da Turma:").pack(padx=10, pady=(10,0), anchor="w")
        self.ent_nome = tk.Entry(self, width=50)
        self.ent_nome.pack(padx=10, pady=5)
        if turma:
            self.ent_nome.insert(0, turma.nome)

        tk.Button(self, text="Salvar", command=self.on_save).pack(pady=10)

    def on_save(self):
        nome = self.ent_nome.get().strip()
        if not nome:
            messagebox.showwarning("Aviso", "O nome da turma não pode ficar vazio.")
            return
        dados = {'nome': nome}
        if self.turma:
            dados['id'] = self.turma.id
        self.callback(dados)
        self.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    TelaManterTurmas(root)
    root.mainloop()
