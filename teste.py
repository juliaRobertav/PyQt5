import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5 import uic
from random import randint


class Jokenpo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.line_edit = None
        self.button = None
        self.label_resultado = None
        self.iniciar_jogo()

    def iniciar_jogo(self):
        tela = uic.loadUi("janelajogo.ui")
        self.line_edit = tela.findChild(QLineEdit, "lineEdit")
        self.button = tela.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.atualizar_escolha)
        self.label_resultado = tela.findChild(QLabel, "labelResultado")
        tela.show()

    def atualizar_escolha(self):
        escolha = int(self.line_edit.text())
        self.jogada(escolha)

    def jogada(self, escolha):
        opcoes = ["pedra", "papel", "tesoura"]
        jogada = randint(0, 2)

        resultado = ""
        resultado += f"Sua escolha: {opcoes[escolha]}\n"
        resultado += f"Jogada: {opcoes[jogada]}\n"
        resultado += "-=" * 11 + "\n"

        if jogada == 0:
            if escolha == 0:
                resultado += "EMPATE"
            elif escolha == 1:
                resultado += "GANHOU"
            elif escolha == 2:
                resultado += "PERDEU"
        elif jogada == 1:
            if escolha == 0:
                resultado += "GANHOU"
            elif escolha == 1:
                resultado += "EMPATE"
            elif escolha == 2:
                resultado += "PERDEU"
        elif jogada == 2:
            if escolha == 0:
                resultado += "PERDEU"
            elif escolha == 1:
                resultado += "GANHOU"
            elif escolha == 2:
                resultado += "EMPATE"

        self.label_resultado.setText(resultado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jokenpo = Jokenpo()
    sys.exit(app.exec_())
