from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import (
    QWidget, QStackedWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout,
    QVBoxLayout, QGridLayout, QSizePolicy)

from minha_tela import MinhaTela
from gerador_equacoes import GeradorEquacoes
from icone_resposta import IconeResposta
from tutorial import Tutorial

from time import time


class TelaJogo(MinhaTela):
    def __init__(self, parent: QStackedWidget):
        super().__init__(parent)

        self.layout_tela_jogo = QHBoxLayout()
        self.layout_tela_jogo.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.__tempo_inicial = 15
        self.__pontos_inciais = 240
        self.__tempo_restante = self.__tempo_inicial
        self.__pontos_desafio = self.__pontos_inciais
        self.__pontos_totais = 0
        self.__numero_desafio = 1
        self.__dificuldade = 1
        self.__tempo_resposta = time()
        self.__counter_bait = 0

        self.timer_pontos = QTimer()
        self.timer_pontos.setInterval(100)
        self.timer_pontos.timeout.connect(self.__atualizar_pontuacao)

        self.timer_tempo_restante = QTimer()
        self.timer_tempo_restante.setInterval(1000)
        self.timer_tempo_restante.timeout.connect(self.__atualizar_tempo_restante)

        layout_botao_retornar = QHBoxLayout()
        icone_retornar = QPixmap('assets/img/seta-esquerda.svg')
        self.botao_retornar = QPushButton(icon=QIcon(icone_retornar), text='')
        self.botao_retornar.setIconSize(QSize(31, 27))
        self.botao_retornar.setObjectName('botaoRetornar')
        self.botao_retornar.clicked.connect(self.__mudar_tela_para_inicio)
        layout_botao_retornar.addWidget(self.botao_retornar)
        layout_botao_retornar.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        layout_botao_avancar = QHBoxLayout()
        icone_retornar = QPixmap('assets/img/seta-direita.svg')
        self.botao_avancar = QPushButton(icon=QIcon(icone_retornar), text='')
        self.botao_avancar.setIconSize(QSize(31, 27))
        self.botao_avancar.setObjectName('botaoAvancar')
        self.botao_avancar.clicked.connect(self.__mudar_tela_para_final)
        layout_botao_avancar.addWidget(self.botao_avancar)
        layout_botao_avancar.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

        self.botao_retornar.blockSignals(True)
        self.botao_avancar.blockSignals(True)

        layout_meio = QVBoxLayout()
        layout_meio.setObjectName('layoutMeio')

        layout_pontos_desafio = QHBoxLayout()
        layout_pontos_desafio.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout_pontos_desafio.setSpacing(40)

        layout_pontos_totais = QHBoxLayout()
        layout_pontos_totais.setSpacing(6)

        container_label_desafio = QWidget()
        container_label_desafio.setObjectName('containerLabelDesafio')
        layout_label_desafio = QHBoxLayout()

        self.label_numero_desafio = QLabel(f'Desafio {self.__numero_desafio}')
        self.label_numero_desafio.setObjectName('labelDesafio')
        layout_label_desafio.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout_label_desafio.addWidget(self.label_numero_desafio)

        self.label_pontos_totais = QLabel(f'{self.__pontos_totais}')
        self.label_pontos_totais.setObjectName('labelPontosTotais')

        container_label_desafio.setFixedWidth(320)
        container_label_desafio.setLayout(layout_label_desafio)
        self.label_pontos_totais.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        icone_pontos = QPixmap('assets/img/moeda-preta.png').scaledToHeight(
            int(self.label_pontos_totais.height() * 0.08),
            Qt.TransformationMode.SmoothTransformation)
        label_icone_pontos = QLabel()
        label_icone_pontos.setPixmap(icone_pontos)

        self.label_dificuldade = QLabel(f'Nível {self.dificuldade}')
        self.label_dificuldade.setObjectName('labelDificuldade')
        self.label_dificuldade.setFixedWidth(320)

        layout_pontos_totais.addWidget(self.label_pontos_totais)
        layout_pontos_totais.addWidget(label_icone_pontos)

        layout_pontos_desafio.addWidget(container_label_desafio)
        layout_pontos_desafio.addLayout(layout_pontos_totais)
        layout_pontos_desafio.addWidget(self.label_dificuldade)

        container_label_equacao = QWidget()
        container_label_equacao.setObjectName('containerLabelEquacao')
        layout_label_equacao = QHBoxLayout()
        layout_label_equacao.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gerador = GeradorEquacoes(self.dificuldade)
        self.__equacao, self.__solucao = self.gerador.gerar_equacao()
        self.label_equacao = QLabel(text=self.__equacao)
        self.label_equacao.setObjectName('labelEquacao')

        layout_label_equacao.addWidget(self.label_equacao)
        container_label_equacao.setLayout(layout_label_equacao)

        layout_equacao = QHBoxLayout()

        container_pontos = QWidget()
        container_pontos.setObjectName('containerPontos')
        container_pontos.setFixedWidth(260)
        layout_pontos = QHBoxLayout()
        layout_pontos.setSpacing(8)
        layout_pontos.setAlignment(Qt.AlignmentFlag.AlignRight)

        seta = QPixmap('assets/img/seta-baixo.svg')
        label_seta = QLabel('')
        label_seta.setPixmap(seta)
        label_seta.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.label_pontos = QLabel(str(self.__pontos_desafio))
        self.label_pontos.setObjectName('labelPontos')
        self.label_pontos.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        moeda = QPixmap('assets/img/moeda-laranja.svg')
        moeda = moeda.scaledToHeight(48)
        label_moeda = QLabel('')
        label_moeda.setPixmap(moeda)
        label_moeda.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        layout_pontos.addWidget(label_seta)
        layout_pontos.addSpacing(8)
        layout_pontos.addWidget(self.label_pontos)
        layout_pontos.addWidget(label_moeda)
        container_pontos.setLayout(layout_pontos)

        self.entrada_equacao = QLineEdit()
        self.entrada_equacao.setObjectName('entradaEquacao')
        self.entrada_equacao.blockSignals(True)
        self.entrada_equacao.returnPressed.connect(self.__tratar_input)
        self.entrada_equacao.setMaxLength(12)
        self.entrada_equacao.setMinimumWidth(128)

        container_tempo = QWidget()
        container_tempo.setObjectName('containerTempo')
        container_tempo.setFixedWidth(260)
        layout_tempo = QHBoxLayout()
        layout_tempo.setSpacing(8)

        self.label_tempo_restante = QLabel(f'{self.__tempo_inicial}s')
        self.label_tempo_restante.setObjectName('labelTempoRestante')

        relogio = QPixmap('assets/img/relogio-menor.svg')
        label_relogio = QLabel('')
        label_relogio.setPixmap(relogio)

        layout_tempo.addWidget(self.label_tempo_restante)
        layout_tempo.addWidget(label_relogio)
        layout_tempo.addStretch(1)
        container_tempo.setLayout(layout_tempo)

        layout_equacao.addWidget(container_pontos)
        layout_equacao.addWidget(self.entrada_equacao)
        layout_equacao.addWidget(container_tempo)

        layout_container_teclado_acertos = QHBoxLayout()
        container_teclado_acertos = QWidget()

        container_teclado = QWidget()
        container_teclado.setObjectName('containerTeclado')
        layout_container_teclado = QHBoxLayout()
        layout_container_teclado.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        container_grid_teclado = QWidget()
        container_grid_teclado.setObjectName('containerGridTeclado')
        container_grid_teclado.setMinimumWidth(16)
        container_grid_teclado.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        grid_teclado = QGridLayout()

        textos_botao_grid = [['1', '2', '3'],
                             ['4', '5', '6'],
                             ['7', '8', '9'],
                             ['-', '0', '=']]

        slots_grid = {
            '0': self.__slot_botao_teclado_0,
            '1': self.__slot_botao_teclado_1,
            '2': self.__slot_botao_teclado_2,
            '3': self.__slot_botao_teclado_3,
            '4': self.__slot_botao_teclado_4,
            '5': self.__slot_botao_teclado_5,
            '6': self.__slot_botao_teclado_6,
            '7': self.__slot_botao_teclado_7,
            '8': self.__slot_botao_teclado_8,
            '9': self.__slot_botao_teclado_9,
            '=': self.__slot_botao_teclado_eq,
            '-': self.__slot_botao_teclado_sub
        }

        for i in range(4):
            for j, texto_botao in enumerate(textos_botao_grid[i]):
                botao_teclado = QPushButton(texto_botao)
                botao_teclado.clicked.connect(slots_grid[texto_botao])
                botao_teclado.setObjectName('botaoGrid')
                botao_teclado.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

                grid_teclado.addWidget(botao_teclado, i, j)

        container_grid_teclado.setLayout(grid_teclado)
        layout_container_teclado.addWidget(container_grid_teclado)
        container_teclado.setLayout(layout_container_teclado)

        self.icone_resposta_esquerda = IconeResposta(self.tela_principal.app)
        self.icone_resposta_direita = IconeResposta(self.tela_principal.app)

        container_icone_resposta_esquerda = QWidget()
        container_icone_resposta_esquerda.setMaximumWidth(260)
        container_icone_resposta_esquerda.setObjectName('containerIconeRespostaEsquerda')

        layout_container_icone_resposta_esquerda = QVBoxLayout()
        layout_container_icone_resposta_esquerda.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        layout_container_icone_resposta_esquerda.addWidget(self.icone_resposta_esquerda)
        container_icone_resposta_esquerda.setLayout(layout_container_icone_resposta_esquerda)

        container_icone_resposta_direita = QWidget()
        container_icone_resposta_direita.setMaximumWidth(260)
        container_icone_resposta_direita.setObjectName('containerIconeRespostaDireita')

        layout_container_icone_resposta_direita = QVBoxLayout()
        layout_container_icone_resposta_direita.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        layout_container_icone_resposta_direita.addWidget(self.icone_resposta_direita)
        container_icone_resposta_direita.setLayout(layout_container_icone_resposta_direita)

        layout_container_teclado_acertos.addWidget(container_icone_resposta_esquerda)
        layout_container_teclado_acertos.addWidget(container_teclado)
        layout_container_teclado_acertos.addWidget(container_icone_resposta_direita)

        container_teclado_acertos.setLayout(layout_container_teclado_acertos)

        layout_meio.setSpacing(72)
        layout_meio.addSpacing(24)
        layout_meio.addLayout(layout_pontos_desafio)
        layout_meio.addWidget(container_label_equacao)
        layout_meio.addLayout(layout_equacao)
        layout_meio.addWidget(container_teclado_acertos)

        container_layout_tutorial_esquerda = QWidget()
        container_layout_tutorial_esquerda.setObjectName('containerLayoutTutorialEsquerda')
        container_layout_tutorial_direita = QWidget()
        container_layout_tutorial_direita.setObjectName('containerLayoutTutorialDireita')

        self.layout_tutorial_esquerda = QVBoxLayout()
        self.layout_tutorial_esquerda.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout_tutorial_direita = QVBoxLayout()
        self.layout_tutorial_direita.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.tutorial = Tutorial(self)
        self.card_tutorial = self.tutorial.card_atual
        self.layout_tutorial_esquerda.addWidget(self.card_tutorial)

        container_layout_tutorial_esquerda.setLayout(self.layout_tutorial_esquerda)
        container_layout_tutorial_direita.setLayout(self.layout_tutorial_direita)

        self.layout_tela_jogo.addLayout(layout_botao_retornar)
        self.layout_tela_jogo.addWidget(container_layout_tutorial_esquerda)
        self.layout_tela_jogo.addLayout(layout_meio)
        self.layout_tela_jogo.addWidget(container_layout_tutorial_direita)
        self.layout_tela_jogo.addLayout(layout_botao_avancar)

        self.layout_tela_jogo.setStretch(2, 4)

        self.setLayout(self.layout_tela_jogo)

    def __tratar_input(self):
        resposta_certa = self.__verificar_resposta()

        if self.__verificar_spam(resposta_certa):
            return None
        else:
            self.__tempo_resposta = time()

        self.__dar_feedback_resposta(resposta_certa)

        if resposta_certa:
            self.__aumentar_pontuacao()
            self.tempo_restante += 10
            self.__mudar_desafio()
            self.pontos_desafio = self.__pontos_inciais
        else:
            self.__diminuir_pontuacao()
            self.__diminuir_tempo_restante()

        self.entrada_equacao.clear()

    def __verificar_resposta(self):
        try:
            return eval(self.entrada_equacao.text().replace(',', '.')) == float(self.__solucao)
        except ValueError:
            return None
        except:
            return self.entrada_equacao.text() == '' and self.__solucao is None

    def __verificar_spam(self, resposta_certa):
        if resposta_certa:
            self.__counter_bait = 0
            return False

        if time() - self.__tempo_resposta < 0.75:
            return True
        elif resposta_certa is None:
            return True
        if self.entrada_equacao.text() == '' or resposta_certa is None:
            self.__counter_bait += 1
            if self.__counter_bait >= 3:
                return True

        return False

    def __dar_feedback_resposta(self, resposta_certa: bool):
        self.__tocar_som(resposta_certa)
        self.__mostrar_animacao(resposta_certa)

    def __aumentar_pontuacao(self):
        self.pontos_totais += self.pontos_desafio

    def __diminuir_pontuacao(self):
        self.pontos_totais -= int(0.75 * self.pontos_desafio)

    def __diminuir_tempo_restante(self):
        self.tempo_restante -= 2
        self.__animacao_label_tempo_restante()

    def __animacao_label_tempo_restante(self):
        for i in range(4):
            if i % 2:
                QTimer.singleShot(i * 100, self.tela_principal.app,
                                  lambda: self.label_tempo_restante.setStyleSheet('color: #1D3AA0'))
            else:
                QTimer.singleShot(i * 100, self.tela_principal.app,
                                  lambda: self.label_tempo_restante.setStyleSheet('color: #E08E45'))

    def __resetar_timers(self):
        self.__resetar_tempo_restante()
        self.__resetar_pontos_desafio()

    def __parar_timers(self):
        self.timer_pontos.stop()
        self.timer_tempo_restante.stop()

    def atualizar_posicoes_animacoes(self):
        self.icone_resposta_esquerda.atualizar_posicao_animacao()
        self.icone_resposta_direita.atualizar_posicao_animacao()

    def iniciar_jogo(self):
        self.botao_retornar.blockSignals(False)
        self.botao_avancar.blockSignals(False)
        self.entrada_equacao.blockSignals(False)
        self.__iniciar_timers()

    def __iniciar_timers(self):
        self.timer_pontos.start()
        self.timer_tempo_restante.start()

    def iniciar_tela_jogo(self, ativar_tutorial: bool):
        if not ativar_tutorial:
            self.tela_principal.atualizar_trilha_sonora('TelaJogo')
            QTimer.singleShot(3600, self.tela_principal.app, self.iniciar_jogo)
            QTimer.singleShot(50, self.tela_principal.app, self.atualizar_posicoes_animacoes)
            self.entrada_equacao.setFocus()
        else:
            self.tutorial.iniciar_tutorial()

    def __mudar_tela(self, tela: str):
        self.tela_principal.dados_usuario.pontos = self.pontos_totais
        self.__resetar_componentes()
        self.__parar_timers()

        self.entrada_equacao.blockSignals(True)
        self.botao_retornar.blockSignals(True)
        self.botao_avancar.blockSignals(True)
        self.tela_principal.ir_para_tela(tela)

    def __mudar_tela_para_inicio(self):
        self.__mudar_tela('TelaInicial')

    def __mudar_tela_para_final(self):
        self.__mudar_tela('TelaFinal')

    def __atualizar_tempo_restante(self):
        self.tempo_restante -= 1

        if self.tempo_restante == 0:
            self.__mudar_tela_para_final()

    def __atualizar_pontuacao(self):
        self.pontos_desafio -= 2

    def __mudar_desafio(self):
        self.numero_desafio += 1

        if self.numero_desafio % 6 == 0:
            self.dificuldade += 1
            self.gerador = GeradorEquacoes(self.dificuldade)

        self.__mudar_equacao()

    def __resetar_componentes(self):
        self.numero_desafio = 1
        self.dificuldade = 1
        self.pontos_totais = 0
        self.gerador = GeradorEquacoes(self.dificuldade)

        self.__resetar_timers()
        self.__mudar_equacao()
        self.entrada_equacao.clear()

    def __tocar_som(self, resposta_certa: bool):
        if resposta_certa:
            self.tela_principal.som_acerto.play()
        else:
            self.tela_principal.som_erro.play()

    def __mostrar_animacao(self, resposta_certa: bool):
        self.icone_resposta_direita.mostrar_animacao(resposta_certa)
        self.icone_resposta_esquerda.mostrar_animacao(resposta_certa)

    def __mudar_equacao(self):
        self.__equacao, self.__solucao = self.gerador.gerar_equacao()
        self.label_equacao.setText(self.__equacao)

    @property
    def numero_desafio(self):
        return self.__numero_desafio

    @numero_desafio.setter
    def numero_desafio(self, novo_valor):
        self.__numero_desafio = novo_valor
        if self.__numero_desafio < 0:
            self.__numero_desafio = 0
        self.label_numero_desafio.setText(f'Desafio {self.__numero_desafio}')

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, novo_valor):
        self.__dificuldade = novo_valor
        self.label_dificuldade.setText(f'Nível {self.dificuldade}')

    @property
    def tempo_restante(self):
        return self.__tempo_restante

    @tempo_restante.setter
    def tempo_restante(self, novo_valor):
        self.__tempo_restante = novo_valor
        if self.__tempo_restante < 0:
            self.__tempo_restante = 0
        elif self.__tempo_restante > self.__tempo_inicial + 5:
            self.__tempo_restante = self.__tempo_inicial + 5
        self.label_tempo_restante.setText(f'{self.__tempo_restante}s')

    @property
    def pontos_totais(self):
        return self.__pontos_totais

    @pontos_totais.setter
    def pontos_totais(self, novo_valor):
        self.__pontos_totais = novo_valor
        if self.__pontos_totais < 0:
            self.__pontos_totais = 0
        self.label_pontos_totais.setText(f'{self.__pontos_totais}')

    @property
    def pontos_desafio(self):
        return self.__pontos_desafio

    @pontos_desafio.setter
    def pontos_desafio(self, novo_valor):
        self.__pontos_desafio = novo_valor
        if self.__pontos_desafio < 10:
            self.__pontos_desafio = 10
        self.label_pontos.setText(f'{self.pontos_desafio}')

    def __resetar_pontos_desafio(self):
        self.pontos_desafio = self.__pontos_inciais

    def __resetar_tempo_restante(self):
        self.tempo_restante = self.__tempo_inicial

    def __slot_botao_teclado(self, caractere_botao_grid: str):
        self.entrada_equacao.setText(self.entrada_equacao.text() + caractere_botao_grid)
        self.entrada_equacao.setFocus()

    def __slot_botao_teclado_1(self):
        self.__slot_botao_teclado('1')

    def __slot_botao_teclado_2(self):
        self.__slot_botao_teclado('2')

    def __slot_botao_teclado_3(self):
        self.__slot_botao_teclado('3')

    def __slot_botao_teclado_4(self):
        self.__slot_botao_teclado('4')

    def __slot_botao_teclado_5(self):
        self.__slot_botao_teclado('5')

    def __slot_botao_teclado_6(self):
        self.__slot_botao_teclado('6')

    def __slot_botao_teclado_7(self):
        self.__slot_botao_teclado('7')

    def __slot_botao_teclado_8(self):
        self.__slot_botao_teclado('8')

    def __slot_botao_teclado_9(self):
        self.__slot_botao_teclado('9')

    def __slot_botao_teclado_0(self):
        self.__slot_botao_teclado('0')

    def __slot_botao_teclado_eq(self):
        self.__tratar_input()

    def __slot_botao_teclado_sub(self):
        self.__slot_botao_teclado('-')
