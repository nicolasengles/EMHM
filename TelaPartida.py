import tkinter as tk
from PIL import Image, ImageTk

class TelaPartida(tk.Canvas):
    def __init__(self, master, width=1280, height=720, highlightthickness=0):
        super().__init__(master)
        
        # --- Load & resize images ---
        imagem_fundo         = tk.PhotoImage(file='images/imagemfundo0.png')
        arquivo_nivel_de_dificuldade = Image.open(r"images/NivelDeDificuldade.png").resize((300, 20), Image.LANCZOS)
        imagem_nivel_de_dificuldade = ImageTk.PhotoImage(arquivo_nivel_de_dificuldade)
        arquivo_alternativa = Image.open(r"images/Alternativa.png").resize((330, 62), Image.LANCZOS)
        imagem_alternativa = ImageTk.PhotoImage(arquivo_alternativa)
        
        # --- Create canvas and draw background & title ---
        self.pack(fill="both", expand=True)
        self.create_image(0, 0, image= imagem_fundo, anchor=tk.NW)
        self.create_image(1000,20, image=imagem_nivel_de_dificuldade, anchor='n')
        self.create_image(380,280, image=imagem_alternativa, anchor='n')
        self.create_image(880,280, image=imagem_alternativa, anchor='n')
        self.create_image(880,380, image=imagem_alternativa, anchor='n')
        self.create_image(380,380, image=imagem_alternativa, anchor='n')
        self.create_image(630,480, image=imagem_alternativa, anchor='n')


        # --- Draw difficulty level text ---
        self.create_text(
            1250, 17,                      # Posição no topo à direita
            text="FÁCIL",                  # Texto
            font=("IM FELL ENGLISH SC", 18, "bold"),  # Fonte grande e em negrito
            fill="green",                  # Cor do texto
            anchor='ne'                    # Alinhado no topo-direita
        )
          # --- Enunciado da Questão ---
        enunciado_texto = "QUAL FOI O OBJETIVO DO TRATADO DE VERSALHES?"
        font_enunciado = ("IM FELL ENGLISH SC", 32, "bold") # Ajuste a fonte e o tamanho conforme sua preferência
        enunciado_color = "darkred" # Uma cor que se assemelha ao do seu print

        # Coordenadas para o enunciado:
        # X: Metade da largura do canvas para centralizar horizontalmente
        enunciado_x = width / 2
        # Y: Estime a posição vertical. Na sua imagem, parece estar a cerca de 180-200 pixels do topo.
        enunciado_y = 190 # Ajuste este valor (190px do topo)

        self.create_text(
            enunciado_x, enunciado_y,
            text=enunciado_texto,
            font=font_enunciado,
            fill=enunciado_color,
            anchor='center' # Centraliza o texto no ponto (enunciado_x, enunciado_y)
        )

         # --- "QUESTÃO 1" ---
        questao_texto = "QUESTÃO 1"
        font_questao = ("Arial", 18, "bold")
        questao_color = "darkred"

        questao_x = 50
        questao_y = 35

        self.create_text(
            questao_x, questao_y,
            text=questao_texto,
            font=font_questao,
            fill=questao_color,
            anchor='nw')
        
        botao_ajuda = self.create_text(
        640, 660,                     # Aproximadamente centro inferior (largura 1280 / 2, e altura quase no final)
        text="PEDIR AJUDA ?",        
        font=("IM FELL ENGLISH SC", 30, "bold"),  # Fonte destacada
        fill="black",
        anchor='center'               # Centralizado
)


        # --- Keep references to prevent GC ---
        master.fundo = imagem_fundo
        master.nivel = imagem_nivel_de_dificuldade
        master.alternativa = imagem_alternativa 
     