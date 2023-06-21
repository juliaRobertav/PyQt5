from PyQt5 import QtWidgets
from janela_convertida import Ui_MainWindow
import sys


class Janela(Ui_MainWindow):
    def __init__(self, janelinha):
        super().setupUi(janelinha)
        self.btnLigar.clicked.connect(self.ligado)


    def ligado(self):
        print("TESTE")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    janelinha = QtWidgets.QMainWindow()
    j = Janela(janelinha)
    janelinha.show()

    sys.exit(app.exec_())
