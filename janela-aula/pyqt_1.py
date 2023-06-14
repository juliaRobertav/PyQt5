import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui


class Janela(QMainWindow):  # Herança
	def __init__(self):
		super().__init__()  # Chamando o construtor da classe mãe(QMainWindow)
		self.topo = 100
		self.esquerda = 100
		self.largura = 800
		self.altura = 600
		self.titulo = " Primeira Janela"

		botao1 = QPushButton('Lua', self)
		botao1.move(100, 100)  # posição dentro da janela
		botao1.resize(150, 50)  # atributo

		botao2 = QPushButton('Sol', self)
		botao2.move(300, 100)
		botao2.resize(150, 50)

		botao1.clicked.connect(self.botao1_click)
		botao2.clicked.connect(self.botao2_click)

		self.label1 = QLabel(self)
		self.label1.setText("INSIRA UM TEXTO")
		self.label1.move(500, 100)
		self.label1.resize(250, 20)
		# set:importante para passar o texto, etc...

		self.imagem = QLabel(self)
		self.imagem.move(400, 200)
		self.imagem.resize(200, 200)
		self.imagem.setScaledContents(True)
		self.imagem.setPixmap(QtGui.QPixmap('sol.jfif'))

		self.imagem2 = QLabel(self)
		self.imagem2.move(100, 200)
		self.imagem2.resize(200, 200)
		self.imagem2.setScaledContents(True)
		self.imagem2.setPixmap(QtGui.QPixmap('lua2.jfif'))

		self.caixa_texto = QLineEdit(self)
		self.caixa_texto.move(100, 500)
		self.caixa_texto.resize(150, 25)

		botao_leitura = QPushButton("LEIA", self)
		botao_leitura.move(260, 500)
		botao_leitura.resize(150, 25)
		botao_leitura.clicked.connect(self.botao_leitura)

		self.carregar_janela()

	# o botão deve ser criado antes de chamar a janela

	def botao_leitura(self):
		texto = self.caixa_texto.text()
		self.caixa_texto.setText("")
		self.label1.setText((texto))

	def carregar_janela(self):
		self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
		self.setWindowTitle(self.titulo)
		self.show()

	def botao1_click(self):
		# print("LIGADO!")
		self.label1.setText("Lua")
		self.label1.setStyleSheet('QLabel {font:monospace;font-size:20px;color: "fuchsia"}')
		self.imagem.setPixmap(QtGui.QPixmap('lua2.jfif'))

	def botao2_click(self):
		# print("DESLIGADO!")
		self.label1.setText("Sol")
		self.label1.setStyleSheet('QLabel {font:monospace;font-size:20px;color: "purple"}')
		self.imagem.setPixmap(QtGui.QPixmap('sol.jfif'))


if __name__ == "__main__":
	aplicacao = QApplication(sys.argv)
	j = Janela()
	sys.exit(aplicacao.exec())
# aplicacao.exec()
