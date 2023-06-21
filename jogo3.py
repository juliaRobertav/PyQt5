import sys
import random
from PyQt5 import QtGui, uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel


class Jokenpo(QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui

        self.ui.button.clicked.connect(self.escolha_jogador)

    def escolha_jogador(self):
        escolha = self.ui.line_edit.text().lower()
        self.jogo(escolha)

    def jogo(self, escolha):
        choices = ["pedra", "papel", "tesoura"]
        jogada = random.choice(choices)

        result = self.resultado(escolha, jogada)

        self.ui.label.setText(f"Você escolheu: {escolha}\n"
                              f"O computador escolheu: {jogada}\n"
                              f"Resultado: {result}")


    def resultado(self, escolha, jogada):
        if escolha == jogada:
            return "Empate"
        elif (escolha == "pedra" and jogada == "tesoura") or \
                (escolha == "papel" and jogada == "pedra") or \
                (escolha == "tesoura" and jogada == "papel"):
            return "Você venceu!"
        else:
            return "Você perdeu!"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = uic.loadUi("janelajogo.ui")
    janela = Jokenpo(tela)
    tela.show()
    sys.exit(app.exec_())
