import math
import sys
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("공학용 계산기")
        self.setFixedSize(400,300)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('calc.png'))
        self.current = ''
        frame = QVBoxLayout()
        self.display = QLineEdit('0')
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(20)
        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        frame.addWidget(self.display)
        grid = QGridLayout()
        grid.setSpacing(7)
        frame.addLayout(grid)
        self.setLayout(frame)
        names = ['Cls','Bck','Close',u"\N{Division Sign}",
                 '7','8','9',u"\N{Multiplication Sign}",
                 '4','5','6','-',
                 '1','2','3','+',
                 '0','00','.','=',
                 'ln','sqrt(x)','x!','x^2',
                 'log','I/x','|x|','exp']

        positions = [(i,j) for i in range(7) for j in range(4)]
        for position,name in zip(positions,names):
            if name == '':
                continue
            button = QPushButton(name)
            button.resize(10,10)
            button.clicked.connect(self.press_btn)
            grid.addWidget(button,*position)

    def press_btn(self):
        button_text = self.sender()
        if button_text.text() == 'Cls':
            self.current = ''
            self.display.setText(self.current)
        elif button_text.text() == 'Bck':
            self.current = self.current[:-1]
            self.display.setText(self.current)
        elif button_text.text() == 'Close':
            self.close()
        elif button_text.text() == 'ln' :
            self.current = self.current.strip('ln')
            self.current = float(self.current)
            self.current = math.log(self.current)
            self.current = str(self.current)
            self.display.setText(self.current)
        elif button_text.text() == 'sqrt(x)' :
            self.current = self.current.strip('sqrt(x)')
            self.current = float(self.current)
            self.current = math.sqrt(self.current)
            self.current = str(self.current)
            self.display.setText(self.current)
        elif button_text.text() == 'x!' :
            self.current = self.current.strip('x!')
            self.current = float(self.current)
            self.current = math.factorial(self.current)
            self.current = str(self.current)
            self.display.setText(self.current)
        elif button_text.text() == 'x^2' :
            self.current = self.current.strip('x^2')
            self.current = float(self.current)
            self.current = math.pow(self.current,2)
            self.current = str(self.current)
            self.display.setText(self.current)
        elif button_text.text() == 'log' :
            self.current = self.current.strip('log')
            self.current = float(self.current)
            self.current = math.log10(self.current)
            self.current = str(self.current)
            self.display.setText(self.current)
        elif button_text.text()=='I/x' :
            self.current = self.current.strip('I/x')
            self.current = float(self.current)
            self.current = np.reciprocal(self.current)
            self.current = str(self.current)
            self.display.setText(self.current)
        elif button_text.text()=='|x|' :
            self.current = self.current.strip('|x|')
            self.current = float(self.current)
            self.current = abs(self.current)
            self.current = str(self.current)
            self.display.setText(self.current)
        elif button_text.text()=='exp' :
            self.current = self.current.strip('exp')
            self.current = float(self.current)
            self.current = math.exp(self.current)
            self.current = str(self.current)
            self.display.setText(self.current)
        elif button_text.text() == '=' :
            try:
                if u"\N{Division Sign}" in self.current:
                    self.current = self.current.replace(u"\N{Division Sign}",'/')
                elif u"\N{Multiplication Sign}" in self.current:
                    self.current = self.current.replace(u"\N{Multiplication Sign}","*")
                self.current = str(eval(self.current))
                self.display.setText(self.current)
            except Exception as e :
                QMessageBox.about(self,'Error!','잘못 된 문장입니다.')
        else:
            self.current +=button_text.text()
            self.display.setText(self.current)

            ''' elif button_text.text() == 'log' or 'sqrt(x)' or 'x!' or 'x^2' :
            try:
                if 'log' in self.current:
                    self.current = self.current.replace('log',"")
                    self.current = str(eval(math.log(self.current)))
                elif 'sqrt(x)' in self.current:
                    self.current = self.current.replace('sqrt(x)',"")
                    self.current = math.sqrt(self.current)
                elif 'x!' in self.current:
                    self.current = self.current.replace('x!',"")
                    self.current = math.factorial(self.current)
                elif 'x^2' in self.current:
                    self.current = self.current.replace('x^2',"")
                    self.current = self.current*self.current
            except Exception as e :
                QMessageBox.about(self,'Error!','잘못 된 문장입니다.') '''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex= Calc()
    ex.show()
    sys.exit(app.exec_())