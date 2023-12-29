from PySide6.QtWidgets import QLabel, QGraphicsOpacityEffect, QApplication
from PySide6.QtCore import (
    QPropertyAnimation, QParallelAnimationGroup, QPoint, QTimer)
from PySide6.QtGui import QPixmap


class IconeResposta(QLabel):
    def __init__(self, app: QApplication):
        super(IconeResposta, self).__init__()
        self.icone_resposta_certa = QPixmap('assets/img/resposta_certa.png')
        self.icone_resposta_errada = QPixmap('assets/img/resposta_errada.png')

        self.__mudar_imagem(True)
        self.__duracao_animacao = 600
        self.app = app

        self.animacao_posicao = QPropertyAnimation(self, b"pos")
        self.animacao_posicao.setDuration(self.__duracao_animacao)

        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)
        self.animacao_opacidade = QPropertyAnimation(effect, b"opacity")
        self.animacao_opacidade.setStartValue(1)
        self.animacao_opacidade.setEndValue(0)
        self.animacao_opacidade.setDuration(self.__duracao_animacao)

        self.grupo_animacao = QParallelAnimationGroup()
        self.grupo_animacao.addAnimation(self.animacao_posicao)
        self.grupo_animacao.addAnimation(self.animacao_opacidade)

        self.hide()

    def __mudar_imagem(self, resposta_certa: bool):
        if resposta_certa:
            self.setPixmap(self.icone_resposta_certa)
        else:
            self.setPixmap(self.icone_resposta_errada)

    def mostrar_animacao(self, resposta_certa: bool):
        self.show()
        self.__mudar_imagem(resposta_certa)
        self.grupo_animacao.start()

        QTimer.singleShot(self.__duracao_animacao, self.app, self.hide)

    def atualizar_posicao_animacao(self):
        self.show()
        posicao_final = self.pos()
        posicao_final.setY(self.pos().y() - 240)
        self.animacao_posicao.setEndValue(posicao_final)
        self.animacao_posicao.setStartValue(self.pos())
        self.hide()
