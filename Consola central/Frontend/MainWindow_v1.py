# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 543)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(25, 0, 90);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_1.setStyleSheet("border:0")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Menu = QtWidgets.QFrame(self.frame_1)
        self.Menu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Menu.setStyleSheet("border:o")
        self.Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu.setObjectName("Menu")
        self.MenuButton = QtWidgets.QPushButton(self.Menu)
        self.MenuButton.setGeometry(QtCore.QRect(30, 10, 40, 30))
        self.MenuButton.setMinimumSize(QtCore.QSize(1, 0))
        self.MenuButton.setStyleSheet("QPushButton{\n"
"background-image: url(:/Menu/Design/icones/menu_40x30.png);\n"
"border-radius:2px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:2px;\n"
"    background-color: rgb(114, 159, 207);\n"
"}")
        self.MenuButton.setText("")
        self.MenuButton.setIconSize(QtCore.QSize(20, 20))
        self.MenuButton.setObjectName("MenuButton")
        self.horizontalLayout_2.addWidget(self.Menu)
        self.Title = QtWidgets.QFrame(self.frame_1)
        self.Title.setStyleSheet("border:0")
        self.Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title.setObjectName("Title")
        self.horizontalLayout_2.addWidget(self.Title)
        self.verticalLayout.addWidget(self.frame_1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("border:0")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Left = QtWidgets.QFrame(self.frame_2)
        self.Left.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Left.setStyleSheet("border:0")
        self.Left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Left.setObjectName("Left")
        self.label_2 = QtWidgets.QLabel(self.Left)
        self.label_2.setGeometry(QtCore.QRect(20, 190, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.Left)
        self.Mid = QtWidgets.QFrame(self.frame_2)
        self.Mid.setStyleSheet("border:0")
        self.Mid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mid.setObjectName("Mid")
        self.label = QtWidgets.QLabel(self.Mid)
        self.label.setGeometry(QtCore.QRect(260, 150, 201, 191))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.Mid)
        self.Right = QtWidgets.QFrame(self.frame_2)
        self.Right.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Right.setStyleSheet("border:0")
        self.Right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Right.setObjectName("Right")
        self.label_3 = QtWidgets.QLabel(self.Right)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.Right)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setStyleSheet("border:0")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "LEFT Text "))
        self.label.setText(_translate("MainWindow", "MID INFO"))
        self.label_3.setText(_translate("MainWindow", "Right Text "))
import file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
