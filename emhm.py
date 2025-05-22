import tkinter as tk
import tela

tela_atual = None

def main():
    #  Criar Janela
    janela = tk.Tk()
    janela.title('Expedição do Milhão: Histórias e Mapas')
    janela.minsize(1280, 720)
    janela.maxsize(1280, 720)

    #  Definir imagem de fundo
    arquivo_imagem_fundo = tk.PhotoImage(file='images/imagemfundo0.png')
    imagem_fundo = tk.Label(janela, image = arquivo_imagem_fundo)
    imagem_fundo.place(x = -2, y = -2)

    #  Definir tela_atual aqui:
    tela_atual = tela.MenuPrincipal(janela)

    #  NÃO MEXER NISSO
    janela.mainloop()

if __name__ == "__main__":
    main()
