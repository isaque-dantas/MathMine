import sys
from PySide6.QtWidgets import QApplication

from tela_principal import TelaPrincipal
from pathlib import Path

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())

    tela_principal = TelaPrincipal(app)

    sys.exit(app.exec())
