from card_tutorial import CardTutorial
from PySide6.QtWidgets import QSpacerItem, QSizePolicy


class Tutorial:
    def __init__(self, tela_jogo):
        self.__cards = [
            CardTutorial('Status do jogo',
                         'Aqui ficam as informações do status: desafio, pontuação total e nível de dificuldade.\n\nA dificuldade aumenta a cada cinco desafios, e a cada vez a equação se torna mais difícil de resolver.\n\nA sua pontuação total será mostrada ao final do programa.',
                         0, 30, self),
            CardTutorial('Equação-desafio',
                         'Essa é uma equação com números e operações gerados aleatoriamente. Ou seja, as equações são diferentes a cada vez que você joga. Quanto maior o nível, mais complexa ela será.',
                         0, 200, self),
            CardTutorial('Status do desafio',
                         'São: a quantidade de pontos ganhos por desafio, o espaço para resposta, e o tempo restante. Lembre-se: quanto mais rápido você responder, mais pontos você ganha!',
                         1, 376, self),
            CardTutorial('Status do desafio',
                         'A resposta pode ser em fração (1/2) ou decimal (0.5; 0,5; .5; ,5). Se a equação não tiver uma resposta possível, não digite nada. Para enviar a resposta, clique no botão “=” ou digite Enter.',
                         1, 376, self),
            CardTutorial('Status do desafio',
                         'A cada vez que você errar, perderá 75% dos pontos em laranja, e dois segundos do tempo. Se acertar, ganhará os pontos em laranja, e dez segundos de tempo.',
                         1, 376, self)
        ]

        self.__index_card_atual = 0
        self.card_atual = self.__cards[self.__index_card_atual]
        self.card_atual.hide()

        self.__tela_jogo = tela_jogo
        self.lado_layout = {
            0: self.__tela_jogo.layout_tutorial_esquerda,
            1: self.__tela_jogo.layout_tutorial_direita,
        }

        self.card_spacer = QSpacerItem(self.card_atual.maximumWidth(), 10, QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.__tela_jogo.layout_tutorial_esquerda.addItem(self.card_spacer)
        self.__tela_jogo.layout_tutorial_direita.addItem(self.card_spacer)

    def avancar_card(self):
        print('Avançando card...')
        lado_card_anterior = self.card_atual.lado
        self.card_atual.hide()

        try:
            self.mudar_card_atual()
        except IndexError:
            self.parar_tutorial()
        else:
            self.card_atual.show()
            self.mudar_lado_card(lado_card_anterior, self.card_atual.lado)

    def parar_tutorial(self):
        print('Parando tutorial')
        self.card_atual.hide()
        self.lado_layout[self.card_atual.lado].addItem(self.card_spacer)
        self.resetar_tutorial()
        self.__tela_jogo.iniciar_tela_jogo(False)

    def resetar_tutorial(self):
        print('Resetando tutorial')
        self.__index_card_atual = 0
        self.card_atual = self.__cards[self.__index_card_atual]
        self.card_atual.hide()

    def iniciar_tutorial(self):
        print('iniciar')
        self.lado_layout[self.card_atual.lado].removeItem(self.card_spacer)
        self.card_atual.show()

    def mudar_card_atual(self):
        self.__index_card_atual += 1
        self.card_atual = self.__cards[self.__index_card_atual]

    def mudar_lado_card(self, lado_partida: int, lado_chegada: int):
        self.lado_layout[lado_chegada].addWidget(self.card_atual)

        if lado_partida != lado_chegada:
            self.lado_layout[lado_chegada].removeItem(self.card_spacer)
            self.lado_layout[lado_partida].addItem(self.card_spacer)

    @property
    def card_atual(self) -> CardTutorial:
        return self.__card_atual

    @card_atual.setter
    def card_atual(self, value: CardTutorial):
        self.__card_atual = value
