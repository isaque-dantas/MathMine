from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QWidget, QStackedWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,
    QSizePolicy, QGridLayout)
from PySide6.QtGui import QPixmap, QIcon
from minha_tela import MinhaTela


class TelaFinal(MinhaTela):
    def __init__(self, parent: QStackedWidget):
        super().__init__(parent)
        layout_tela_final = QHBoxLayout()
        layout_tela_final.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__pontuacao_total_usuario = 0
        self.__nome_usuario = ''

        layout_meio = QVBoxLayout()
        layout_meio.setAlignment(Qt.AlignmentFlag.AlignCenter)

        container_titulo = QWidget()
        container_titulo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout_container_titulo = QHBoxLayout()
        layout_container_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        container_layout_titulo = QWidget()
        layout_titulo = QHBoxLayout()
        label_titulo_azul = QLabel('Fim ')
        label_titulo_azul.setObjectName('labelTituloAzul')
        label_titulo_preto = QLabel('de jogo')
        label_titulo_preto.setObjectName('labelTituloPreto')

        label_titulo_azul.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label_titulo_preto.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        container_layout_titulo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout_titulo.addWidget(label_titulo_azul)
        layout_titulo.addWidget(label_titulo_preto)
        container_layout_titulo.setLayout(layout_titulo)
        layout_container_titulo.addWidget(container_layout_titulo)
        container_titulo.setLayout(layout_container_titulo)

        layout_pontuacao_descricao = QHBoxLayout()
        layout_pontuacao_descricao.setSpacing(8)
        layout_pontuacao_descricao.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)

        layout_jogador_descricao_pontuacao = QVBoxLayout()
        layout_descricao_pontuacao = QHBoxLayout()

        self.label_nome_jogador = QLabel(f'<{self.nome_usuario}>')
        self.label_nome_jogador.setObjectName('labelNomeJogador')
        label_descricao_pontuacao_1 = QLabel('Sua')
        label_descricao_pontuacao_1.setObjectName('labelPontuacaoPreta')
        label_descricao_pontuacao_2 = QLabel(' pontuação')
        label_descricao_pontuacao_2.setObjectName('labelPontuacaoLaranja')
        label_descricao_pontuacao_3 = QLabel(' foi de')
        label_descricao_pontuacao_3.setObjectName('labelPontuacaoPreta')

        label_descricao_pontuacao_1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label_descricao_pontuacao_2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label_descricao_pontuacao_3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.label_nome_jogador.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout_descricao_pontuacao.addWidget(label_descricao_pontuacao_1)
        layout_descricao_pontuacao.addWidget(label_descricao_pontuacao_2)
        layout_descricao_pontuacao.addWidget(label_descricao_pontuacao_3)

        layout_jogador_descricao_pontuacao.addWidget(self.label_nome_jogador)
        layout_jogador_descricao_pontuacao.addLayout(layout_descricao_pontuacao)

        layout_pontuacao = QHBoxLayout()
        layout_pontuacao.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter)
        layout_pontuacao.setSpacing(8)

        self.label_pontuacao = QLabel(f' {self.pontuacao_total_usuario}')
        self.label_pontuacao.setObjectName('labelPontuacao')
        moeda = QPixmap('assets/img/moeda-laranja-64px.svg')
        label_moeda = QLabel('')
        label_moeda.setPixmap(moeda)

        self.label_pontuacao.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label_moeda.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout_pontuacao.addWidget(self.label_pontuacao)
        layout_pontuacao.addWidget(label_moeda)

        layout_pontuacao_descricao.addLayout(layout_jogador_descricao_pontuacao)
        layout_pontuacao_descricao.addSpacing(32)
        layout_pontuacao_descricao.addLayout(layout_pontuacao)

        self.botao_inicio = QPushButton('  Voltar ao início')
        self.botao_inicio.setObjectName('botaoInicio')
        self.botao_inicio.setFixedWidth(600)
        self.botao_inicio.clicked.connect(self.mudar_para_tela_inicial)

        self.icone_inicio_amarelo = QIcon(QPixmap('assets/img/home-amarelo.png'))
        self.icone_inicio_branco = QIcon(QPixmap('assets/img/home-branco.png'))
        self.botao_inicio.setIcon(self.icone_inicio_amarelo)
        self.botao_inicio.setIconSize(QSize(48, 48))

        self.botao_inicio.pressed.connect(lambda: self.botao_inicio.setIcon(self.icone_inicio_branco))
        self.botao_inicio.released.connect(lambda: self.botao_inicio.setIcon(self.icone_inicio_amarelo))

        layout_meio.addWidget(container_titulo)
        layout_meio.addSpacing(48)
        layout_meio.addLayout(layout_pontuacao_descricao)
        layout_meio.addSpacing(96)
        layout_meio.addWidget(self.botao_inicio)

        layout_autor = QVBoxLayout()

        label_nome_autor = QLabel('Feito por\nIsaque Dantas')
        label_nome_autor.setObjectName('labelNomeAutor')

        container_redes_sociais_autor = QWidget()
        layout_redes_sociais_autor = QGridLayout()
        layout_redes_sociais_autor.setHorizontalSpacing(24)
        layout_redes_sociais_autor.setVerticalSpacing(56)

        imagens_redes_sociais_autor = ['github.png', 'email.png', 'Discord.svg']
        descricoes_redes_sociais_autor = ['<a href="https://github.com/IsqDantas">@IsqDantas</a>', '<a href="mailto:vicisaque413@gmail.com">vicisaque413<br>@gmail.com</a>', '<a href="discordapp.com/users/isaque_d">@isaque_d</a>']
        for i, (imagem, descricao) in enumerate(zip(imagens_redes_sociais_autor, descricoes_redes_sociais_autor)):
            label_imagem_rede_social = QLabel()
            label_imagem_rede_social.setPixmap(QPixmap(f'assets/img/{imagem}'))
            layout_redes_sociais_autor.addWidget(label_imagem_rede_social, i, 0)

            label_descricao_rede_social = QLabel(descricao)
            label_descricao_rede_social.setObjectName('labelDescricaoRedeSocial')
            layout_redes_sociais_autor.addWidget(label_descricao_rede_social, i, 1)

        container_redes_sociais_autor.setLayout(layout_redes_sociais_autor)
        container_redes_sociais_autor.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout_autor.addWidget(label_nome_autor)
        layout_autor.addWidget(container_redes_sociais_autor)

        layout_tela_final.addStretch(3)
        layout_tela_final.addLayout(layout_meio)
        layout_tela_final.addStretch(1)
        layout_tela_final.addLayout(layout_autor)
        layout_tela_final.addStretch(3)

        self.pontuacao_total_usuario = 2000
        self.setLayout(layout_tela_final)

    def mudar_para_tela_inicial(self):
        self.tela_principal.ir_para_tela('TelaInicial')

    def atualizar_dados_usuario(self):
        self.nome_usuario = self.tela_principal.dados_usuario.nome
        self.pontuacao_total_usuario = self.tela_principal.dados_usuario.pontos

    @property
    def pontuacao_total_usuario(self) -> int:
        return self.__pontuacao_total_usuario

    @pontuacao_total_usuario.setter
    def pontuacao_total_usuario(self, value: int):
        self.__pontuacao_total_usuario = value
        self.label_pontuacao.setText(str(self.__pontuacao_total_usuario))

    @property
    def nome_usuario(self) -> str:
        return self.__nome_usuario

    @nome_usuario.setter
    def nome_usuario(self, value: str):
        self.__nome_usuario = value
        self.label_nome_jogador.setText(str(self.nome_usuario))
