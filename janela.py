import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

def funcao():
    print("TESTE")

if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)

    janela = uic.loadUi('janela.ui')
    janela.label.setText("Clebinho")
    janela.btnLigar.clicked.connect(funcao)

    janela.show()
    sys.exit(aplicacao.exec())