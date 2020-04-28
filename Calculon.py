#!/usr/bin/env/python3

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from math import *

from PyQt5.QtCore import *
from CalculonUi import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #inserting nos
        self.pushButton_0.clicked.connect(lambda:self.lineEdit.insert('0'))
        self.pushButton_1.clicked.connect(lambda:self.lineEdit.insert('1'))
        self.pushButton_2.clicked.connect(lambda: self.lineEdit.insert('2'))
        self.pushButton_3.clicked.connect(lambda:self.lineEdit.insert('3'))
        self.pushButton_4.clicked.connect(lambda: self.lineEdit.insert('4'))
        self.pushButton_5.clicked.connect(lambda: self.lineEdit.insert('5'))
        self.pushButton_6.clicked.connect(lambda: self.lineEdit.insert('6'))
        self.pushButton_7.clicked.connect(lambda: self.lineEdit.insert('7'))
        self.pushButton_8.clicked.connect(lambda: self.lineEdit.insert('8'))
        self.pushButton_9.clicked.connect(lambda: self.lineEdit.insert('9'))

        #inserting operations
        self.pushButton_dot.clicked.connect(lambda: self.lineEdit.insert('.'))
        self.pushButton_add.clicked.connect(lambda: self.lineEdit.insert('+'))
        self.pushButton_sub.clicked.connect(lambda: self.lineEdit.insert('-'))
        self.pushButton_mul.clicked.connect(lambda: self.lineEdit.insert('*'))
        self.pushButton_div.clicked.connect(lambda: self.lineEdit.insert('/'))
        self.pushButton_sin.clicked.connect(lambda: self.lineEdit.insert('sin('))
        self.pushButton_cos.clicked.connect(lambda: self.lineEdit.insert('cos('))
        self.pushButton_tan.clicked.connect(lambda: self.lineEdit.insert('tan('))
        self.pushButton_asin.clicked.connect(lambda: self.lineEdit.insert('asin('))
        self.pushButton_acos.clicked.connect(lambda: self.lineEdit.insert('acos('))
        self.pushButton_atan.clicked.connect(lambda: self.lineEdit.insert('atan('))
        self.pushButton_sinh.clicked.connect(lambda: self.lineEdit.insert('sinh('))
        self.pushButton_cosh.clicked.connect(lambda: self.lineEdit.insert('cosh('))
        self.pushButton_tanh.clicked.connect(lambda: self.lineEdit.insert('tanh('))
        self.pushButton_ln.clicked.connect(lambda: self.lineEdit.insert('log('))
        self.pushButton_log_2.clicked.connect(lambda: self.lineEdit.insert('log10('))
        self.pushButton_sqrt.clicked.connect(lambda: self.lineEdit.insert('sqrt('))
        self.pushButton_mod.clicked.connect(lambda: self.lineEdit.insert('fmod('))
        self.pushButton_abs.clicked.connect(lambda: self.lineEdit.insert('fabs('))
        self.pushButton_ceil.clicked.connect(lambda: self.lineEdit.insert('ceil('))
        self.pushButton_flr.clicked.connect(lambda: self.lineEdit.insert('floor('))
        self.pushButton_fact.clicked.connect(lambda: self.lineEdit.insert('fact('))
        self.pushButton_e.clicked.connect(lambda: self.lineEdit.insert('e'))
        self.pushButton_pow.clicked.connect(lambda: self.lineEdit.insert('**'))
        self.pushButton_pi.clicked.connect(lambda: self.lineEdit.insert('pi'))
        self.pushButton_eql.clicked.connect(lambda: self.evalExp())
        self.pushButton_seql.clicked.connect(lambda: self.evalExp())
        #backspace
        self.pushButton_bs.clicked.connect(lambda: self.lineEdit.backspace())
        self.pushButton_sbs.clicked.connect(lambda: self.lineEdit.backspace())
        self.pushButton_clr.clicked.connect(lambda: self.lineEdit.clear())
        self.pushButton_sclr.clicked.connect(lambda: self.lineEdit.clear())

        #equal -here evalExp is a user defined function
        self.pushButton_2.clicked.connect(lambda: window.evalExp())
        self.pushButton_2.clicked.connect(lambda: window.evalExp())

        #paranthesis

        self.pushButton_ob.clicked.connect(lambda: self.lineEdit.insert('('))
        self.pushButton_cb.clicked.connect(lambda: self.lineEdit.insert(')'))
        self.pushButton_sob.clicked.connect(lambda: self.lineEdit.insert('('))
        self.pushButton_scb.clicked.connect(lambda: self.lineEdit.insert(')'))

        # return pressed means enter key pressed in keyboard..we called to evlExp through keyboard also

        self.lineEdit.returnPressed.connect(lambda: window.evalExp())
    def evalExp(self):
        try:
            exp = self.lineEdit.text()
            self.result = eval(exp)
            #setText()- to replace the display chars
            self.lineEdit.setText(str(self.result))
        except:
            self.lineEdit.setText('SYNTAX  ERROR')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
