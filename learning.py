from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*

import sys

App = QApplication(sys.argv)


def clear(w):
    name.setText('')
    password.setText('')
    print(name)

w = QMainWindow()
w.setWindowTitle('ادخال بيانات')
w.resize(400,400)
w.move(400,200)

but = QPushButton(w,text='ادخل')
but.resize(80,50)
but.move(150,300)
but.clicked.connect(clear)

name = QLineEdit(w)
name.resize(200,30)
name.move(100,150)
name.setPlaceholderText('اكتب اسمك هنا')


password =QLineEdit(w)
password.resize(200,30)
password.move(100,200)
password.setPlaceholderText('ادخل كلمة المرور')

text =QTextEdit(w)
#text.setText(text.name)





w.show()
App.exec_()