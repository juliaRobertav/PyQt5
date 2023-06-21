import sys
import random
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton, QLabel


class Jokenpo(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Escolha uma opção:")
        self.label.setFont(QFont("Arial", 12))

        layout = QVBoxLayout()

        self.line_edit = QLineEdit()
        self.button = QPushButton("JOGAR")

        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button.clicked.connect(self.escolha_jogador)

    def escolha_jogador(self):
        escolha = self.line_edit.text().lower()
        self.jogo(escolha)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Jokenpo()
    janela.show()
    sys.exit(app.exec_())
