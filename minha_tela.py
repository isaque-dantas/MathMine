from PySide6.QtWidgets import QStackedWidget, QWidget


class MinhaTela(QWidget):
    def __init__(self, tela_principal: QStackedWidget):
        super().__init__()
        self.tela_principal = tela_principal
