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
        MainWindow.resize(1015, 645)
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
        self.Menu.setMaximumSize(QtCore.QSize(55, 16777215))
        self.Menu.setStyleSheet("border:o;\n"
"background-color: rgb(46, 52, 54);")
        self.Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu.setObjectName("Menu")
        self.MenuButton = QtWidgets.QPushButton(self.Menu)
        self.MenuButton.setGeometry(QtCore.QRect(10, 10, 40, 30))
        self.MenuButton.setMinimumSize(QtCore.QSize(1, 0))
        self.MenuButton.setStyleSheet("QPushButton{\n"
"background-image: url(:/Menu/Design/icones/menu_40x30.png);\n"
"border-radius:2px;\n"
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
        self.Left.setMinimumSize(QtCore.QSize(55, 0))
        self.Left.setMaximumSize(QtCore.QSize(55, 16777215))
        self.Left.setStyleSheet("border:0 ; \n"
"background-color: rgb(46, 52, 54);")
        self.Left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Left.setObjectName("Left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Left)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TOP_BUTTON = QtWidgets.QFrame(self.Left)
        self.TOP_BUTTON.setMaximumSize(QtCore.QSize(150, 16777215))
        self.TOP_BUTTON.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TOP_BUTTON.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TOP_BUTTON.setObjectName("TOP_BUTTON")
        self.Home = QtWidgets.QPushButton(self.TOP_BUTTON)
        self.Home.setGeometry(QtCore.QRect(0, 120, 130, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Home.setFont(font)
        self.Home.setStyleSheet("QPushButton{\n"
"     \n"
"    border-radius: 10px;\n"
"    background-repeat:none;\n"
"    background-image: url(:/Menu/Design/icones/home-icon-silhouette_1_50x50.png);\n"
"    padding-left: 50px; \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"}")
        self.Home.setObjectName("Home")
        self.NewUnidade = QtWidgets.QPushButton(self.TOP_BUTTON)
        self.NewUnidade.setGeometry(QtCore.QRect(0, 270, 130, 60))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.NewUnidade.setFont(font)
        self.NewUnidade.setStyleSheet("QPushButton{\n"
"    padding: 5px 7px; \n"
"    border-radius: 10px;\n"
"    background-color: rgb(85, 87, 83);\n"
"    color: rgb(255, 255, 255);\n"
"    background-repeat:none;\n"
"    background-image: url(:/Menu/Design/icones/plus_50x50.png);\n"
"    background-position: center left;\n"
"    padding-left: 50px; \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"}")
        self.NewUnidade.setFlat(False)
        self.NewUnidade.setObjectName("NewUnidade")
        self.verticalLayout_2.addWidget(self.TOP_BUTTON)
        self.Account = QtWidgets.QPushButton(self.Left)
        self.Account.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Account.setFont(font)
        self.Account.setStyleSheet("QPushButton{\n"
"    padding: 5px 7px; \n"
"    border-radius: 10px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-repeat:none;\n"
"    \n"
"    background-image: url(:/Menu/Design/icones/pngfind.com-man-head-silhouette-png-6227673_50x50.png);\n"
"\n"
"    background-position: center left;\n"
"    padding-left: 54px; \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"}")
        self.Account.setObjectName("Account")
        self.verticalLayout_2.addWidget(self.Account)
        self.Settings = QtWidgets.QPushButton(self.Left)
        self.Settings.setMinimumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Settings.setFont(font)
        self.Settings.setStyleSheet("QPushButton{\n"
"    padding: 5px 7px; \n"
"    border-radius: 10px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-repeat:none;\n"
"    \n"
"    background-image: url(:/Menu/Design/icones/settings_50x50.png);\n"
"    background-position: center left;\n"
"    padding-left: 55px; \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(114, 159, 207);\n"
"}")
        self.Settings.setObjectName("Settings")
        self.verticalLayout_2.addWidget(self.Settings)
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
        self.frame_3.setStyleSheet("border:0;\n"
"background-color: rgb(46, 52, 54);")
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
        self.Home.setText(_translate("MainWindow", "Home"))
        self.NewUnidade.setText(_translate("MainWindow", "Add"))
        self.Account.setText(_translate("MainWindow", "Account"))
        self.Settings.setText(_translate("MainWindow", "Settings"))
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
