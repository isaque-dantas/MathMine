from PySide6.QtWidgets import QStackedWidget, QApplication

from tela_inicial import TelaInicial
from tela_jogo import TelaJogo
from tela_final import TelaFinal
from dados_usuario import DadosUsuario
from trilha_sonora import TrilhaSonora

from pygame import init, mixer


class TelaPrincipal(QStackedWidget):
    def __init__(self, app: QApplication):
        super().__init__()
        self.setWindowTitle("MathMine - quiz interativo de álgebra elementar")

        self.app = app

        self.dados_usuario = DadosUsuario()

        self.addWidget(TelaInicial(self))
        self.addWidget(TelaJogo(self))
        self.addWidget(TelaFinal(self))

        self.index_telas = {
            'TelaInicial': 0,
            'TelaJogo': 1,
            'TelaFinal': 2
        }

        init()
        mixer.init()
        self.som_whoosh = mixer.Sound('assets/audio/whoosh.mp3')
        self.som_whoosh.set_volume(0.4)
        self.som_acerto = mixer.Sound('assets/audio/right.mp3')
        self.som_acerto.set_volume(0.5)
        self.som_erro = mixer.Sound('assets/audio/wrong.mp3')
        self.som_erro.set_volume(0.25)

        self.trilha_sonora_calma = TrilhaSonora("assets/audio/Kirby's Epic Yarn - Quilty Square.mp3",
                                                'trilha_calma', self.app)
        self.trilha_sonora_calma.set_volume(0.9)
        self.trilha_sonora_jogo = TrilhaSonora("assets/audio/Gourmet Race - editado.mp3",
                                               'trilha_jogo', self.app)
        self.trilha_sonora_jogo.set_volume(0.3)

        self.telas_trilhas = {
            'TelaInicial': self.trilha_sonora_calma,
            'TelaJogo': self.trilha_sonora_jogo,
            'TelaFinal': self.trilha_sonora_calma
        }

        self.trilha_inversa = {
            self.trilha_sonora_calma: self.trilha_sonora_jogo,
            self.trilha_sonora_jogo: self.trilha_sonora_calma
        }

        self.ir_para_tela('TelaInicial')
        self.show()

    def ir_para_tela(self, nome_tela_destino: str, ativar_tutorial: bool = False):
        self.som_whoosh.play()

        if nome_tela_destino == 'TelaJogo':
            self.widget(self.index_telas['TelaJogo']).iniciar_tela_jogo(ativar_tutorial)
        elif nome_tela_destino == 'TelaFinal':
            self.widget(self.index_telas['TelaFinal']).atualizar_dados_usuario()

        if nome_tela_destino in ['TelaInicial', 'TelaFinal']:
            self.atualizar_trilha_sonora(nome_tela_destino)

        self.setCurrentIndex(self.index_telas[nome_tela_destino])

    def atualizar_trilha_sonora(self, nome_tela_destino: str):
        trilha = self.telas_trilhas[nome_tela_destino]
        if not trilha.esta_tocando:
            self.trilha_inversa[trilha].parar()
            trilha.tocar()
