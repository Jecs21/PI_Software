from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QSize, endl
from PyQt5.QtWidgets import QApplication, QFrame, QMainWindow
from PyQt5.uic import loadUi
import sys
import os
from PyQt5.uic.uiparser import QtCore
import file_rc
import requests

import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time

from PyQt5.QtGui import QFont, QIcon, QPainter, QPixmap, QColor
from PyQt5.QtCore import Qt, QMargins, QTranslator, QLocale, QLibraryInfo, QEvent,QSize
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QSizePolicy,
                             QGridLayout, QLabel, QColorDialog, QComboBox, QCheckBox,
                             QPushButton, QFileDialog, QMessageBox)

#############################################################################################################
#################################### Global Variables #######################################################
#############################################################################################################
global global_Unidade_id_for_table_layout
global_Unidade_id_for_table_layout = -1

global flag_delay
flag_delay = 0

global press
press = ""

global consola_id
consola_id = -1

global email_global
email_global = ""

global username_global
username_global = ""

global x
x = 0  

global data_sensor
data_sensor = []

global pressUnidade_global
pressUnidade_global = -1

global data_id
data_id = []

#############################################################################################################
#################################### Login Window ###########################################################
#############################################################################################################

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow,self).__init__() 
        loadUi("Login.ui",self)
        self.SignUpButton.clicked.connect(self.GotoRegister)
        self.LOGINButton.clicked.connect(self.loginCheck)
        self.Error.setHidden(True)
        global x
        x=2
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxAAAAAAAAAAAAAAAAAAAAAAAA",x) 
        
    def GotoRegister(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.Error.setHidden(True)    
    
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
                    global consola_id
                    consola_id = Id[i]
                    global username_global
                    username_global = usernamee
                    global email_global
                    email_global = Email[i]

                    print("Password is valid , ", passwordd)
                    print("Username is Valid , ", usernamee)
                    
                    widget.setCurrentIndex(widget.currentIndex()+2) #+2 to main
                    widget.showFullScreen()
                    self.Error.setHidden(True)
                    break
                else:
                    self.Error.setHidden(False)
            else:
                self.Error.setHidden(False)
               
            i = i + 1
#############################################################################################################
#################################### Register Window ########################################################
#############################################################################################################

class RegisterWindow(QMainWindow):

    def __init__(self):
        super(RegisterWindow,self).__init__() 
        loadUi("Register_V1.ui",self)
        self.BacktoLOGIN.clicked.connect(self.GotoLogin)
        self.REGISTERButton.clicked.connect(self.registerCheck)
        global x
        x = 2
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxAAAAAAAAAAAAAAAAAAAAAAAA",x) 

    def GotoLogin(self):
        widget.setCurrentIndex(widget.currentIndex()-1) 

    def registerCheck(self):
        
        url = 'http://127.0.0.1:8000/users/'
        
        if self.NewPassword.text() != self.ConfirmPassword.text(): 
            print("Password is  , ", self.NewPassword.text())
            print(" Diferent Password is  , ", self.ConfirmPassword.text())
            
        else:
        
            users_data = {
                "username": str(self.New_Username.text()),
                "email": str(self.email.text()),
                "password": str(self.NewPassword.text())
            }

            response = requests.post(url, json=users_data)

            if response.status_code >= 200 and response.status_code <= 299:
                #sucesso
                print('Status code', response.status_code)
                print('Reason', response.reason)
                response_data = response.json()
                print(response_data)
            else:
                #erros
                print('Status code', response.status_code)
                print('Reason', response.reason)
                print('Reason', response.text)
            
            #### Register consola
            url = 'http://127.0.0.1:8000/consolas/'
            
            users_data = {
                "Consola_client": self.loginCheck()
            }

            response = requests.post(url, json=users_data)

            if response.status_code >= 200 and response.status_code <= 299:
                #sucesso
                print('Status code', response.status_code)
                print('Reason', response.reason)
                response_data = response.json()
                print(response_data)
            else:
                #erros
                print('Status code', response.status_code)
                print('Reason', response.reason)
                print('Reason', response.text) 

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
        
        return len(response_data)
#############################################################################################################
#################################### Main Window ############################################################
############################################################################################################# 

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow,self).__init__() 
        loadUi("MainWindow_vf.ui",self)       
        self.MenuButton.clicked.connect(self.SlideLeftMenu)
        self.Settings.clicked.connect(self.GotoSettings)
        self.Account.clicked.connect(self.GotoAccount)
        self.NewUnidade.clicked.connect(self.GotoADD)
        self.Home.clicked.connect(self.GotoMain)
        widget.showFullScreen()
        self.initUI()
        global x
        x = 3
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAxAAAAAAAAAAAAAAAAAAAAAAAA",x)  
        
    def unida1 (self):
        global global_Unidade_id_for_table_layout
        global_Unidade_id_for_table_layout = self.unidades_ids[0]
        global pressUnidade_global
        pressUnidade_global = 0
        self.GotoSensor()
    def unida2 (self):
        global global_Unidade_id_for_table_layout
        global_Unidade_id_for_table_layout = self.unidades_ids[1]
        global pressUnidade_global
        pressUnidade_global = 1
        self.GotoSensor()
    def unida3 (self):
        global global_Unidade_id_for_table_layout
        global_Unidade_id_for_table_layout = self.unidades_ids[2]
        global pressUnidade_global
        pressUnidade_global = 2
        self.GotoSensor()
    def unida4 (self):
        global global_Unidade_id_for_table_layout
        global_Unidade_id_for_table_layout = self.unidades_ids[3]
        global pressUnidade_global
        pressUnidade_global = 3
        self.GotoSensor()
    def unida5 (self):
        global global_Unidade_id_for_table_layout
        global_Unidade_id_for_table_layout = self.unidades_ids[4]
        global pressUnidade_global
        pressUnidade_global = 4
        self.GotoSensor()
    def unida6 (self):
        global global_Unidade_id_for_table_layout
        global_Unidade_id_for_table_layout = self.unidades_ids[5]
        global pressUnidade_global
        pressUnidade_global = 5
        self.GotoSensor()

    def GotoMain(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex())
        widget.showFullScreen()

    def GotoAccount(self):
        self.initUI()
        if len(self.unidades_ids) > 0:
            self.removeWidget(len(self.unidades_ids))
        widget.setCurrentIndex(widget.currentIndex()+2)
        widget.showFullScreen()

    def GotoADD(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex()+4)  
        widget.showFullScreen()
        
    def GotoSensor(self):
        self.initUI()
        global flag_delay
        flag_delay = 1
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.showFullScreen()
                
    def GotoSettings(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex()+3)  
        widget.showFullScreen() 

    def SlideLeftMenu(self):
        self.initUI()
        width = self.Left.width()
        
        if width == 55:
            newWidth = 140
        else:
            newWidth = 55
        
        self.animation = QPropertyAnimation(self.Left, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        #self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def setLastvalue(self,unidade_id): 
        
        ss = "Nah"
        url = "http://127.0.0.1:8000/Dados/"+ str(unidade_id)
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

        # processamento dos dados
        data_time = len(response_data)*[1]
        data_value = len(response_data)*[1]
        array_dados = len(response_data)*[1]

        i = 0
        for data in response_data:

            array_dados[i] = data
            string = str(data).split(',') # obter cada um dos dados

             ########  TIME
            time = string[0].split("'")   # string[0] corresponde ao tempo e split pra separar 'data_time' : '2021-03-10T18:05:30Z'
            time = time[3]                # separar e obter ex: '2021-03-10T18:05:30Z'
            time_proc = ""                # valor de time processado
            
            for j in range(len(time)):
                #print(j,"     ",ord(time[j]),"         ",ord('T'))
                if(ord(time[j]) == ord('T')):
                    time_proc = time_proc + " "
                elif(ord(time[j]) == ord('Z')):
                    time_proc = time_proc + ""
                else:
                    time_proc = time_proc + "" + time[j]
                j = j + 1
            data_time[i] = time_proc 
            
            ########  VALUE
            value = string[1].split(':')
            value = value[1].split(' ')
            data_value[i] = int(value[1])    #remover as ''
            #print(data_value[i])
            
            i = i + 1
            print (data_value[i-1])
            if len(data_value) > 0:
                ss = str(data_value[i-1])
            else:
                ss = "Nah"
        return ss

    def initUI(self):

        if(consola_id != -1):
            url = "http://127.0.0.1:8000/Unidades/" + str(consola_id)
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

            # processamento dos dados
            Unidade_id = len(response_data)*[1]
            Unidade_consola = len(response_data)*[1]
            Unidade_sensor = len(response_data)*[1]

            i = 0
            for data in response_data:

                string = str(data).split(',') # obter cada um dos dados
                
                ########  Unidade_id
                id = string[0].split(' ')  
                Unidade_id[i] = int(id[1])                       
                ########  Unidade_consola
                consola = string[1].split(' ')
                Unidade_consola[i] = int(consola[2]) #por algum motivo ele deteta um espaço no inicio, logo [2] e nao [1]
                ########  Unidade_sensor
                sensor = string[2].split("'")
                Unidade_sensor[i] = sensor[3]
                
                i = i + 1

            self.unidades_ids = Unidade_id

            global data_sensor
            data_sensor = Unidade_sensor

            global data_id
            data_id = Unidade_id

            colums_max = 1

            # quero ter no máximo 4 colunas
            if len(Unidade_sensor) >= 8:
                colums_max = 4  
            elif len(Unidade_sensor) >= 4:
                colums_max = len(Unidade_sensor)//2 + len(Unidade_sensor) % 2 
            elif len(Unidade_sensor) > 0:
                colums_max = len(Unidade_sensor)

            number_rows = (len(Unidade_sensor) // colums_max) + 1 # parte inteira da disisão = numero de linhas. Nota -1 se resto ==0 
            number_colums = len(Unidade_sensor) % colums_max # resto = numero de colunas finais
            if number_colums == 0:
                number_rows = number_rows-1

            # self.createNewWidgets(number_rows, number_colums)
            # FOR loop
            # rows
            i = 0
            if number_rows != 0:
                for x in range(0,number_rows):
                    # columns
                    for y in range(0,colums_max):
                        self.createNewWidgets(x, y,Unidade_sensor[i],Unidade_id[i],colums_max)
                        if x == (number_rows - 1): # ultima fila
                            if y == (number_colums - 1): # ultima posição na coluna
                                break
                        i = i + 1

            num_max_unidades = 6
            data = num_max_unidades*[False]
            for i in range(0, len(self.unidades_ids)):
                data[i] = True
            if data[0] == True:
                self.Sensor1Button.clicked.connect(self.unida1)
            if data[1] == True:
                self.Sensor2Button.clicked.connect(self.unida2)
            if data[2] == True:
                self.Sensor3Button.clicked.connect(self.unida3)
            if data[3] == True:
                self.Sensor4Button.clicked.connect(self.unida4)
            if data[4] == True:
                self.Sensor5Button.clicked.connect(self.unida5)
            if data[5] == True:
                self.Sensor6Button.clicked.connect(self.unida6)
                    
    def createNewWidgets(self, rowNumber, columNumber, sensor_type, Unidade_id,colums_max):
        # CREATE NEW UNIQUE NAMES FOR THE WIDGETS
        num = (rowNumber)*colums_max + (columNumber+1)
        newNameFrame = "Sensor" + str(num)
        print(newNameFrame)
        newNameFramel = "label" + str(num)
        newNameFrameb = "label" + str(num)
        newNameButton = "Sensor" + str(num) + "Button"
        newNameLabel = "Sensor" + str(num) + "Label"
        newNamevertical_f = "verticalLayoutframe" + str(num)
        newNamevertical_b = "verticalLayoutbutton" + str(num)
        newNamevertical_l = "verticalLayoutlabel" + str(num)

        # USE setObjectName() to give your object a new name
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(newNameFrame)
        self.frame.setMinimumSize(QSize(200, 200))
        #self.frame.setMaximumSize(QSize(200, 200))
        self.frame.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(newNamevertical_f)

        self.framel = QtWidgets.QFrame(self.frame)
        self.framel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framel.setMinimumSize(QSize(180, 87))
        self.framel.setMaximumSize(QSize(180, 87))
        self.framel.setObjectName(newNameFramel)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.framel)
        self.verticalLayout_4.setObjectName(newNamevertical_l)
        self.label = QtWidgets.QLabel(self.framel)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(42)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMinimumSize(QSize(160, 67))
        self.label.setMaximumSize(QSize(160, 67))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName(newNameLabel)
        last = self.setLastvalue(Unidade_id)
        if last !="Nah":
            self.label.setText(last)
            if int(last) > 50:
                self.label.setStyleSheet("border: 4px solid rgb(239, 41, 41);\n"
"    border-radius: 20px;\n"
"")
            elif int(last) > 20:
                self.label.setStyleSheet("border: 4px solid rgb(237, 212, 0);\n"
"    border-radius: 20px;\n"
"")
            else:
                self.label.setStyleSheet("border: 4px solid rgb(115, 210, 22);\n"
"    border-radius: 20px;\n"
"")
        else:
            self.label.setText("Nah")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.framel)

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QSize(180, 70))
        self.frame_2.setMaximumSize(QSize(180, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(newNameFrameb)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(newNamevertical_b)
        
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QSize(160, 50))
        self.pushButton.setMaximumSize(QSize(160, 50))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(136, 138, 133);\n"
"    border: 2px  ;\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(239, 41, 41);\n"
"    border: 2px solid rgb(239, 41, 41);\n"
"}")
        self.pushButton.setObjectName(newNameButton) 
        self.pushButton.setText("Sensor "+str(sensor_type))      
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        # Create new attribute to Mainwindow
        # Syntax : setattr(obj, var, val)
        # Parameters :
        # obj : Object whose which attribute is to be assigned.
        # var : object attribute which has to be assigned.
        # val : value with which variable is to be assigned.
        setattr(self, newNameFrame, self.frame)
        setattr(self, newNameFramel, self.framel)
        setattr(self, newNameFrameb, self.frame_2)
        setattr(self, newNameButton, self.pushButton)
        setattr(self, newNameLabel, self.label)

        setattr(self, newNamevertical_f, self.verticalLayout_2)
        setattr(self, newNamevertical_b, self.verticalLayout_3)
        setattr(self, newNamevertical_l, self.verticalLayout_4)

        # 
        # void QGridLayout::addLayout(QLayout *layout, int row, int column, int rowSpan, int columnSpan, Qt::Alignment alignment = Qt::Alignment())
        # 
        self.gridLayout.addWidget(self.frame, rowNumber, columNumber, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

    
    def removeWidget(self, lenght):
        if lenght > 0:
            if lenght >= 8:
                colums_max = 4  
            elif lenght >= 4:
                colums_max = lenght//2 + lenght % 2 
            elif lenght > 0:
                colums_max = lenght

            number_rows = (lenght // colums_max) + 1 # parte inteira da disisão = numero de linhas. Nota -1 se resto ==0 
            number_colums = lenght % colums_max # resto = numero de colunas finais
            if number_colums == 0:
                number_rows = number_rows-1
            
            sensor = [self.Sensor1]
            if lenght == 2:
                sensor = [self.Sensor1,self.Sensor2]
            if lenght == 3:
                sensor = [self.Sensor1,self.Sensor2,self.Sensor3]
            if lenght == 4:
                sensor = [self.Sensor1,self.Sensor2,self.Sensor3,self.Sensor4]
            if lenght == 5:
                sensor = [self.Sensor1,self.Sensor2,self.Sensor3,self.Sensor4,self.Sensor5]
            if lenght == 6:
                sensor = [self.Sensor1,self.Sensor2,self.Sensor3,self.Sensor4,self.Sensor5,self.Sensor6]
            
            # self.deleteWidgets(number_rows, number_colums)
            # FOR loop
            # rows
            i = 0
            if number_rows != 0:
                for x in range(0,number_rows):
                    # columns
                    for y in range(0,colums_max):
                        self.removeWid(x, y, colums_max)
                        if x == (number_rows - 1): # ultima fila
                            if y == (number_colums - 1): # ultima posição na coluna
                                break
                        i = i + 1

    def removeWid(self, rowNumber, columNumber, colums_max):
        # CREATE NEW UNIQUE NAMES FOR THE WIDGETS
        num = (rowNumber)*colums_max + (columNumber+1)
        newNameFrame = "Sensor" + str(num)

        # USE setObjectName() to give your object a new name
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(newNameFrame)
        self.frame.setMinimumSize(QSize(200, 200))
        #self.frame.setMaximumSize(QSize(200, 200))
        self.frame.setStyleSheet(u"background-color: rgb(238, 238, 236);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        # Create new attribute to Mainwindow
        # Syntax : setattr(obj, var, val)
        # Parameters :
        # obj : Object whose which attribute is to be assigned.
        # var : object attribute which has to be assigned.
        # val : value with which variable is to be assigned.
        setattr(self, newNameFrame, self.frame)

        # 
        # void QGridLayout::addLayout(QLayout *layout, int row, int column, int rowSpan, int columnSpan, Qt::Alignment alignment = Qt::Alignment())
        # 
        self.gridLayout.addWidget(self.frame, rowNumber, columNumber, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

class SensorWindow(QMainWindow):
    def __init__(self):
        super(SensorWindow,self).__init__() 
        loadUi("SensorWindow_vf.ui",self)
        self.GotoMainButton.clicked.connect(self.GotoMain)
        self.GotoGraphicButton_3.clicked.connect(self.GotoGraphicbar)
        self.GotoGraphicButton.clicked.connect(self.GotoGraphic)
        self.GotoTableButton.clicked.connect(self.tabelaDados)
        self.NomeSensor.setText("")
        self.lastvalue.setText("")
        self.lastvalue_label.setText("")
        if flag_delay == 1:
            self.tabelaDados()
        global x 
        x = 0

    def GotoMain(self):
        self.tabelaDados()
        widget.setCurrentIndex(widget.currentIndex()-1) 
        widget.showFullScreen()    
    
    def GotoGraphicbar(self):
        self.tabelaDados()
        widget.setCurrentIndex(widget.currentIndex()+4)
        widget.showFullScreen() 

    def GotoGraphic(self):
        self.tabelaDados()
        widget.setCurrentIndex(widget.currentIndex()+5)
        widget.showFullScreen()  

    def tabelaDados (self):
        if pressUnidade_global != -1:
            self.NomeSensor.setText(str(data_sensor[pressUnidade_global]))
        else:
            self.NomeSensor.setText("")

        #obter os dados
        if(global_Unidade_id_for_table_layout != -1):
            url = "http://127.0.0.1:8000/Dados/"+str(global_Unidade_id_for_table_layout)
            print("global_Unidade_id_for_table_layout",global_Unidade_id_for_table_layout)
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

            # processamento dos dados
            data_time = len(response_data)*[1]
            data_value = len(response_data)*[1]
            data_time_day = len(response_data)*[1]
            array_dados = len(response_data)*[1]

            i = 0
            for data in response_data:

                array_dados[i] = data
                string = str(data).split(',') # obter cada um dos dados

                ########  TIME
                time = string[0].split("'")   # string[0] corresponde ao tempo e split pra separar 'data_time' : '2021-03-10T18:05:30Z'
                time = time[3]                # separar e obter ex: '2021-03-10T18:05:30Z'
                time_proc = "" # valor de time processado
                for j in range(len(time)):
                    #print(j,"     ",ord(time[j]),"         ",ord('T'))
                    if(ord(time[j]) == ord('T')):
                        time_proc = time_proc + " "
                    elif(ord(time[j]) == ord('Z')):
                        time_proc = time_proc + ""
                    else:
                        time_proc = time_proc + "" + time[j]
                    j = j + 1

                time_proc = time_proc.split(" ")
                data_time_day[i] = time_proc[0]
                data_time[i] = time_proc[1]
                
                ########  VALUE
                value = string[1].split(':')
                value = value[1].split(' ')
                data_value[i] = int(value[1])    #remover as ''

                i = i + 1

            # fazer tabela
            self.tableWidget.setRowCount(len(response_data))
            self.tableWidget.verticalHeader().setVisible(False)
            if(len(data_time)>0):
                i = 0
                for data in data_value:
                    self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(data_time_day[i]))
                    self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(data_time[i]))
                    self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(str(data_value[i])))
                    i = i + 1
                self.lastvalue_label.setText("last value = ")
                self.lastvalue.setText(str(data_value[i-1]))
                if data_value[i-1] > 50:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(239, 41, 41);\n"
"    border-radius: 20px;\n"
"")
                elif data_value[i-1] > 20:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(237, 212, 0);\n"
"    border-radius: 20px;\n"
"")
                else:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(115, 210, 22);\n"
"    border-radius: 20px;\n"
"")
            else:
                self.lastvalue.setText("Nah")
            

class graphicBarWindow(QMainWindow):
    def __init__(self):
        super(graphicBarWindow,self).__init__() 
        loadUi("Grafic_2.ui",self)
        self.GotoMainButton.clicked.connect(self.GotoMain)
        self.GotoTableButton.clicked.connect(self.GotoTable)
        self.GotoGraphicButton_3.clicked.connect(self.initUI)
        self.GotoGraphicButton.clicked.connect(self.GotoGraphic)
        self.lastvalue.setText("")
        self.lastvalue_label.setText("")
        self.timeSelected_label.setText("")
        self.initUI()
        global x 
        x = 0

    def GotoGraphic(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.showFullScreen()

    def GotoMain(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex()-5)
        widget.showFullScreen()

    def GotoTable(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex()-4)
        widget.showFullScreen()  
    
    def initUI(self):
        if pressUnidade_global != -1:
            self.NomeSensor.setText(str(data_sensor[pressUnidade_global]))
        else:
            self.NomeSensor.setText("")

        # Crear gráfico
        if global_Unidade_id_for_table_layout != -1:
            self.criarGrafico()
            self.timeSelected_label.setText("Time selected = " + press)
            # ========================== DISEÑO ==========================
            self.baseDisenio_2.addWidget(self.vistaGrafico, 0, 0, 0, 1)
            self.baseDisenio_2.setSpacing(10)
            self.baseDisenio_2.setContentsMargins(10, 10, 10, 10)
    
    def criarGrafico(self):
        ########################## obter os dados ##################
        if global_Unidade_id_for_table_layout != -1:
            url = "http://127.0.0.1:8000/Dados/"+str(global_Unidade_id_for_table_layout)
            response = requests.get(url)

            print("global_Unidade_id_for_table_layout",global_Unidade_id_for_table_layout)

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

            # processamento dos dados
            data_time = len(response_data)*[1]
            data_value = len(response_data)*[1]
            data_time_day = len(response_data)*[1]
            array_dados = len(response_data)*[1]
            data_allTime = len(response_data)*[1]

            i = 0
            for data in response_data:

                array_dados[i] = data
                string = str(data).split(',') # obter cada um dos dados

                ########  TIME
                time = string[0].split("'")   # string[0] corresponde ao tempo e split pra separar 'data_time' : '2021-03-10T18:05:30Z'
                time = time[3]                # separar e obter ex: '2021-03-10T18:05:30Z'
                time_proc = "" # valor de time processado
                for j in range(len(time)):
                    #print(j,"     ",ord(time[j]),"         ",ord('T'))
                    if(ord(time[j]) == ord('T')):
                        time_proc = time_proc + " "
                    elif(ord(time[j]) == ord('Z')):
                        time_proc = time_proc + ""
                    else:
                        time_proc = time_proc + "" + time[j]
                    j = j + 1
                
                data_allTime[i] = time_proc    
                time_proc = time_proc.split(" ")
                data_time_day[i] = time_proc[0]
                data_time[i] = time_proc[1]
                
                ########  VALUE
                value = string[1].split(':')
                value = value[1].split(' ')
                data_value[i] = int(value[1])    #remover as ''

                i = i + 1     

            self.lastvalue_label.setText("last value = ")
            if(len(data_value)>0):
                self.lastvalue.setText(str(data_value[len(data_value)-1]))
                if data_value[len(data_value)-1] > 50:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(239, 41, 41);\n"
"    border-radius: 20px;\n"
"")
                elif data_value[len(data_value)-1] > 20:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(237, 212, 0);\n"
"    border-radius: 20px;\n"
"")
                else:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(115, 210, 22);\n"
"    border-radius: 20px;\n"
"")
            else:
                self.lastvalue.setText("Nah")

            #criar grafico de barras
            class barGraph(pg.BarGraphItem):
                def mouseClickEvent(self,event):
                    global press 
                    press = data_allTime[0]

            self.vistaGrafico = pg.plot()
            x = 0
            for j in range(len(data_value)):
                y = int(data_value[j])
                if y > 50:
                    color = 'r'
                elif y > 20:
                    color = 'y'
                else:
                    color = 'g'
                bg = barGraph(x=[x], height = y, width = 0.3, brush = color)
                self.vistaGrafico.addItem(bg)
                x = x + 1

class graphicWindow(QMainWindow):
    def __init__(self):
        super(graphicWindow,self).__init__() 
        loadUi("Grafic_3.ui",self)
        self.GotoMainButton.clicked.connect(self.GotoMain)
        self.GotoTableButton.clicked.connect(self.GotoTable)
        self.GotoGraphicButton_3.clicked.connect(self.GotoGraphicBar)
        self.GotoGraphicButton.clicked.connect(self.initUI)
        self.lastvalue.setText("")
        self.lastvalue_label.setText("")
        self.initUI()
        global x 
        x = 0

    def GotoGraphicBar(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.showFullScreen()

    def GotoMain(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex()-5)
        widget.showFullScreen()

    def GotoTable(self):
        self.initUI()
        widget.setCurrentIndex(widget.currentIndex()-4)
        widget.showFullScreen()  
    
    def initUI(self):
        if pressUnidade_global != -1:
            self.NomeSensor.setText(str(data_sensor[pressUnidade_global]))
        else:
            self.NomeSensor.setText("")

        # Crear gráfico
        if global_Unidade_id_for_table_layout != -1:
            self.criarGrafico()
            # ========================== DISEÑO ==========================
            self.baseDisenio_2.addWidget(self.vistaGrafico, 0, 0, 0, 1)
            self.baseDisenio_2.setSpacing(10)
            self.baseDisenio_2.setContentsMargins(10, 10, 10, 10)
    
    def criarGrafico(self):
        ########################## obter os dados ##################
        if global_Unidade_id_for_table_layout != -1:
            url = "http://127.0.0.1:8000/Dados/"+str(global_Unidade_id_for_table_layout)
            response = requests.get(url)

            print("global_Unidade_id_for_table_layout",global_Unidade_id_for_table_layout)

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

            # processamento dos dados
            data_time = len(response_data)*[1]
            data_value = len(response_data)*[1]
            data_time_day = len(response_data)*[1]
            array_dados = len(response_data)*[1]
            data_allTime = len(response_data)*[1]

            i = 0
            for data in response_data:

                array_dados[i] = data
                string = str(data).split(',') # obter cada um dos dados

                ########  TIME
                time = string[0].split("'")   # string[0] corresponde ao tempo e split pra separar 'data_time' : '2021-03-10T18:05:30Z'
                time = time[3]                # separar e obter ex: '2021-03-10T18:05:30Z'
                time_proc = "" # valor de time processado
                for j in range(len(time)):
                    #print(j,"     ",ord(time[j]),"         ",ord('T'))
                    if(ord(time[j]) == ord('T')):
                        time_proc = time_proc + " "
                    elif(ord(time[j]) == ord('Z')):
                        time_proc = time_proc + ""
                    else:
                        time_proc = time_proc + "" + time[j]
                    j = j + 1
                
                data_allTime[i] = time_proc    
                time_proc = time_proc.split(" ")
                data_time_day[i] = time_proc[0]
                data_time[i] = time_proc[1]
                
                ########  VALUE
                value = string[1].split(':')
                value = value[1].split(' ')
                data_value[i] = int(value[1])    #remover as ''

                i = i + 1     

            self.lastvalue_label.setText("last value = ")
            if(len(data_value)>0):
                self.lastvalue.setText(str(data_value[len(data_value)-1]))
                if data_value[len(data_value)-1] > 50:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(239, 41, 41);\n"
"    border-radius: 20px;\n"
"")
                elif data_value[len(data_value)-1] > 20:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(237, 212, 0);\n"
"    border-radius: 20px;\n"
"")
                else:
                    self.lastvalue.setStyleSheet("border: 4px solid rgb(115, 210, 22);\n"
"    border-radius: 20px;\n"
"")
            else:
                self.lastvalue.setText("Nah")

            self.vistaGrafico = pg.plot(x = np.arange(len(data_value)), y=data_value)

class ProfileWindow(QMainWindow):
    
    def __init__(self):
        super(ProfileWindow,self).__init__() 
        loadUi("ProfileWindow.ui",self)
        self.LogOutButton.clicked.connect(self.GotoLogin)
        self.GotoMainButton.clicked.connect(self.GotoMain)
        self.UserManual.clicked.connect(self.GotoUserManual)
        self.fillProfile()
        global x 
        x = 0

    def GotoLogin(self):
        self.fillProfile()
        widget.setCurrentIndex(widget.currentIndex()-4)
        widget.showNormal()

    def GotoUserManual(self):
        self.fillProfile()

    def GotoMain(self):
        self.fillProfile()
        widget.setCurrentIndex(widget.currentIndex()-2) 
        widget.showFullScreen()  

    def fillProfile(self):
        if consola_id == -1:
            self.id_label.setText("id= ")
        else:
            self.id_label.setText("id = "+str(consola_id))
        self.usename_label.setText(str(username_global))
        self.Email_label.setText(str(email_global))
        self.tabelaDados()
    
    def tabelaDados (self):
        if(len(data_sensor) > 0):
            # fazer tabela
            self.tableWidget.setRowCount(len(data_sensor))
            self.tableWidget.verticalHeader().setVisible(False)
            if(len(data_sensor)>0):
                i = 0
                for data in data_sensor:
                    self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(data_sensor[i-1]))
                    self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(data_id[i-1])))
                    i = i + 1

class SettingsWindow(QMainWindow):
    
    def __init__(self):
        super(SettingsWindow,self).__init__() 
        loadUi("SettingsWindow.ui",self)
        self.GotoMainButton.clicked.connect(self.GotoMain)
        global x 
        x = 0

    def GotoMain(self):
        widget.setCurrentIndex(widget.currentIndex()-3)
        widget.showFullScreen()


class AddWindow(QMainWindow):
    
    def __init__(self):
        widget.showFullScreen()
        super(AddWindow,self).__init__() 
        loadUi("AddWindow_vf.ui",self)
        self.Account.clicked.connect(self.GotoProfile)
        self.Settings.clicked.connect(self.GotoSettings)
        self.Home.clicked.connect(self.GotoHome)
        self.MenuButton.clicked.connect(self.SlideLeftMenu)
        global x 
        x = 0
                
    def GotoProfile(self):
        widget.setCurrentIndex(widget.currentIndex()-2) 
        widget.showFullScreen()
    
    def GotoSettings(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.showFullScreen()

    def GotoHome(self):
        widget.setCurrentIndex(widget.currentIndex()-4)
        widget.showFullScreen() 

    def SlideLeftMenu(self):
        width = self.Left.width()
        
        if width == 55:
            newWidth = 140
        else:
            newWidth = 55
        
        self.animation = QPropertyAnimation(self.Left, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        #self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()       

#Main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

login_w = LoginWindow()
register_w = RegisterWindow()
Main_W = MainWindow()
Sensor_W  = SensorWindow()
Profile_w = ProfileWindow()
Settings_w = SettingsWindow()
Add_w = AddWindow()
graphicbar_W = graphicBarWindow()
graphic_W = graphicWindow()




widget.addWidget(login_w)       # id = 1
widget.addWidget(register_w)    # id = 2
widget.addWidget(Main_W)        # id = 3
widget.addWidget(Sensor_W)      # id = 4
widget.addWidget(Profile_w)     # id = 5
widget.addWidget(Settings_w)    # id = 6
widget.addWidget(Add_w)         # id = 7
widget.addWidget(graphicbar_W)  # id = 8
widget.addWidget(graphic_W)     # id = 9
#widget.show()
#if (widget.currentIndex() <=2): 
widget.showMinimized()

try:
    sys.exit(app.exec_())

except:
    print("Exiting")