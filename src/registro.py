# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

class Ui_MRegistro(object):
    
    def setupUi(self, MRegistro):
        
        MRegistro.setObjectName("MRegistro")
        MRegistro.resize(800, 600)
        MRegistro.setMaximumSize(QtCore.QSize(800, 600))
        MRegistro.setMinimumSize(QtCore.QSize(800, 600))
        
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
        
        self.centralwidget = QtWidgets.QWidget(MRegistro)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lineainferior = QtWidgets.QFrame(self.centralwidget)
        self.lineainferior.setGeometry(QtCore.QRect(10, 10, 780, 580))
        self.lineainferior.setFrameShape(QtWidgets.QFrame.Box)
        self.lineainferior.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineainferior.setObjectName("lineasupeior")
        
        #-----------------------------------------------------------------------
        self.tfecha = QtWidgets.QLabel(self.centralwidget)
        self.tfecha.setGeometry(QtCore.QRect(25, 70, 90, 20))
        self.tfecha.setFont(letra)
        self.tfecha.setObjectName("tfecha")
        
        self.mfecha = QtWidgets.QLabel(self.centralwidget)
        self.mfecha.setGeometry(QtCore.QRect(25, 100, 90, 20))
        self.mfecha.setText("")
        self.mfecha.setFont(letraeditable)
        self.mfecha.setObjectName("mfecha")
        
        #-----------------------------------------------------------------------
        self.tturno = QtWidgets.QLabel(self.centralwidget)
        self.tturno.setGeometry(QtCore.QRect(25, 130, 90, 20))
        self.tturno.setFont(letra)
        self.tturno.setObjectName("tturno")
        
        self.eturno = QtWidgets.QComboBox(self.centralwidget)
        self.eturno.setGeometry(QtCore.QRect(25, 160, 100, 20))
        self.eturno.setObjectName("eturno")
        self.eturno.setFont(letraeditable)
        self.eturno.addItem("")
        self.eturno.addItem("")
        self.eturno.addItem("") 
        
        #-----------------------------------------------------------------------
        self.toficina = QtWidgets.QLabel(self.centralwidget)
        self.toficina.setGeometry(QtCore.QRect(135, 130, 90, 20))
        self.toficina.setFont(letra)
        self.toficina.setObjectName("toficina")
        
        self.eoficina = QtWidgets.QComboBox(self.centralwidget)
        self.eoficina.setGeometry(QtCore.QRect(135, 160, 180, 20))
        self.eoficina.setFont(letraeditable)
        self.eoficina.setObjectName("eoficina")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        self.eoficina.addItem("")
        
        #-----------------------------------------------------------------------
        self.tsoportes = QtWidgets.QLabel(self.centralwidget)
        self.tsoportes.setGeometry(QtCore.QRect(325, 130, 150, 20))
        self.tsoportes.setFont(letra)
        self.tsoportes.setObjectName("tsoportes")
        
        self.esoporte = QtWidgets.QComboBox(self.centralwidget)
        self.esoporte.setGeometry(QtCore.QRect(325, 160, 150, 20))
        self.esoporte.setFont(letraeditable)
        self.esoporte.setObjectName("esoporte")
        self.esoporte.addItem("")
        self.esoporte.addItem("")
        self.esoporte.addItem("")
        self.esoporte.addItem("")
        self.esoporte.addItem("")
        self.esoporte.addItem("")
        self.esoporte.addItem("")
        self.esoporte.addItem("")
        
        #-----------------------------------------------------------------------
        self.ttdescripcion = QtWidgets.QLabel(self.centralwidget)
        self.ttdescripcion.setGeometry(QtCore.QRect(485, 130, 200, 20))
        self.ttdescripcion.setFont(letra)
        self.ttdescripcion.setObjectName("ttdescripcion")
        
        self.edescripcion = QtWidgets.QComboBox(self.centralwidget)
        self.edescripcion.setGeometry(QtCore.QRect(485, 160,295, 20))
        self.edescripcion.setFont(letraeditable)
        self.edescripcion.setObjectName("edescripcion")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        self.edescripcion.addItem("")
        
        #-----------------------------------------------------------------------
        self.tpuestos = QtWidgets.QLabel(self.centralwidget)
        self.tpuestos.setGeometry(QtCore.QRect(25, 190, 70, 20))
        self.tpuestos.setFont(letra)
        self.tpuestos.setObjectName("tpuestos")
        
        self.epuestos = QtWidgets.QComboBox(self.centralwidget)
        self.epuestos.setGeometry(QtCore.QRect(25, 220, 70, 20))
        self.epuestos.setFont(letra)
        self.epuestos.setObjectName("epuestos")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        self.epuestos.addItem("")
        
        #-----------------------------------------------------------------------
        self.tbien = QtWidgets.QLabel(self.centralwidget)
        self.tbien.setGeometry(QtCore.QRect(105, 190, 200, 20))
        self.tbien.setFont(letra)
        self.tbien.setObjectName("tbien")
        
        self.ebien = QtWidgets.QLineEdit(self.centralwidget)
        self.ebien.setGeometry(QtCore.QRect(105, 220, 145, 20))
        self.ebien.setFont(letraeditable)
        self.ebien.setObjectName("ebien")
        
        #-----------------------------------------------------------------------
        self.tip = QtWidgets.QLabel(self.centralwidget)
        self.tip.setGeometry(QtCore.QRect(323, 190, 90, 20))
        self.tip.setFont(letra)
        self.tip.setObjectName("tip")
        
        self.cip = QtWidgets.QLabel(self.centralwidget)
        self.cip.setGeometry(QtCore.QRect(260, 220, 61, 20))
        self.cip.setFont(letra)
        self.cip.setObjectName("cip")
        
        self.eip = QtWidgets.QLineEdit(self.centralwidget)
        self.eip.setGeometry(QtCore.QRect(326, 220, 61, 20))
        self.eip.setFont(letraeditable)
        self.eip.setObjectName("eip")
         
        #-----------------------------------------------------------------------
        self.tmac = QtWidgets.QLabel(self.centralwidget)
        self.tmac.setGeometry(QtCore.QRect(397, 190, 90, 20))
        self.tmac.setFont(letra)
        self.tmac.setObjectName("tmac")
        
        self.emac = QtWidgets.QLineEdit(self.centralwidget)
        self.emac.setGeometry(QtCore.QRect(397, 220, 130, 20))
        self.emac.setObjectName("emac")
        
        #-----------------------------------------------------------------------
        self.tnota = QtWidgets.QLabel(self.centralwidget)
        self.tnota.setGeometry(QtCore.QRect(537, 190, 200, 20))
        self.tnota.setFont(letra)
        self.tnota.setObjectName("tnota")
        
        self.enota = QtWidgets.QLineEdit(self.centralwidget)
        self.enota.setGeometry(QtCore.QRect(537, 220, 243, 20))
        self.enota.setObjectName("enota")
        
        #-----------------------------------------------------------------------
        self.testatus = QtWidgets.QLabel(self.centralwidget)
        self.testatus.setGeometry(QtCore.QRect(537, 260, 90, 20))
        self.testatus.setFont(letra)
        self.testatus.setObjectName("testatus")
        
        self.eestatus = QtWidgets.QComboBox(self.centralwidget)
        self.eestatus.setGeometry(QtCore.QRect(537, 290, 160, 20))
        self.eestatus.setFont(letraeditable)
        self.eestatus.setObjectName("eestatus")
        self.eestatus.addItem("")
        self.eestatus.addItem("")
        self.eestatus.addItem("")
        self.eestatus.addItem("")
        
        #-----------------------------------------------------------------------
        self.mapa = QtWidgets.QLabel(MRegistro)
        self.mapa.setGeometry(QtCore.QRect(25, 260, 500, 300))
        self.mapa.setStyleSheet("background-color: #FFFFFF;")
        self.mapa.setObjectName("mapa")
        
        #-----------------------------------------------------------------------
        self.cargardatos = QtWidgets.QPushButton(self.centralwidget)
        self.cargardatos.setGeometry(QtCore.QRect(537, 440, 243, 120))
        self.cargardatos.setFont(letra)
        self.cargardatos.setObjectName("cargardatos")
        
        #-----------------------------------------------------------------------
        
        MRegistro.setPalette(colores)
        
        self.retranslateUi(MRegistro)
        QtCore.QMetaObject.connectSlotsByName(MRegistro)

    def retranslateUi(self, MRegistro):
        
        _translate = QtCore.QCoreApplication.translate
        MRegistro.setWindowTitle(_translate("Registro", "Registro"))
        
        self.cargardatos.setText(_translate("MRegistro", "CARGAR"))
        self.tfecha.setText(_translate("MRegistro", "FECHA"))
        self.toficina.setText(_translate("MRegistro", "OFICINA"))
        self.tturno.setText(_translate("MRegistro", "TURNO"))
        self.tsoportes.setText(_translate("MRegistro", "TIPO DE SOPORTE"))
        self.ttdescripcion.setText(_translate("MRegistro", "DESCRIPCI??N"))
        self.tpuestos.setText(_translate("MRegistro", "PUESTO"))
        self.tbien.setText(_translate("MRegistro", "N??MERO DE BIEN"))
        self.tip.setText(_translate("MRegistro", "IP"))
        self.tmac.setText(_translate("MRegistro", "MAC"))
        self.tnota.setText(_translate("MRegistro", "OBSERVACIONES"))
        self.testatus.setText(_translate("MRegistro", "ESTATUS"))
        
        self.eturno.setItemText(1,_translate("MRegistro", "MA??ANA"))
        self.eturno.setItemText(2,_translate("MRegistro", "TARDE"))
        
        self.eestatus.setItemText(1,_translate("MRegistro", "CULMINADO"))
        self.eestatus.setItemText(2,_translate("MRegistro", "EN PROCESO"))
        self.eestatus.setItemText(3,_translate("MRegistro", "NO CULMINADO"))
        
        self.eoficina.setItemText(1, _translate("MRegistro", "ADMINISTRACI??N"))
        self.eoficina.setItemText(2, _translate("MRegistro", "GESTI??N HUMANA"))
        self.eoficina.setItemText(3, _translate("MRegistro", "PRESIDENCIA"))
        self.eoficina.setItemText(4, _translate("MRegistro", "PLANIFICACI??N"))
        self.eoficina.setItemText(5, _translate("MRegistro", "PRENSA"))
        self.eoficina.setItemText(6, _translate("MRegistro", "RED NACIONAL"))
        self.eoficina.setItemText(7, _translate("MRegistro", "DEMANDA"))
        self.eoficina.setItemText(8, _translate("MRegistro", "INTERNACIONALES"))
        self.eoficina.setItemText(9, _translate("MRegistro", "DESPACHO"))
        self.eoficina.setItemText(10, _translate("MRegistro", "OVD"))
        self.eoficina.setItemText(11, _translate("MRegistro", "CONSULTORIA"))
        self.eoficina.setItemText(12, _translate("MRegistro", "OSTIC"))
        self.eoficina.setItemText(13, _translate("MRegistro", "OFERTA"))
        self.eoficina.setItemText(14, _translate("MRegistro", "CAE"))
        self.eoficina.setItemText(15, _translate("MRegistro", "SEGURIDAD"))
        self.eoficina.setItemText(16, _translate("MRegistro", "ENFERMERIA"))
        self.eoficina.setItemText(17, _translate("MRegistro", "CORRESPONDENCIA"))
        self.eoficina.setItemText(18, _translate("MRegistro", "SERV. GENERALES"))
        self.eoficina.setItemText(19, _translate("MRegistro", "TRANSPORTE"))
        self.eoficina.setItemText(20, _translate("MRegistro", "CEAD"))
        self.eoficina.setItemText(21, _translate("MRegistro", "OTRA INSTITUCI??N"))
        
        self.esoporte.setItemText(1, _translate("MRegistro", "REDES"))
        self.esoporte.setItemText(2, _translate("MRegistro", "SERVIDORES"))
        self.esoporte.setItemText(3, _translate("MRegistro", "DESARROLLO"))
        self.esoporte.setItemText(4, _translate("MRegistro", "IMPRESORAS"))
        self.esoporte.setItemText(5, _translate("MRegistro", "EVENTOS"))
        self.esoporte.setItemText(6, _translate("MRegistro", "GENERAL"))
        self.esoporte.setItemText(7, _translate("MRegistro", "INTERNAS"))
        
        self.cip.setText(_translate("MRegistro", "192.168."))
