from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5 import QtGui, uic
from random import randint


class Jokenpo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.jogo()

        self.imagem = QLabel(self)
        self.imagem.move(400, 200)
        self.imagem.resize(200, 200)
        self.imagem.setScaledContents(True)
        self.imagem.setPixmap(QtGui.QPixmap('pedra.png'))

        self.imagem2 = QLabel(self)
        self.imagem2.move(100, 200)
        self.imagem2.resize(200, 200)
        self.imagem2.setScaledContents(True)
        self.imagem2.setPixmap(QtGui.QPixmap('papel.png'))

        self.imagem3 = QLabel(self)
        self.imagem3.move(90, 200)
        self.imagem3.resize(200, 200)
        self.imagem3.setScaledContents(True)
        self.imagem3.setPixmap(QtGui.QPixmap('tesoura.png'))


    def jogo(self):
        opcoes = ["pedra", "papel", "tesoura"]
        escolha = int(input("Opções:\n"
                            "[0]PEDRA\n"
                            "[1]PAPEL\n"
                            "[2]TESOURA\n"
                            "Qual opção deseja:"))

        jogada = randint(0, 2)

        print('-=' * 11)
        print(f"Sua escolha:{opcoes[escolha]}")
        print(f"Jogada:{opcoes[jogada]}")
        print('-=' * 11)

        if jogada == 0:
            if escolha == 0:
                print("EMPATE")

            elif escolha == 1:
                print("GANHOU")

            elif escolha == 2:
                print("PERDEU")


        elif jogada == 1:
            if escolha == 0:
                print("GANHOU")

            elif escolha == 1:
                print("EMPATE")

            elif escolha == 2:
                print("PERDEU")


        elif jogada == 2:
            if escolha == 0:
                print("PERDEU")

            elif escolha == 1:
                print("GANHOU")

            elif escolha == 2:
                print("EMPATE")


if __name__ == "__main__":
    import sys

    jogo = QApplication(sys.argv)
    tela = uic.loadUi("janelajogo.ui")
    tela.show()
    janela = Jokenpo()
    sys.exit(jogo.exec())
