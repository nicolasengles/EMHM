import tkinter as tk
from PIL import Image, ImageTk

class TelaInicial(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        # 1) Inicializa o Canvas com tamanho definido
        super().__init__(master, width=width, height=height, highlightthickness=highlightthickness)
        # 2) Empacota o Canvas antes de desenhar
        self.pack(fill="both", expand=True)

        # 3) Carrega as imagens e armazena em atributos de instância
        img_fundo = Image.open('images/imagemfundo0.png')
        self.imagem_fundo = ImageTk.PhotoImage(img_fundo)

        raw_titulo = Image.open("images/EXPEDICAO_DO_MILHAO.png").resize((750, 75), Image.LANCZOS)
        self.imagem_titulo = ImageTk.PhotoImage(raw_titulo)

        raw_subtitulo = Image.open("images/HistoriaseMapas.png").resize((500, 65), Image.LANCZOS)
        self.imagem_subtitulo = ImageTk.PhotoImage(raw_subtitulo)

        raw_deseja = Image.open("images/DesejaLogar.png").resize((300, 50), Image.LANCZOS)
        self.imagem_deseja = ImageTk.PhotoImage(raw_deseja)

        raw_prof = Image.open('images/FrameProfessor.png').resize((300, 80), Image.LANCZOS)
        self.imagem_professor = ImageTk.PhotoImage(raw_prof)

        raw_aluno = Image.open('images/FrameAluno.png').resize((300, 80), Image.LANCZOS)
        self.imagem_aluno = ImageTk.PhotoImage(raw_aluno)

        # 4) Desenha a tela: fundo, título, subtítulo e aviso “Deseja Logar?”
        self.create_image(0, 0, image=self.imagem_fundo, anchor=tk.NW)
        self.create_image(640, 100, image=self.imagem_titulo, anchor='n')
        self.create_image(810, 200, image=self.imagem_subtitulo, anchor='n')
        self.create_image(640, 320, image=self.imagem_deseja, anchor='n')

        # 5) Cria o botão “PROFESSOR” usando Canvas + tag única
        btn_prof_tag = 'btn_professor'
        self.create_image(
            640, 400,
            image=self.imagem_professor,
            anchor='n',
            tags=(btn_prof_tag,)  # observe a vírgula!
        )

        # 6) Vincula o clique na tag ao método on_first_click
        self.tag_bind(btn_prof_tag, '<Button-1>', self.on_first_click)

        # 7) Se desejar também um botão “ALUNO”, proceda de forma análoga:
        btn_aluno_tag = 'btn_aluno'
        self.create_image(
            640, 500,
            image=self.imagem_aluno,
            anchor='n',
            tags=(btn_aluno_tag,)
        )

        self.tag_bind(btn_aluno_tag, '<Button-1>', self.on_click_aluno)

    def on_first_click(self, event):
        print("Botão Professor clicado")
        #  Antes de criar a próxima tela, destrua tudo nesta janela:
        self.destroy()
        #  Importe aqui, dentro do método, para evitar problemas de import circular
        from TelaMenuPrincipal import TelaMenuPrincipal
        TelaMenuPrincipal(self.master)

    def on_click_aluno(self, event):
        print("Botão Aluno clicado")
        #  Destrói a tela atual:
        self.destroy()
        #  Se existir uma outra tela para “Aluno”, importe e instancie aqui.
        #  Por exemplo:
        # from TelaAluno import TelaAluno
        # TelaAluno(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    TelaInicial(root)
    root.mainloop()
