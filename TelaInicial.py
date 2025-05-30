import tkinter as tk
from PIL import Image, ImageTk

class TelaInicial(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master)
        # Insira aqui todo o código desta tela
        arquivo_imagem_fundo = Image.open('images/imagemfundo0.png')
        imagem_fundo = ImageTk.PhotoImage(arquivo_imagem_fundo) 

        arquivo_imagem_titulo = Image.open(r"images/EXPEDICAO_DO_MILHAO.png").resize((750, 75), Image.LANCZOS)
        imagem_titulo = ImageTk.PhotoImage(arquivo_imagem_titulo) 

        arquivo_imagem_subtitulo = Image.open(r"images/HistoriaseMapas.png").resize((500, 65), Image.LANCZOS)
        imagem_subtitulo = ImageTk.PhotoImage(arquivo_imagem_subtitulo) 
        arquivo_DesejaLogar = Image.open(r"images/DesejaLogar.png").resize((300, 50), Image.LANCZOS)
        imagem_DesejaLogar = ImageTk.PhotoImage(arquivo_DesejaLogar)
        arquivo_professor = Image.open(r'images/FrameProfessor.png').resize((300, 80), Image.LANCZOS)
        imagem_professor = ImageTk.PhotoImage(arquivo_professor)
        arquivo_aluno = Image.open(r'images/FrameAluno.png').resize((300, 80), Image.LANCZOS)
        imagem_aluno = ImageTk.PhotoImage(arquivo_aluno)

# Criar canvas e adicionar título, subtitulo e imagem de fundo
        self.pack(fill="both", expand=True)
        self.create_image(0, 0, image=imagem_fundo, anchor=tk.NW)
        self.create_image(640, 100, image=imagem_titulo, anchor='n')
        self.create_image(810, 200, image=imagem_subtitulo)
        self.create_image(640, 320, image=imagem_DesejaLogar, anchor='n')


# Botão Professor
        botao_x, botao_y = 640, 300 + 62 + 15
        comprimento_botao, altura_botao = 406, 70

        retangulo3 = self.create_rectangle(
            botao_x - comprimento_botao/2, botao_y,
            botao_x + comprimento_botao/2, botao_y + altura_botao,
            fill='', outline=''
        )
        imagem3 = self.create_image(botao_x, botao_y, image=imagem_professor, anchor='n')

        for tag in (retangulo3, imagem3):
            self.tag_bind(tag, '<Button-1>')

       # Segundo botão
        botao4_y = botao_y + altura_botao + 30
        retangulo4 = self.create_rectangle(
            botao_x - comprimento_botao/2, botao4_y,
            botao_x + comprimento_botao/2, botao4_y + altura_botao,
        fill='', outline=''
)

        imagem4 = self.create_image(botao_x, botao4_y, image=imagem_aluno, anchor='n')

        def on_second_click(event):
            print("Botão Aluno botão clicado")

        for tag in (retangulo4, imagem4):
            self.tag_bind(tag, '<Button-1>', on_second_click)

        
 # Manter imagens na memória
        master.bg_img = imagem_fundo
        master.title_img = imagem_titulo
        master.subtitulo = imagem_subtitulo
        master.logar = imagem_DesejaLogar
        master.professor = imagem_professor
        master.aluno = imagem_aluno
     