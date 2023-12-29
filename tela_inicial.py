from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (QStackedWidget, QLabel, QPushButton, QLineEdit,
                               QHBoxLayout, QVBoxLayout, QWidget, QCheckBox)
from minha_tela import MinhaTela


class TelaInicial(MinhaTela):
    def __init__(self, parent: QStackedWidget):
        super().__init__(parent)

        layout_tela_inicial = QVBoxLayout()
        layout_tela_inicial.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout_titulo = QHBoxLayout()
        layout_titulo.setObjectName('layoutTitulo')
        layout_titulo.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        titulo_preto = QLabel('Bem vindo(a) ao ')
        titulo_preto.setObjectName('tituloPretoTelaInicial')

        titulo_azul = QLabel('MathMine')
        titulo_azul.setObjectName('tituloAzulTelaInicial')

        layout_titulo.addWidget(titulo_preto)
        layout_titulo.addWidget(titulo_azul)

        layout_nome = QVBoxLayout()
        layout_nome.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        label_nome = QLabel('Digite seu nome:')
        label_nome.setObjectName('labelNome')
        layout_nome.setSpacing(12)

        self.entrada_nome = QLineEdit()
        self.entrada_nome.setObjectName('entradaNome')
        self.entrada_nome.setMaxLength(16)
        self.entrada_nome.returnPressed.connect(self.mudar_tela)

        self.label_alerta = QLabel('Insira um nome válido')
        self.label_alerta.setObjectName('labelAlerta')
        self.label_alerta.hide()

        layout_nome.addWidget(label_nome)
        layout_nome.addWidget(self.entrada_nome)
        layout_nome.addWidget(self.label_alerta)

        layout_container_layout_botoes = QHBoxLayout()
        container_layout_botoes = QWidget()
        # container_layout_botoes.setFixedHeight(108)
        container_layout_botoes.setObjectName('containerLayoutBotoes')
        layout_botoes = QVBoxLayout()
        layout_botoes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.botao_comecar = QPushButton('Começar')
        self.botao_comecar.setObjectName('botaoComecar')
        self.botao_comecar.clicked.connect(self.mudar_tela)

        layout_botao_tutorial = QHBoxLayout()

        self.botao_tutorial = QCheckBox(' Ver tutorial')
        self.botao_tutorial.setObjectName('botaoTutorial')
        self.botao_tutorial.setChecked(True)
        self.botao_tutorial.clicked.connect(self.entrada_nome.setFocus())

        layout_botao_tutorial.addSpacing(184)
        layout_botao_tutorial.addWidget(self.botao_tutorial)
        layout_botao_tutorial.addSpacing(184)

        self.botao_tutorial.setIconSize(QSize(48, 48))
        self.botao_tutorial.setIcon(QIcon(QPixmap('assets/img/tutorial-azul.svg')))

        layout_botoes.addLayout(layout_botao_tutorial)
        layout_botoes.addSpacing(32)
        layout_botoes.addWidget(self.botao_comecar)
        container_layout_botoes.setLayout(layout_botoes)

        layout_container_layout_botoes.addStretch(1)
        layout_container_layout_botoes.addWidget(container_layout_botoes)
        layout_container_layout_botoes.addStretch(1)

        layout_tela_inicial.addStretch(10)
        layout_tela_inicial.addLayout(layout_titulo)
        layout_tela_inicial.addStretch(7)
        layout_tela_inicial.addLayout(layout_nome)
        layout_tela_inicial.addStretch(5)
        layout_tela_inicial.addLayout(layout_container_layout_botoes)
        layout_tela_inicial.addStretch(10)

        self.setLayout(layout_tela_inicial)

    def mudar_tela(self):
        self.entrada_nome.setFocus()

        try:
            self.tela_principal.dados_usuario.nome = self.entrada_nome.text()
        except ValueError:
            self.label_alerta.show()
        else:
            self.label_alerta.hide()
            self.tela_principal.ir_para_tela('TelaJogo', self.botao_tutorial.isChecked())
            self.botao_tutorial.setChecked(False)

        self.entrada_nome.clear()
