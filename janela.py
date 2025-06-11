import tkinter as tk
from TelaInicial import TelaInicial
import pygame

class Janela():
    def __init__(self):
        # Inicializa o mixer UMA única vez
        pygame.mixer.init()
        pygame.mixer.music.load('Resources/musica.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)   # -1 = loop infinito

        # Janela Tk
        self.janela = tk.Tk()
        self.janela.title('Expedição do Milhão: Histórias e Mapas')
        self.janela.minsize(1280, 720)
        self.janela.maxsize(1280, 720)

        # Primeira tela
        self.tela_atual = TelaInicial(master=self.janela)

    def iniciar_janela(self):
        self.janela.mainloop()

    def mudar_tela(self, tela_nova):
        # Destroi a tela atual
        self.tela_atual.destroy()
        # Instancia a próxima
        self.tela_atual = tela_nova(self.janela)
        # Opcional: pausar ou retomar música conforme a tela
        self._ajusta_musica()

    def _ajusta_musica(self):
        # Exemplo: não tocar na tela de menu inicial
        telas_sem_musica = ['TelaInicialProfessor', 'TelaLoginProfessor', 'TelaCadastroProfessor',
                            'TelaManterAlunos', 'TelaManterTurmas', 'TelaManterPerguntas', 'TelaPrincipalPainel']
        nome = self.tela_atual.__class__.__name__
        if nome in telas_sem_musica:
            pygame.mixer.music.pause()
        else:
            # Se estava pausada, retoma; se já tocando, não reinicia
            pygame.mixer.music.unpause()

# Cria e inicia
janela = Janela()
