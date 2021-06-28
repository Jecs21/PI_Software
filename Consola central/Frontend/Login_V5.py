# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_V5.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):

    def loginCheck(self):

        url = 'http://127.0.0.1:8000/users/' # obter all users
        response = requests.get(url)

        if response.status_code >= 200 and response.status_code <= 299:
            #sucesso
            print('Status code', response.status_code)
            print('Reason', response.reason)
            response_data = response.json()
        else:
            #erros
            print('Status code', response.status_code)
            print('Reason', response.reason)
            print('Reason', response.text)
        
        # processamento dos dados dos users
        Id = len(response_data)*[1]
        Username = len(response_data)*[1]
        Email = len(response_data)*[1]
        Password = len(response_data)*[1]
        array_user = len(response_data)*[1]

        i = 0
        for data in response_data:

            array_user[i] = data
            string = str(data).split(',') # obter cada um dos users

            ########  ID
            ID = string[0].split(':')   # string[0] corresponde ao id e split pra separar 'id' : '1'
            ID = ID[1].split(' ')       # separar o espaço do numero ex: ' 1'
            Id[i] = int(ID[1])          # obter apenas o numero ex: '1' e remover as '' passando para int
            
            ########  USERNAME
            user_name = string[1].split(':')
            user_name = user_name[1].split(' ')
            user_name = user_name[1].split("'")    #remover as ''
            Username[i] = user_name[1]
           
            ########  EMAIL
            email = string[2].split(':')
            email = email[1].split(' ')
            email = email[1].split("'") 
            Email[i] = email[1]
            ########  PASSWORD
            password = string[3].split(':')
            password = password[1].split(' ')
            password = password[1].split("'") 
            Password[i] = password[1]

            i = i + 1
        
        # login validação

        usernamee = str(self.User.text())
        passwordd = str(self.Password.text())

        i=0
        for data in Username:
            if(data == usernamee):
                if(Password[i] == passwordd):
                    print("Password is valid , ", passwordd)
                    print("Username is Valid , ", usernamee)
                    print("home Page , ", usernamee)
                    break
        
                
            i = i + 1
            




    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 700)
        MainWindow.setMaximumSize(QtCore.QSize(500, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 700))
        self.centralwidget.setMaximumSize(QtCore.QSize(500, 700))
        self.centralwidget.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_1.setStyleSheet("border:0")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.verticalLayout.addWidget(self.frame_1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("border:0")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(100, 380, 92, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox::indicator{\n"
"border: 2px solid rgb(136, 138, 133);\n"
"border-radius: 7px;\n"
"width: 15px;\n"
"heigth: 15px;\n"
"background-color: rgb(186, 189, 182);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"border: 2px solid rgb(204, 0, 0);\n"
"background-color: rgbrgb(239, 41, 41);\n"
"}\n"
"")
        self.checkBox.setObjectName("checkBox")
        self.Password = QtWidgets.QLineEdit(self.frame_2)
        self.Password.setEnabled(True)
        self.Password.setGeometry(QtCore.QRect(100, 320, 280, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.Password.setFont(font)
        self.Password.setStyleSheet("QLineEdit{\n"
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
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Avatar = QtWidgets.QFrame(self.frame_2)
        self.Avatar.setGeometry(QtCore.QRect(180, 90, 121, 121))
        self.Avatar.setStyleSheet("background-image: url(:/Avatar/Design/icones/avatar.png);\n"
"border: 2px  solid rgb(239, 41, 41);\n"
"border-radius: 60px;\n"
"")
        self.Avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Avatar.setObjectName("Avatar")
        self.LOGINButton = QtWidgets.QPushButton(self.frame_2)
        self.LOGINButton.setEnabled(True)
        self.LOGINButton.setGeometry(QtCore.QRect(140, 420, 200, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.LOGINButton.setFont(font)
        self.LOGINButton.setStyleSheet("QPushButton{\n"
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
        self.LOGINButton.setObjectName("LOGINButton")
        self.User = QtWidgets.QLineEdit(self.frame_2)
        self.User.setEnabled(True)
        self.User.setGeometry(QtCore.QRect(100, 260, 280, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.User.setFont(font)
        self.User.setStyleSheet("QLineEdit{\n"
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
        self.User.setText("")
        self.User.setObjectName("User")
        self.SignUpButton = QtWidgets.QPushButton(self.frame_2)
        self.SignUpButton.setGeometry(QtCore.QRect(270, 540, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setStyleSheet("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color:rgb(239, 41, 41);\n"
"    \n"
"}")
        self.SignUpButton.setObjectName("SignUpButton")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(100, 540, 161, 20))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
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
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.LOGINButton.clicked.connect(self.loginCheck)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Save User"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.LOGINButton.setText(_translate("MainWindow", "LOGIN"))
        self.User.setPlaceholderText(_translate("MainWindow", "User"))
        self.SignUpButton.setText(_translate("MainWindow", "Sign Up"))
        self.label.setText(_translate("MainWindow", "Don\'t have an Account ?"))
import file_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
