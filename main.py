import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QLineEdit
from PyQt5 import QtGui


class Janela(QMainWindow):  # Herança
    def __init__(self):
        super().__init__()  # Chamando o construtor da classe mãe (QMainWindow)
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = " Primeira Janela "

        botao1 = QPushButton('Ligar', self)
        botao1.move(100, 100)  # posição dentro da janela
        botao1.resize(150, 50)
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Desligar', self)
        botao2.move(300, 100)
        botao2.resize(150, 50)
        botao2.clicked.connect(self.botao2_click)

        self.label1 = QLabel(self)
        self.label1.setText("TEXTO A SER EXIBIDO!")
        self.label1.move(500, 100)
        self.label1.resize(250, 20)
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"blue"}')

        self.imagem = QLabel(self)
        self.imagem.move(100, 200)
        self.imagem.resize(200, 200)
        self.imagem.setScaledContents(True)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(100, 500)
        self.caixa_texto.resize(150, 25)

        self.botao_leitura = QPushButton('LEIA', self)
        self.botao_leitura.move(260, 500)
        self.botao_leitura.resize(150, 25)
        self.botao_leitura.clicked.connect(self.funcao_leitura)

        self.carregar_janela()


    def funcao_leitura(self):
        texto = self.caixa_texto.text()
        self.caixa_texto.setText("")
        self.label1.setText(texto)


    def botao1_click(self):
        print("LIGADO")
        self.label1.setText("LIGADO!")
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"green"}')
        self.imagem.setPixmap(QtGui.QPixmap("on.png"))
        self.botao_leitura.setEnabled(True)


    def botao2_click(self):
        print("DESLIGADO")
        self.label1.setText("DESLIGADO!")
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"red"}')
        self.imagem.setPixmap(QtGui.QPixmap("off.png"))
        self.botao_leitura.setEnabled(False)


    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Janela()
    sys.exit(aplicacao.exec())
    #aplicacao.exec()
