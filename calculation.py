from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import random



class MyWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setup_UI()

	def setup_UI(self):
		
		self.resize(640,480)
		self.setWindowTitle('Calculation')
		# self.window.setTitle('Calculation')
		# self.a = str(random.randint(10,100))
		# self.b = str(random.randint(1,10))
		layout = QHBoxLayout()
		self.text1 = QLabel(self)
		# self.text1.setText(self.a)

		
		self.text2 = QLabel(self)
		# self.text2.setText(random.choice('+-×÷'))
		# self.text2.setText('gogog')
		# self.text3 = QLabel(self.b,self)
		self.text3 = QLabel(self)

		self.set_numbers()

		self.text4 = QLabel('=',self)
		self.text_edit = QLineEdit()
		
		self.btn =QPushButton('判断')
		self.btn.clicked.connect(self.calcute)

		# self.text5 = QLabel('0',self)
		# self.text5.setText(str(self.calcute().goal))
		
		
		

		layout.addWidget(self.text1)
		layout.addWidget(self.text2)
		layout.addWidget(self.text3)
		layout.addWidget(self.text4)
		layout.addWidget(self.text_edit)
		layout.addWidget(self.btn)

		self.setLayout(layout)

	def set_numbers(self):
		a = str(random.randint(10,100))
		b = str(random.randint(1,10))
		self.text1.setText(a)
		self.text2.setText(random.choice('+-×÷'))
		self.text3.setText(b)
		

	def calcute(self):
		
		answer = int(self.text_edit.text())
		num1 = int(self.text1.text())
		num2 = int(self.text3.text())
		

		if self.text2.text() == '+':
			if answer == num1 + num2:
				QMessageBox.information(self,'正确','恭喜你，回答正确！')
				
			else:
				QMessageBox.information(self,'错误','很抱歉，回答错误！')
				
		if self.text2.text() == '-':
			if answer == num1 - num2:
				QMessageBox.information(self,'正确','恭喜你，回答正确！')
			else:
				QMessageBox.information(self,'错误','很抱歉，回答错误！')
		if self.text2.text() == '×':
			if answer == num1 * num2:
				QMessageBox.information(self,'正确','恭喜你，回答正确！')
			else:
				QMessageBox.information(self,'错误','很抱歉，回答错误！')
		if self.text2.text() == '÷':
			if answer == num1 / num2:
				QMessageBox.information(self,'正确','恭喜你，回答正确！')
			else:
				QMessageBox.information(self,'错误','很抱歉，回答错误！')
		self.set_numbers()
		self.text_edit.setText('')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MyWindow()
	win.show()

	sys.exit(app.exec_())