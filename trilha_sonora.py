import pygame
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication


class TrilhaSonora(pygame.mixer.Sound):
    def __init__(self, filename: str, nome_trilha: str, app: QApplication):
        super(TrilhaSonora, self).__init__(filename)
        self.__nome_trilha = nome_trilha
        self.__app = app
        self.__esta_tocando = False

        self.__delay_trilha = {
            'trilha_calma': 200,
            'trilha_jogo': 500
        }

    def tocar(self):
        QTimer.singleShot(self.__delay_trilha[self.__nome_trilha],
                          self.__app, lambda: self.play(-1))
        self.esta_tocando = True

    def parar(self):
        self.fadeout(self.__delay_trilha[self.__nome_trilha])
        self.esta_tocando = False

    @property
    def esta_tocando(self) -> bool:
        return self.__esta_tocando

    @esta_tocando.setter
    def esta_tocando(self, value: bool):
        self.__esta_tocando = value
