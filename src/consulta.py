# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class Ui_MConsulta(object):
    
    def setupUi(self, MConsulta):
        
        MConsulta.setObjectName("MConsulta")
        MConsulta.resize(800, 600)
        MConsulta.setMaximumSize(QtCore.QSize(800, 600))
        MConsulta.setMinimumSize(QtCore.QSize(800, 600))
        
        colores = QtGui.QPalette()
        
        pincel  = QtGui.QBrush(QtGui.QColor("#102A43"))
        pincel.setStyle(QtCore.Qt.SolidPattern)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, pincel)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, pincel)
        #colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, pincel)
        #colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light,pincel)
        #colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, pincel)
        #colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark,pincel)
        
        pincel  = QtGui.QBrush(QtGui.QColor("#9FB3C8"))
        pincel.setStyle(QtCore.Qt.SolidPattern)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, pincel)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, pincel)
        
        pincel  = QtGui.QBrush(QtGui.QColor("#BCCCDC"))
        pincel.setStyle(QtCore.Qt.SolidPattern)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window,pincel)
        
        pincel  = QtGui.QBrush(QtGui.QColor("#2CB1BC"))
        pincel.setStyle(QtCore.Qt.SolidPattern)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight,pincel)
        
        letra = QtGui.QFont()
        letra.setFamily("Arial")
        letra.setPointSize(12)
        letra.setBold(True)
        
        letraeditable = QtGui.QFont()
        letraeditable.setFamily("Arial")
        letraeditable.setPointSize(11)
        
        self.centralwidget = QtWidgets.QWidget(MConsulta)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lineainferior = QtWidgets.QFrame(self.centralwidget)
        self.lineainferior.setGeometry(QtCore.QRect(10, 10, 780, 580))
        self.lineainferior.setFrameShape(QtWidgets.QFrame.Box)
        self.lineainferior.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineainferior.setObjectName("lineasupeior")
        
        self.visordereportes= QtWidgets.QTableWidget(MConsulta)
        self.visordereportes.setGeometry(QtCore.QRect(15, 15, 770, 470))
        self.visordereportes.setColumnCount(12)
        self.visordereportes.setHorizontalHeaderLabels(("ID","Fecha", "Turno",  "Oficina", "Soporte","Descripción", 
                                             "Puesto", "Bien", "IP", "MAC", "Observación", "Estatus"))
        
        MConsulta.setPalette(colores)
        
        self.retranslateUi(MConsulta)
        QtCore.QMetaObject.connectSlotsByName(MConsulta)

    def retranslateUi(self, MConsulta):
        
        _translate = QtCore.QCoreApplication.translate
        MConsulta.setWindowTitle(_translate("Consulta", "CONSULTA"))