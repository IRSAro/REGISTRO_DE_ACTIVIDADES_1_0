
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MInicio(object):
    def setupUi(self, MInicio):
        MInicio.setObjectName("MInicio")
        MInicio.resize(800, 600)
        MInicio.setMaximumSize(QtCore.QSize(800, 600))
        MInicio.setMinimumSize(QtCore.QSize(800, 600))
        
        MInicio.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MInicio.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        
        colores = QtGui.QPalette()
        
        pincel  = QtGui.QBrush(QtGui.QColor("#9FB3C8"))
        pincel.setStyle(QtCore.Qt.SolidPattern)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, pincel)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, pincel)
        
        pincel  = QtGui.QBrush(QtGui.QColor("#102A43"))
        pincel.setStyle(QtCore.Qt.SolidPattern) 
        #colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, pincel)
        #colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light,pincel)
        #colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, pincel)
        #colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark,pincel)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, pincel)
        
        pincel  = QtGui.QBrush(QtGui.QColor("#BCCCDC"))
        pincel.setStyle(QtCore.Qt.SolidPattern)
        colores.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, pincel)
        colores.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window,pincel)
        
        letra = QtGui.QFont()
        letra.setFamily("Arial")
        letra.setPointSize(12)
        letra.setBold(True)
        
        self.centralwidget = QtWidgets.QWidget(MInicio)
        self.centralwidget.setObjectName("centralwidget")
        
        self.lineainferior = QtWidgets.QFrame(self.centralwidget)
        self.lineainferior.setGeometry(QtCore.QRect(25, 25, 750, 550))
        self.lineainferior.setFrameShape(QtWidgets.QFrame.Box)
        self.lineainferior.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineainferior.setObjectName("lineasupeior")
        
        self.idatos= QtWidgets.QPushButton(self.centralwidget)
        self.idatos.setGeometry(QtCore.QRect(300, 150, 200, 100))
        self.idatos.setFont(letra)
        self.idatos.setObjectName("idatos")
        
        self.cdatos= QtWidgets.QPushButton(self.centralwidget)
        self.cdatos.setGeometry(QtCore.QRect(300, 300, 200, 100))
        self.cdatos.setFont(letra)
        self.cdatos.setObjectName("cdatos")
        
        MInicio.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MInicio)
        self.statusbar.setObjectName("statusbar")
       
        MInicio.setPalette(colores)
        MInicio.setStatusBar(self.statusbar)

        self.retranslateUi(MInicio)
        QtCore.QMetaObject.connectSlotsByName(MInicio)

    def retranslateUi(self, MInicio):
        _translate = QtCore.QCoreApplication.translate
        MInicio.setWindowTitle(_translate("MInicio", "Sistema de registro de actividades OSTIC"))
        self.idatos.setText(_translate("MInicio", "REGISTRO"))
        self.cdatos.setText(_translate("MInicio", "CONSULTA"))