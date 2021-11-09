import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scientific Caluclator")
        self.setFixedSize(300,200)
        self.initUI()
    def initUI(self):
        self.current = ''
        frame = QVBoxLayout()
        self.display = QLineEdit('0')
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        frame.addWidget(self.display)
        grid = QGridLayout()
        grid.setSpacing(5)
        frame.addLayout(grid)
        self.setLayout(frame)
        names = ['Cls','Bck','Close',u"\N{Division Sign}",
                 '7','8','9',u"\N{Multiplication Sign}",
                 '4','5','6','-',
                 '1','2','3','+',
                 '0','00','.','=']

        positions = [(i,j) for i in range(5) for j in range(4)]
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
        elif button_text.text() == '=':
            try:
                if u"\N{Division Sign}" in self.current:
                    self.current = self.current.replace(u"\N{Division Sign}",'/')
                elif u"\N{Multiplication Sign}" in self.current:
                    self.current = self.current.replace(u"\N{Multiplication Sign}","*")
                self.current = str(eval(self.current))
                self.display.setText(self.current)
            except Exception as e :
                QMessageBox.about(self,'Calculator says ','you pass a wrong expression :'+str(e) )
        else:
            self.current +=button_text.text()
            self.display.setText(self.current)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex= Example()
    ex.show()
    sys.exit(app.exec_())