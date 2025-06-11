import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import janela

from sgbd import (
    buscar_perguntas,
    cadastrar_pergunta,
    editar_pergunta,
    excluir_pergunta
)

class TelaManterPerguntas(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        self.pack(fill="both", expand=True)

        # Mapas de filtro
        self.materia_map     = {"Todas": 2, "História": 0, "Geografia": 1}
        self.dificuldade_map = {"Todas": -1, "0": 0, "1": 1, "2": 2, "3": 3}

        # Carrega imagem de fundo e textos
        raw = Image.open(r'images\imagemfundo1.jpg')\
            .resize((width, height), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(raw)
        self.create_image(0, 0, image=self.bg, anchor='nw')
        self.create_text(640, 100, text="Manutenção de Perguntas", font=("Arial",24,"bold"), fill="white", anchor='n')
        self.create_text(640, 150, text="Filtre, selecione e use os botões abaixo", font=("Arial",16), fill="white", anchor='n')

        # --- Filtros ---
        frm_filtros = tk.Frame(self, bg="black")
        self.var_mat = tk.StringVar(value="Todas")
        self.var_dif = tk.StringVar(value="Todas")
        tk.Label(frm_filtros, text="Matéria:", fg="white", bg="black").pack(side="left", padx=5)
        tk.OptionMenu(frm_filtros, self.var_mat, *self.materia_map).pack(side="left")
        tk.Label(frm_filtros, text="Dificuldade:", fg="white", bg="black").pack(side="left", padx=5)
        tk.OptionMenu(frm_filtros, self.var_dif, *self.dificuldade_map).pack(side="left")
        tk.Button(frm_filtros, text="Filtrar", command=self.apply_filters).pack(side="left", padx=10)
        self.create_window(640, 200, window=frm_filtros, anchor='n')

        # --- Lista e scrollbar ---
        self.listbox = tk.Listbox(self, font=("Arial",12), width=80, height=15)
        sb = tk.Scrollbar(self, orient="vertical", command=self.listbox.yview)
        self.listbox.config(yscrollcommand=sb.set)
        self.create_window(640, 300, window=self.listbox,   anchor='n')
        self.create_window(1040,300, window=sb,              anchor='n')

        # --- Botões de CRUD e Voltar ---
        frm_botoes = tk.Frame(self, bg="black")
        tk.Button(frm_botoes, text="Cadastrar", command=self.nova_pergunta).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Editar",     command=self.editar_selecionada).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Excluir",    command=self.excluir_selecionada).pack(side="left", padx=5)
        tk.Button(frm_botoes, text="Voltar",     command=self.voltar).pack(side="left", padx=5)
        self.create_window(640, 620, window=frm_botoes, anchor='n')

        # Dados carregados
        self.perguntas = []
        self.apply_filters()

    def apply_filters(self):
        mat = self.materia_map[self.var_mat.get()]
        dif = self.dificuldade_map[self.var_dif.get()]
        self.load_perguntas(mat, dif)

    def load_perguntas(self, materia, dificuldade):
        self.listbox.delete(0, tk.END)
        self.perguntas = buscar_perguntas(materia, dificuldade)
        for p in self.perguntas:
            self.listbox.insert(tk.END, f"{p.id}: {p.enunciado}")

    def get_selecao(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Aviso", "Nenhuma pergunta selecionada.")
            return None
        return self.perguntas[sel[0]]

    def nova_pergunta(self):
        PerguntaForm(self, title="Cadastrar Pergunta", callback=self._cadastrar_callback)

    def editar_selecionada(self):
        p = self.get_selecao()
        if p:
            PerguntaForm(self, pergunta=p, title="Editar Pergunta", callback=self._editar_callback)

    def excluir_selecionada(self):
        p = self.get_selecao()
        if p and messagebox.askyesno("Confirmar", f"Excluir pergunta {p.id}?"):
            excluir_pergunta(p)
            self.apply_filters()

    def voltar(self):
        from TelaPrincipalPainel import TelaPrincipalPainel
        janela.janela.mudar_tela(TelaPrincipalPainel)
        

    def _cadastrar_callback(self, dados):
        cadastrar_pergunta(**dados)
        self.apply_filters()

    def _editar_callback(self, dados):
        editar_pergunta(**dados)
        self.apply_filters()

class PerguntaForm(tk.Toplevel):
    def __init__(self, parent, pergunta=None, title="Formulário", callback=None):
        super().__init__(parent)
        self.title(title)
        self.callback = callback
        self.pergunta = pergunta

        # Campos
        self.var_mat = tk.IntVar(value=getattr(pergunta, "materia", 0))
        self.var_dif = tk.IntVar(value=getattr(pergunta, "dificuldade", 0))
        self.txt_enun = tk.Text(self, width=60, height=4)
        self.ent_dica = tk.Entry(self, width=60)
        default = 'a'
        if pergunta:
            default = chr(ord('a') + pergunta.resposta_correta)
        self.var_resp = tk.StringVar(value=default)
        self.alternativas = [tk.Entry(self, width=60) for _ in range(5)]

        # Pré-popula se for edição
        if pergunta:
            self.txt_enun.insert("1.0", pergunta.enunciado)
            self.ent_dica.insert(0, pergunta.dica)
            for i, alt in enumerate(pergunta.alternativas):
                self.alternativas[i].insert(0, alt)

        # Layout
        tk.Label(self, text="Matéria (0=Hist,1=Geo):").grid(row=0, column=0, sticky="w")
        tk.OptionMenu(self, self.var_mat, 0,1).grid(row=0, column=1, sticky="w")
        tk.Label(self, text="Dificuldade (0–3):").grid(row=1, column=0, sticky="w")
        tk.OptionMenu(self, self.var_dif, 0,1,2,3).grid(row=1, column=1, sticky="w")

        tk.Label(self, text="Enunciado:").grid(row=2, column=0, sticky="nw")
        self.txt_enun.grid(row=2, column=1, pady=5)

        tk.Label(self, text="Dica:").grid(row=3, column=0, sticky="w")
        self.ent_dica.grid(row=3, column=1, pady=5)

        tk.Label(self, text="Resp. correta (a–e):").grid(row=4, column=0, sticky="w")
        tk.OptionMenu(self, self.var_resp, 'a','b','c','d','e').grid(row=4, column=1, sticky="w")

        for idx, entry in enumerate(self.alternativas):
            letra = chr(ord('a') + idx)
            tk.Label(self, text=f"Alt. {letra}:").grid(row=5+idx, column=0, sticky="w")
            entry.grid(row=5+idx, column=1, pady=2)

        tk.Button(self, text="Salvar", command=self.on_save).grid(row=10, column=0, columnspan=2, pady=10)

    def on_save(self):
        letra = self.var_resp.get()
        resp_idx = ord(letra) - ord('a')
        dados = {
            'materia': self.var_mat.get(),
            'dificuldade': self.var_dif.get(),
            'enunciado': self.txt_enun.get("1.0", "end").strip(),
            'dica': self.ent_dica.get().strip(),
            'resposta_correta': resp_idx,
            'alternativas': tuple(e.get().strip() for e in self.alternativas)
        }
        if self.pergunta:
            dados['id'] = self.pergunta.id
        self.callback(dados)
        self.destroy()
