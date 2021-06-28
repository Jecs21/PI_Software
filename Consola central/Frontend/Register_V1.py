# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register_V1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 700))
        self.centralwidget.setMaximumSize(QtCore.QSize(500, 700))
        self.centralwidget.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setGeometry(QtCore.QRect(10, -2, 482, 40))
        self.frame_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_1.setStyleSheet("border:0")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.BacktoLOGIN = QtWidgets.QPushButton(self.frame_1)
        self.BacktoLOGIN.setGeometry(QtCore.QRect(0, 0, 50, 40))
        self.BacktoLOGIN.setStyleSheet("background-image: url(:/LeftArrow/Design/icones/left-arrow_1_50x40.png);")
        self.BacktoLOGIN.setText("")
        self.BacktoLOGIN.setObjectName("BacktoLOGIN")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 44, 482, 590))
        self.frame_2.setStyleSheet("border:0")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.NewPassword = QtWidgets.QLineEdit(self.frame_2)
        self.NewPassword.setEnabled(True)
        self.NewPassword.setGeometry(QtCore.QRect(100, 220, 280, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.NewPassword.setFont(font)
        self.NewPassword.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(122, 6, 6);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(239, 41, 41);\n"
"color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.NewPassword.setText("")
        self.NewPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPassword.setObjectName("NewPassword")
        self.REGISTERButton = QtWidgets.QPushButton(self.frame_2)
        self.REGISTERButton.setEnabled(True)
        self.REGISTERButton.setGeometry(QtCore.QRect(140, 510, 200, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.REGISTERButton.setFont(font)
        self.REGISTERButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(46, 52, 54);\n"
"    border: 2px solid rgb(239, 41, 41);\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgb(239, 41, 41);\n"
"    border: 2px solid rgb(239, 41, 41);\n"
"}")
        self.REGISTERButton.setObjectName("REGISTERButton")
        self.New_Username = QtWidgets.QLineEdit(self.frame_2)
        self.New_Username.setEnabled(True)
        self.New_Username.setGeometry(QtCore.QRect(100, 120, 280, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.New_Username.setFont(font)
        self.New_Username.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(122, 6, 6);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(239, 41, 41);\n"
"color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.New_Username.setText("")
        self.New_Username.setObjectName("New_Username")
        self.NewAccount = QtWidgets.QLabel(self.frame_2)
        self.NewAccount.setGeometry(QtCore.QRect(170, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.NewAccount.setFont(font)
        self.NewAccount.setStyleSheet("color: rgb(255, 255, 255);")
        self.NewAccount.setObjectName("NewAccount")
        self.Username = QtWidgets.QLabel(self.frame_2)
        self.Username.setGeometry(QtCore.QRect(130, 90, 71, 19))
        self.Username.setStyleSheet("color:rgb(186, 189, 182)")
        self.Username.setObjectName("Username")
        self.Password = QtWidgets.QLabel(self.frame_2)
        self.Password.setGeometry(QtCore.QRect(130, 190, 67, 19))
        self.Password.setStyleSheet("color:rgb(186, 189, 182)")
        self.Password.setObjectName("Password")
        self.ConfirmPassord = QtWidgets.QLabel(self.frame_2)
        self.ConfirmPassord.setGeometry(QtCore.QRect(130, 290, 131, 19))
        self.ConfirmPassord.setStyleSheet("color:rgb(186, 189, 182)")
        self.ConfirmPassord.setObjectName("ConfirmPassord")
        self.ConfirmPassword = QtWidgets.QLineEdit(self.frame_2)
        self.ConfirmPassword.setEnabled(True)
        self.ConfirmPassword.setGeometry(QtCore.QRect(100, 320, 280, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.ConfirmPassword.setFont(font)
        self.ConfirmPassword.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(122, 6, 6);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(239, 41, 41);\n"
"color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.ConfirmPassword.setText("")
        self.ConfirmPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ConfirmPassword.setObjectName("ConfirmPassword")
        self.Email = QtWidgets.QLabel(self.frame_2)
        self.Email.setGeometry(QtCore.QRect(130, 390, 131, 19))
        self.Email.setStyleSheet("color:rgb(186, 189, 182)")
        self.Email.setObjectName("Email")
        self.email = QtWidgets.QLineEdit(self.frame_2)
        self.email.setEnabled(True)
        self.email.setGeometry(QtCore.QRect(100, 420, 280, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.email.setFont(font)
        self.email.setStyleSheet("QLineEdit{\n"
"border: 2px solid rgb(45,45,45);\n"
"border-radius: 5px;\n"
"padding: 15px;\n"
"background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(122, 6, 6);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"border: 2px solid rgb(239, 41, 41);\n"
"color: rgb(200, 200, 200);\n"
"}\n"
"")
        self.email.setText("")
        self.email.setObjectName("email")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(100, 190, 21, 21))
        self.frame.setStyleSheet("background-image: url(:/PadLock/Design/icones/padlock_21x21.png);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(100, 290, 21, 21))
        self.frame_4.setStyleSheet("background-image: url(:/PadLock/Design/icones/padlock_21x21.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setGeometry(QtCore.QRect(100, 90, 21, 21))
        self.frame_5.setStyleSheet("\n"
"background-image: url(:/Username/Design/icones/user_21x21.png);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setGeometry(QtCore.QRect(100, 390, 21, 21))
        self.frame_6.setStyleSheet("background-image: url(:/email/Design/icones/envelope_21x21.png)")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(10, 640, 482, 40))
        self.frame_3.setMinimumSize(QtCore.QSize(35, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_3.setStyleSheet("border:0")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Logo = QtWidgets.QFrame(self.frame_3)
        self.Logo.setGeometry(QtCore.QRect(160, 0, 150, 40))
        self.Logo.setMaximumSize(QtCore.QSize(150, 40))
        self.Logo.setStyleSheet("background-image: url(:/Bosh/Design/icones/bosch-logo_2_150x40.png);\n"
"\n"
"border-radius: 5px")
        self.Logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Logo.setObjectName("Logo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.NewPassword.setPlaceholderText(_translate("MainWindow", "New Password"))
        self.REGISTERButton.setText(_translate("MainWindow", "REGISTER"))
        self.New_Username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.NewAccount.setText(_translate("MainWindow", "Sign Up"))
        self.Username.setText(_translate("MainWindow", "Username"))
        self.Password.setText(_translate("MainWindow", "Password"))
        self.ConfirmPassord.setText(_translate("MainWindow", "Confirm Password"))
        self.ConfirmPassword.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.Email.setText(_translate("MainWindow", "Email"))
        self.email.setPlaceholderText(_translate("MainWindow", "example@example.com"))
import file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
