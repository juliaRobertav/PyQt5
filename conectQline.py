import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.line_edit = QLineEdit()
        self.button = QPushButton("Clique aqui")

        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        text = self.line_edit.text()
        print("Texto inserido:", text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

