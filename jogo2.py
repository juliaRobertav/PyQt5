import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont

class RPSGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pedra, Papel e Tesoura")
        self.setGeometry(200, 200, 300, 200)

        self.label = QLabel("Escolha uma opção:")
        self.label.setFont(QFont("Arial", 12))

        self.button_rock = QPushButton("Pedra")
        self.button_paper = QPushButton("Papel")
        self.button_scissors = QPushButton("Tesoura")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_rock)
        layout.addWidget(self.button_paper)
        layout.addWidget(self.button_scissors)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button_rock.clicked.connect(self.play_rock)
        self.button_paper.clicked.connect(self.play_paper)
        self.button_scissors.clicked.connect(self.play_scissors)

    def play_rock(self):
        self.play("rock")

    def play_paper(self):
        self.play("paper")

    def play_scissors(self):
        self.play("scissors")

    def play(self, player_choice):
        import random

        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        result = self.get_result(player_choice, computer_choice)

        self.label.setText(f"Você escolheu: {player_choice}\n"
                           f"O computador escolheu: {computer_choice}\n"
                           f"Resultado: {result}")

    def get_result(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Empate"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            return "Você venceu!"
        else:
            return "Você perdeu!"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = RPSGame()
    game.show()
    sys.exit(app.exec_())

