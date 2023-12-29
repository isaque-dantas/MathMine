from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy)
from PySide6.QtCore import Qt


class CardTutorial(QWidget):
    def __init__(self, titulo: str, descricao: str, lado: int, posicao_y: int, animacao):
        super(CardTutorial, self).__init__()
        self.__titulo = titulo
        self.__descricao = descricao
        self.__lado = lado
        self.__posicao_y = posicao_y
        self.__animacao = animacao

        self.setObjectName('cardTutorial')

        max_width = 260
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setMaximumWidth(max_width)
        self.setContentsMargins(0, self.__posicao_y, 0, 0)
        layout_card = QVBoxLayout()

        layout_seta = QHBoxLayout()

        lado_seta = {
            0: 'assets/img/seta-direita-card.svg',
            1: 'assets/img/seta-esquerda-card.svg'
        }

        alinhamento_layout_seta = {
            0: Qt.AlignmentFlag.AlignRight,
            1: Qt.AlignmentFlag.AlignLeft
        }

        layout_seta.setAlignment(alinhamento_layout_seta[lado])
        imagem_seta = QPixmap(lado_seta[lado])

        label_seta = QLabel('')
        label_seta.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label_seta.setPixmap(imagem_seta)

        layout_seta.addWidget(label_seta)
        layout_seta.insertStretch(self.__lado, 1)

        self.label_titulo = QLabel(self.__titulo)
        self.label_titulo.setObjectName('labelTituloCard')
        self.label_titulo.setWordWrap(True)
        self.label_titulo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.label_descricao = QLabel(self.__descricao)
        self.label_descricao.setObjectName('labelDescricaoCard')
        self.label_descricao.setFixedWidth(max_width - 8)
        self.label_descricao.setWordWrap(True)
        self.label_descricao.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout_botoes = QHBoxLayout()

        self.botao_fechar = QPushButton('Fechar')
        self.botao_fechar.setObjectName('botaoFecharCard')
        self.botao_fechar.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.botao_fechar.clicked.connect(self.__animacao.parar_tutorial)

        self.botao_proximo = QPushButton('Próximo')
        self.botao_proximo.setObjectName('botaoProximoCard')
        self.botao_proximo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.botao_proximo.clicked.connect(self.__animacao.avancar_card)

        layout_botoes.addStretch(1)
        layout_botoes.addWidget(self.botao_fechar)
        layout_botoes.addSpacing(16)
        layout_botoes.addWidget(self.botao_proximo)

        layout_card.addLayout(layout_seta)
        layout_card.addSpacing(4)
        layout_card.addWidget(self.label_titulo)
        layout_card.addWidget(self.label_descricao)
        layout_card.addSpacing(32)
        layout_card.addLayout(layout_botoes)

        self.setLayout(layout_card)

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, value):
        self.__lado = value