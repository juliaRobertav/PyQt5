import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
import random


class Jokenpo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pedra, Papel e Tesoura")
        self.setGeometry(200, 200, 300, 200)

        self.label = QLabel("Escolha uma opção:")
        self.label.setFont(QFont("Arial", 12))

        self.btnPedra = QPushButton("Pedra")
        self.btnPapel = QPushButton("Papel")
        self.btnTesoura = QPushButton("Tesoura")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btnPedra)
        layout.addWidget(self.btnPapel)
        layout.addWidget(self.btnTesoura)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.btnPedra.clicked.connect(self.pedra)
        self.btnPapel.clicked.connect(self.papel)
        self.btnTesoura.clicked.connect(self.tesoura)

    def pedra(self):
        self.jogo("pedra")

    def papel(self):
        self.jogo("papel")

    def tesoura(self):
        self.jogo("tesoura")

    def jogo(self, escolha):
        choices = ["pedra", "papel", "tesoura"]
        jogada = random.choice(choices)

        result = self.resultado(escolha, jogada)

        self.label.setText(f"Você escolheu: {escolha}\n"
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Jokenpo()
    game.show()
    sys.exit(app.exec_())

