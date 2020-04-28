# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculon.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 583)
        MainWindow.setMinimumSize(QtCore.QSize(424, 583))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/pinpng.com-butterfree-png-6856905.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow\n"
"{\n"
"    background:black;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 90))
        font = QtGui.QFont()
        font.setFamily("Scientific Calculator LCD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setStyleSheet("background-color: rgb(32, 110, 59);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(True)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setStyleSheet("    border:none;\n"
"    background-color:rgb(46, 52, 54);\n"
"    color:white;\n"
"    font: 10pt \"DejaVu Sans Mono\";")
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabSt = QtWidgets.QWidget()
        self.tabSt.setObjectName("tabSt")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabSt)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_2.addWidget(self.pushButton_1, 3, 0, 1, 1)
        self.pushButton_add = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_add.setFlat(False)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout_2.addWidget(self.pushButton_add, 4, 3, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout_2.addWidget(self.pushButton_0, 4, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 2, 1, 1, 1)
        self.pushButton_sub = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sub.sizePolicy().hasHeightForWidth())
        self.pushButton_sub.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.gridLayout_2.addWidget(self.pushButton_sub, 3, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 2, 2, 1, 1)
        self.pushButton_eql = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_eql.sizePolicy().hasHeightForWidth())
        self.pushButton_eql.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_eql.setFont(font)
        self.pushButton_eql.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_eql.setObjectName("pushButton_eql")
        self.gridLayout_2.addWidget(self.pushButton_eql, 4, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.pushButton_dot = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_dot.sizePolicy().hasHeightForWidth())
        self.pushButton_dot.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.gridLayout_2.addWidget(self.pushButton_dot, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_div = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_div.sizePolicy().hasHeightForWidth())
        self.pushButton_div.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_div.setObjectName("pushButton_div")
        self.gridLayout_2.addWidget(self.pushButton_div, 1, 3, 1, 1)
        self.pushButton_mul = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_mul.sizePolicy().hasHeightForWidth())
        self.pushButton_mul.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_mul.setFont(font)
        self.pushButton_mul.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_mul.setObjectName("pushButton_mul")
        self.gridLayout_2.addWidget(self.pushButton_mul, 2, 3, 1, 1)
        self.pushButton_bs = QtWidgets.QPushButton(self.tabSt)
        self.pushButton_bs.setMinimumSize(QtCore.QSize(0, 65))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_bs.setFont(font)
        self.pushButton_bs.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:rgb(209, 44, 44);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 10pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(214, 81, 81);\n"
"    color:black;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_bs.setObjectName("pushButton_bs")
        self.gridLayout_2.addWidget(self.pushButton_bs, 0, 3, 1, 1)
        self.pushButton_clr = QtWidgets.QPushButton(self.tabSt)
        self.pushButton_clr.setMinimumSize(QtCore.QSize(0, 65))
        self.pushButton_clr.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_clr.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_clr.setFont(font)
        self.pushButton_clr.setAutoFillBackground(False)
        self.pushButton_clr.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_clr.setObjectName("pushButton_clr")
        self.gridLayout_2.addWidget(self.pushButton_clr, 0, 2, 1, 1)
        self.pushButton_cb = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cb.sizePolicy().hasHeightForWidth())
        self.pushButton_cb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_cb.setFont(font)
        self.pushButton_cb.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_cb.setObjectName("pushButton_cb")
        self.gridLayout_2.addWidget(self.pushButton_cb, 0, 1, 1, 1)
        self.pushButton_ob = QtWidgets.QPushButton(self.tabSt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ob.sizePolicy().hasHeightForWidth())
        self.pushButton_ob.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_ob.setFont(font)
        self.pushButton_ob.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_ob.setObjectName("pushButton_ob")
        self.gridLayout_2.addWidget(self.pushButton_ob, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.tabWidget_2.addTab(self.tabSt, "")
        self.tabSc = QtWidgets.QWidget()
        self.tabSc.setObjectName("tabSc")
        self.gridLayout = QtWidgets.QGridLayout(self.tabSc)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_sclr = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sclr.sizePolicy().hasHeightForWidth())
        self.pushButton_sclr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sclr.setFont(font)
        self.pushButton_sclr.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:rgb(209, 44, 44);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 10pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(214, 81, 81);\n"
"    color:black;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_sclr.setObjectName("pushButton_sclr")
        self.gridLayout.addWidget(self.pushButton_sclr, 0, 0, 1, 2)
        self.pushButton_sbs = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sbs.sizePolicy().hasHeightForWidth())
        self.pushButton_sbs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sbs.setFont(font)
        self.pushButton_sbs.setStyleSheet("QPushButton \n"
"{\n"
"    background-color:rgb(209, 44, 44);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 10pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    background-color:rgb(214, 81, 81);\n"
"    color:black;\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_sbs.setObjectName("pushButton_sbs")
        self.gridLayout.addWidget(self.pushButton_sbs, 0, 2, 1, 2)
        self.pushButton_sin = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sin.sizePolicy().hasHeightForWidth())
        self.pushButton_sin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sin.setFont(font)
        self.pushButton_sin.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.gridLayout.addWidget(self.pushButton_sin, 1, 0, 1, 1)
        self.pushButton_cos = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cos.sizePolicy().hasHeightForWidth())
        self.pushButton_cos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_cos.setFont(font)
        self.pushButton_cos.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.gridLayout.addWidget(self.pushButton_cos, 1, 1, 1, 1)
        self.pushButton_tan = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_tan.sizePolicy().hasHeightForWidth())
        self.pushButton_tan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_tan.setFont(font)
        self.pushButton_tan.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_tan.setObjectName("pushButton_tan")
        self.gridLayout.addWidget(self.pushButton_tan, 1, 2, 1, 1)
        self.pushButton_pi = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_pi.sizePolicy().hasHeightForWidth())
        self.pushButton_pi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_pi.setFont(font)
        self.pushButton_pi.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_pi.setObjectName("pushButton_pi")
        self.gridLayout.addWidget(self.pushButton_pi, 1, 3, 1, 1)
        self.pushButton_asin = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_asin.sizePolicy().hasHeightForWidth())
        self.pushButton_asin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_asin.setFont(font)
        self.pushButton_asin.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_asin.setObjectName("pushButton_asin")
        self.gridLayout.addWidget(self.pushButton_asin, 2, 0, 1, 1)
        self.pushButton_acos = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_acos.sizePolicy().hasHeightForWidth())
        self.pushButton_acos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_acos.setFont(font)
        self.pushButton_acos.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_acos.setObjectName("pushButton_acos")
        self.gridLayout.addWidget(self.pushButton_acos, 2, 1, 1, 1)
        self.pushButton_atan = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_atan.sizePolicy().hasHeightForWidth())
        self.pushButton_atan.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_atan.setFont(font)
        self.pushButton_atan.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_atan.setObjectName("pushButton_atan")
        self.gridLayout.addWidget(self.pushButton_atan, 2, 2, 1, 1)
        self.pushButton_e = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_e.sizePolicy().hasHeightForWidth())
        self.pushButton_e.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_e.setFont(font)
        self.pushButton_e.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_e.setObjectName("pushButton_e")
        self.gridLayout.addWidget(self.pushButton_e, 2, 3, 1, 1)
        self.pushButton_sinh = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sinh.sizePolicy().hasHeightForWidth())
        self.pushButton_sinh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sinh.setFont(font)
        self.pushButton_sinh.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_sinh.setObjectName("pushButton_sinh")
        self.gridLayout.addWidget(self.pushButton_sinh, 3, 0, 1, 1)
        self.pushButton_cosh = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cosh.sizePolicy().hasHeightForWidth())
        self.pushButton_cosh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_cosh.setFont(font)
        self.pushButton_cosh.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_cosh.setObjectName("pushButton_cosh")
        self.gridLayout.addWidget(self.pushButton_cosh, 3, 1, 1, 1)
        self.pushButton_tanh = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_tanh.sizePolicy().hasHeightForWidth())
        self.pushButton_tanh.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_tanh.setFont(font)
        self.pushButton_tanh.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_tanh.setObjectName("pushButton_tanh")
        self.gridLayout.addWidget(self.pushButton_tanh, 3, 2, 1, 1)
        self.pushButton_pow = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_pow.sizePolicy().hasHeightForWidth())
        self.pushButton_pow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_pow.setFont(font)
        self.pushButton_pow.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_pow.setObjectName("pushButton_pow")
        self.gridLayout.addWidget(self.pushButton_pow, 3, 3, 1, 1)
        self.pushButton_ln = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ln.sizePolicy().hasHeightForWidth())
        self.pushButton_ln.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_ln.setFont(font)
        self.pushButton_ln.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_ln.setObjectName("pushButton_ln")
        self.gridLayout.addWidget(self.pushButton_ln, 4, 0, 1, 1)
        self.pushButton_log_2 = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_log_2.sizePolicy().hasHeightForWidth())
        self.pushButton_log_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_log_2.setFont(font)
        self.pushButton_log_2.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_log_2.setObjectName("pushButton_log_2")
        self.gridLayout.addWidget(self.pushButton_log_2, 4, 1, 1, 1)
        self.pushButton_sqrt = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sqrt.sizePolicy().hasHeightForWidth())
        self.pushButton_sqrt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sqrt.setFont(font)
        self.pushButton_sqrt.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.gridLayout.addWidget(self.pushButton_sqrt, 4, 2, 1, 1)
        self.pushButton_fact = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_fact.sizePolicy().hasHeightForWidth())
        self.pushButton_fact.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_fact.setFont(font)
        self.pushButton_fact.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_fact.setObjectName("pushButton_fact")
        self.gridLayout.addWidget(self.pushButton_fact, 4, 3, 1, 1)
        self.pushButton_sob = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_sob.sizePolicy().hasHeightForWidth())
        self.pushButton_sob.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sob.setFont(font)
        self.pushButton_sob.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_sob.setObjectName("pushButton_sob")
        self.gridLayout.addWidget(self.pushButton_sob, 5, 0, 1, 1)
        self.pushButton_scb = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_scb.sizePolicy().hasHeightForWidth())
        self.pushButton_scb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_scb.setFont(font)
        self.pushButton_scb.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_scb.setObjectName("pushButton_scb")
        self.gridLayout.addWidget(self.pushButton_scb, 5, 1, 1, 1)
        self.pushButton_flr = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_flr.sizePolicy().hasHeightForWidth())
        self.pushButton_flr.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_flr.setFont(font)
        self.pushButton_flr.setStyleSheet("QPushButton{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_flr.setObjectName("pushButton_flr")
        self.gridLayout.addWidget(self.pushButton_flr, 5, 2, 1, 1)
        self.pushButton_ceil = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_ceil.sizePolicy().hasHeightForWidth())
        self.pushButton_ceil.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_ceil.setFont(font)
        self.pushButton_ceil.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_ceil.setObjectName("pushButton_ceil")
        self.gridLayout.addWidget(self.pushButton_ceil, 5, 3, 1, 1)
        self.pushButton_mod = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_mod.sizePolicy().hasHeightForWidth())
        self.pushButton_mod.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_mod.setFont(font)
        self.pushButton_mod.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_mod.setObjectName("pushButton_mod")
        self.gridLayout.addWidget(self.pushButton_mod, 6, 0, 1, 1)
        self.pushButton_abs = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_abs.sizePolicy().hasHeightForWidth())
        self.pushButton_abs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_abs.setFont(font)
        self.pushButton_abs.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_abs.setObjectName("pushButton_abs")
        self.gridLayout.addWidget(self.pushButton_abs, 6, 1, 1, 1)
        self.pushButton_seql = QtWidgets.QPushButton(self.tabSc)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_seql.sizePolicy().hasHeightForWidth())
        self.pushButton_seql.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_seql.setFont(font)
        self.pushButton_seql.setStyleSheet("QPushButton{\n"
"    background-color:rgb(32, 74, 135);\n"
"    color:white;\n"
"    border:none;\n"
"    \n"
"    font: 12pt \"DejaVu Sans\";\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color:rgb(114, 159, 207);\n"
"    color:black;\n"
"    border:none;\n"
"}")
        self.pushButton_seql.setObjectName("pushButton_seql")
        self.gridLayout.addWidget(self.pushButton_seql, 6, 2, 1, 2)
        self.tabWidget_2.addTab(self.tabSc, "")
        self.horizontalLayout.addWidget(self.tabWidget_2)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.pushButton_clr.pressed.connect(self.lineEdit.clear)
        self.pushButton_sclr.pressed.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculan"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_add.setText(_translate("MainWindow", "+"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_sub.setText(_translate("MainWindow", "-"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_eql.setText(_translate("MainWindow", "="))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_dot.setText(_translate("MainWindow", "."))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_mul.setText(_translate("MainWindow", "X"))
        self.pushButton_bs.setText(_translate("MainWindow", "⌫"))
        self.pushButton_clr.setText(_translate("MainWindow", "Clear"))
        self.pushButton_cb.setText(_translate("MainWindow", ")"))
        self.pushButton_ob.setText(_translate("MainWindow", "("))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabSt), _translate("MainWindow", "Standard"))
        self.pushButton_sclr.setText(_translate("MainWindow", "Clear"))
        self.pushButton_sbs.setText(_translate("MainWindow", "⌫"))
        self.pushButton_sin.setText(_translate("MainWindow", "sin"))
        self.pushButton_cos.setText(_translate("MainWindow", "cos"))
        self.pushButton_tan.setText(_translate("MainWindow", "tan"))
        self.pushButton_pi.setText(_translate("MainWindow", "π"))
        self.pushButton_asin.setText(_translate("MainWindow", "asin"))
        self.pushButton_acos.setText(_translate("MainWindow", "acos"))
        self.pushButton_atan.setText(_translate("MainWindow", "atan"))
        self.pushButton_e.setText(_translate("MainWindow", "e"))
        self.pushButton_sinh.setText(_translate("MainWindow", "sinh"))
        self.pushButton_cosh.setText(_translate("MainWindow", "cosh"))
        self.pushButton_tanh.setText(_translate("MainWindow", "tanh"))
        self.pushButton_pow.setText(_translate("MainWindow", "^"))
        self.pushButton_ln.setText(_translate("MainWindow", "ln"))
        self.pushButton_log_2.setText(_translate("MainWindow", "log"))
        self.pushButton_sqrt.setText(_translate("MainWindow", "sqrt"))
        self.pushButton_fact.setText(_translate("MainWindow", "fact"))
        self.pushButton_sob.setText(_translate("MainWindow", "("))
        self.pushButton_scb.setText(_translate("MainWindow", ")"))
        self.pushButton_flr.setText(_translate("MainWindow", "floor"))
        self.pushButton_ceil.setText(_translate("MainWindow", "ceil"))
        self.pushButton_mod.setText(_translate("MainWindow", "mod"))
        self.pushButton_abs.setText(_translate("MainWindow", "abs"))
        self.pushButton_seql.setText(_translate("MainWindow", "="))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabSc), _translate("MainWindow", "Scientific"))

