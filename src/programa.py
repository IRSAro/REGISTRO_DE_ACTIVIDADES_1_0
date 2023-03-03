# -*- coding: utf-8 -*-

from inicio import *
from registro import *
from consulta import *
from datetime  import date, time, datetime 
from sqlite3 import connect

conectar = connect('DATOS.db')   
puntero = conectar.cursor()

puntero.execute("""CREATE TABLE IF NOT EXISTS Reportes (InfID INTEGER PRIMARY KEY 
AUTOINCREMENT, Fecha TEXT, Hora TEXT,  Oficina TEXT, Soporte TEXT, 
Descripcion TEXT, Puesto TEXT, Bien TEXT, IP TEXT, MAC TEXT, Observacion TEXT, Estatus TEXT)""")        
conectar.commit()

class consulta(QtWidgets.QDialog, Ui_MConsulta):
    
    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        conectar = connect('DATOS.db')   
        puntero = conectar.cursor()
        puntero.execute("SELECT InfID,Fecha,Hora,Oficina,Soporte,Descripcion,Puesto,Bien,IP,MAC,Observacion,Estatus FROM Reportes")        
        datos = puntero.fetchall()
        conectar.close()
        
        self.visordereportes.setRowCount(len(datos))
        
        #-----------------------------------------------------------------------
        fila = 0
        columna = 0
        limite=len(datos)
        while fila < limite:    
            datotuple = datos[fila]
            while columna < 12:
                elementodetuple=str(datotuple[columna])
                datoparamostrar = QtWidgets.QTableWidgetItem(elementodetuple)        
                self.visordereportes.setItem(fila,columna,datoparamostrar)
                columna=columna+1                
            columna=0
            fila=fila+1
        #-----------------------------------------------------------------------

            
        
    def closeEvent(self, event):        
        close = QtWidgets.QMessageBox.question(self,
        "Advertencia ","Volvera al menu inicio", 
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)                    
        if close == QtWidgets.QMessageBox.Yes:                
            event.accept()
        else:    
            event.ignore()

class registro(QtWidgets.QDialog, Ui_MRegistro):
    
    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        fecha=datetime.now()
        tfecha= fecha.strftime("%d/%m/%y")
        self.mfecha.setText(tfecha)
 
        self.cargardatos.clicked.connect(self.guardarreporte)
        self.eoficina.activated.connect(self.cargarlistadepuestos)
        self.esoporte.activated.connect(self.cargarsoportes)
        
    def guardarreporte(self):
        
        fecha=datetime.now()
        tid=fecha.strftime("%y%d%m%H%M%S")
        
        inffecha       = fecha.strftime("%d/%m/%y")
        infid          = int(tid)
        infturno       = self.eturno.currentText()
        infoficina     = self.eoficina.currentText()
        infsoporte     = self.esoporte.currentText()
        infdescripcion = self.edescripcion.currentText()
        infpuesto      = self.epuestos.currentText()
        infbien        = self.ebien.text()
        infip          = self.eip.text()
        infmac         = self.emac.text()
        infnota        = self.enota.text()
        infestatus     = self.eestatus.currentText()
        
        data =(infid,inffecha,infturno,infoficina,infsoporte,infdescripcion,infpuesto,infbien,infip,infmac,infnota,infestatus)
        puntero.execute("""INSERT INTO Reportes
        (InfID,Fecha, Hora,  Oficina, Soporte,Descripcion, Puesto, Bien, IP, MAC, Observacion, Estatus)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""", data)                
        conectar.commit()
        
        QtWidgets.QMessageBox.information(self, "Información", 
        """Se registro correctamente""", QtWidgets.QMessageBox.Ok)
         
                
    def cargarsoportes(self):
        
        self.edescripcion.setItemText(0,"")
        self.edescripcion.setItemText(1,"")
        self.edescripcion.setItemText(2,"")
        self.edescripcion.setItemText(3,"")
        self.edescripcion.setItemText(4,"")
        self.edescripcion.setItemText(5,"")
        self.edescripcion.setItemText(6,"")
        self.edescripcion.setItemText(7,"")
        self.edescripcion.setItemText(8,"")
        self.edescripcion.setItemText(9,"")
        self.edescripcion.setItemText(10,"")
        self.edescripcion.setItemText(11,"")
        
        soporte = self.esoporte.currentText()
        
        if soporte == "REDES":
            self.edescripcion.setItemText(0,"Asignación de ip a equipos.")
            self.edescripcion.setItemText(1,"Revisión de duplicidad de ip")
            self.edescripcion.setItemText(2,"Revisión del cableado de red")
            self.edescripcion.setItemText(3,"Revisión de teléfono voz-ip")
            self.edescripcion.setItemText(4,"Configuración de proxy.")
            self.edescripcion.setItemText(5,"Monitoreo., revisión y configuración de VPN")
            self.edescripcion.setItemText(6,"Levantamiento de información IP/MAC")
            self.edescripcion.setItemText(7,"Configuración de RED macro")
            self.edescripcion.setItemText(8,"Configuración de equipos WI-FI")
            
        elif soporte == "SERVIDORES":
            self.edescripcion.setItemText(0,"Creación de usuario")
            self.edescripcion.setItemText(1,"Asignación de carpeta compartida")
            self.edescripcion.setItemText(2,"Recuperación de usuario y contraseña")
            self.edescripcion.setItemText(3,"Recuperación de contraseña")
            self.edescripcion.setItemText(4,"Entrega de usuario.")
            self.edescripcion.setItemText(5,"Problema de acceso a la carpeta compartida")
            
        elif soporte == "DESARROLLO":
            self.edescripcion.setItemText(0,"Revisión de los servicios web")
            
        elif soporte == "IMPRESORAS":
            self.edescripcion.setItemText(0,"Instalación de software de impresoras")
            self.edescripcion.setItemText(1,"Configuración de impresoras en red")
            self.edescripcion.setItemText(2,"Asignación de IP a la impresora en red")
            self.edescripcion.setItemText(3,"Instalación local de impresora")
            self.edescripcion.setItemText(4,"Instalación fisica de impresora")
            self.edescripcion.setItemText(5,"Cambio de cartucho de impresora")
            self.edescripcion.setItemText(6,"Soporte a hoja atascada en impresora")
            self.edescripcion.setItemText(7,"Configuración de impresora en equipo")
            
        elif soporte == "EVENTOS":
            self.edescripcion.setItemText(0,"Instalación de los equipos de sonido y video.")
            self.edescripcion.setItemText(1,"Desinstalación de los equipos de sonido y video.")
            self.edescripcion.setItemText(2,"Supervisión del uso de los equipos utilizados durante los eventos")
            self.edescripcion.setItemText(3,"Manejo de los equipos de sonido y video durante los eventos")
            
        elif soporte == "GENERAL":
            self.edescripcion.setItemText(0,"Registro de la documentación de las estación de trabajo de la SUNAD")
            self.edescripcion.setItemText(1,"Apoyo en la movilización e instalación de equipos en los puestos de trabajo")
            self.edescripcion.setItemText(2,"Mantenimiento correctivo y preventivo de los equipos de computación")
            self.edescripcion.setItemText(3,"Revisión de hardware")
            self.edescripcion.setItemText(4,"Revisión de software")
            self.edescripcion.setItemText(5,"Asesorías en el uso del software")
            self.edescripcion.setItemText(6,"Asesorías en el uso del hardware")
            
        elif soporte == "INTERNAS":
            self.edescripcion.setItemText(0,"Revisión de los bienes asignados a la oficina")
            self.edescripcion.setItemText(1,"Capacitación y supervisión del personal nuevo ingreso")
            self.edescripcion.setItemText(2,"Planificación y ejecución de actividades programadas")
            self.edescripcion.setItemText(3,"Realización de informes técnicos")
            self.edescripcion.setItemText(4,"Realización de actas de préstamos")
            self.edescripcion.setItemText(5,"Realización de actas de entrega de equipos")
            self.edescripcion.setItemText(6,"Registro de actividades")
            self.edescripcion.setItemText(7,"Mantenimiento correctivo y preventivo de los equipos de computación")
            self.edescripcion.setItemText(8,"Actualización de las imágenes de clonación de Linux")
            self.edescripcion.setItemText(9,"Actualización de las imágenes de clonación de Windows")
            self.edescripcion.setItemText(10,"Actualización los paquetes de instalación de los software.")
            self.edescripcion.setItemText(11,"Creación de manuales de procedimientos")
            self.edescripcion.setItemText(12,"Asesorías en la adquisición de equipos")
            self.edescripcion.setItemText(13,"Supervisión de actividades macros")
            self.edescripcion.setItemText(14,"Recepción y entrega de comunicaciones internas y externas")
            self.edescripcion.setItemText(15,"Realización de memorándums.")
            self.edescripcion.setItemText(16,"Control de asistencia e inasistencia.")

        
    def cargarlistadepuestos(self):
        self.epuestos.setItemText(0,"")
        self.epuestos.setItemText(1,"")
        self.epuestos.setItemText(2,"")
        self.epuestos.setItemText(3,"")
        self.epuestos.setItemText(4,"")
        self.epuestos.setItemText(5,"")
        self.epuestos.setItemText(6,"")
        self.epuestos.setItemText(7,"")
        self.epuestos.setItemText(8,"")
        self.epuestos.setItemText(9,"")
        self.epuestos.setItemText(10,"")
        self.epuestos.setItemText(11,"")
        self.epuestos.setItemText(12,"")
        self.epuestos.setItemText(13,"")
        self.epuestos.setItemText(14,"")
        self.epuestos.setItemText(15,"")
        self.epuestos.setItemText(16,"")
        self.epuestos.setItemText(17,"")
        self.epuestos.setItemText(18,"")
        self.epuestos.setItemText(19,"")
        self.epuestos.setItemText(20,"")
        self.epuestos.setItemText(21,"")
        self.epuestos.setItemText(22,"")
        self.epuestos.setItemText(23,"")
        self.epuestos.setItemText(24,"")
        
        oficina = self.eoficina.currentText()
        
        if oficina == "CAE":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            
            contenedor = self.mapa
            imagen = QPixmap("MCAE.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "ENFERMERIA":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            
            contenedor = self.mapa
            imagen = QPixmap("MSM.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "ADMINISTRACIÓN":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            self.epuestos.setItemText(13,"13")
            self.epuestos.setItemText(14,"14")
            self.epuestos.setItemText(15,"15")
            
            contenedor = self.mapa
            imagen = QPixmap("MADMIN.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "GESTIÓN HUMANA":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            self.epuestos.setItemText(13,"13")
            self.epuestos.setItemText(14,"14")
            self.epuestos.setItemText(15,"15")
            self.epuestos.setItemText(16,"16")
            self.epuestos.setItemText(17,"17")
            self.epuestos.setItemText(18,"18")
            self.epuestos.setItemText(19,"19")
            self.epuestos.setItemText(20,"20")
            
            contenedor = self.mapa
            imagen = QPixmap("MGH.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "PRESIDENCIA":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            
            contenedor = self.mapa
            imagen = QPixmap("MPRESI.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "PLANIFICACIÓN":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            
            contenedor = self.mapa
            imagen = QPixmap("MPLANIFICACION.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "PRENSA":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            self.epuestos.setItemText(13,"13")
            self.epuestos.setItemText(14,"14")
            self.epuestos.setItemText(15,"15")
            self.epuestos.setItemText(16,"16")
            self.epuestos.setItemText(17,"17")
            self.epuestos.setItemText(18,"18")
            
            contenedor = self.mapa
            imagen = QPixmap("MPRENSA.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "RED NACIONAL":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            self.epuestos.setItemText(13,"13")
            self.epuestos.setItemText(14,"14")
            
            contenedor = self.mapa
            imagen = QPixmap("MRN.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "DEMANDA":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            self.epuestos.setItemText(13,"13")
            self.epuestos.setItemText(14,"14")
            self.epuestos.setItemText(15,"15")
            self.epuestos.setItemText(16,"16")
            self.epuestos.setItemText(17,"17")
            self.epuestos.setItemText(18,"18")
            self.epuestos.setItemText(19,"19")
            self.epuestos.setItemText(20,"20")
            self.epuestos.setItemText(21,"21")
            self.epuestos.setItemText(22,"22")
            self.epuestos.setItemText(23,"23")
            self.epuestos.setItemText(24,"24")
            
            contenedor = self.mapa
            imagen = QPixmap("MDEMANDA.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "INTERNACIONALES":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            
            contenedor = self.mapa
            imagen = QPixmap("MINTER.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "DESPACHO":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            
            contenedor = self.mapa
            imagen = QPixmap("NOIMAGEN.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)    
            
        elif oficina == "OVD":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            self.epuestos.setItemText(13,"13")
            self.epuestos.setItemText(14,"14")
            self.epuestos.setItemText(15,"15")
            self.epuestos.setItemText(16,"16")
            self.epuestos.setItemText(17,"17")
            self.epuestos.setItemText(18,"18")
            self.epuestos.setItemText(19,"19")
            self.epuestos.setItemText(20,"20")
            
            contenedor = self.mapa
            imagen = QPixmap("MOVD.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "CONSULTORIA":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            
            contenedor = self.mapa
            imagen = QPixmap("MCONSUL.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "OSTIC":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            self.epuestos.setItemText(13,"13")
            self.epuestos.setItemText(14,"14")
            self.epuestos.setItemText(15,"15")
            self.epuestos.setItemText(16,"16")
            self.epuestos.setItemText(17,"17")
            self.epuestos.setItemText(18,"18")
            self.epuestos.setItemText(19,"19")
            self.epuestos.setItemText(20,"20")
            self.epuestos.setItemText(21,"21")
            self.epuestos.setItemText(22,"22")
            self.epuestos.setItemText(23,"23")
            self.epuestos.setItemText(24,"24")
            
            contenedor = self.mapa
            imagen = QPixmap("MOSTIC.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "OFERTA":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            self.epuestos.setItemText(6,"6")
            self.epuestos.setItemText(7,"7")
            self.epuestos.setItemText(8,"8")
            self.epuestos.setItemText(9,"9")
            self.epuestos.setItemText(10,"10")
            self.epuestos.setItemText(11,"11")
            self.epuestos.setItemText(12,"12")
            self.epuestos.setItemText(13,"13")
            self.epuestos.setItemText(14,"14")
            self.epuestos.setItemText(15,"15")
            self.epuestos.setItemText(16,"16")
            self.epuestos.setItemText(17,"17")
            self.epuestos.setItemText(18,"18")
            self.epuestos.setItemText(19,"19")
            self.epuestos.setItemText(20,"20")
            self.epuestos.setItemText(21,"21")
            self.epuestos.setItemText(22,"22")
            self.epuestos.setItemText(23,"23")
            self.epuestos.setItemText(24,"24")
            
            contenedor = self.mapa
            imagen = QPixmap("MOFERTA.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "SEGURIDAD":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            
            contenedor = self.mapa
            imagen = QPixmap("MSEGURIDAD.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "CORRESPONDENCIA":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            
            contenedor = self.mapa
            imagen = QPixmap("MCORRESPONDENCIA.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "SERV. GENERALES":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            self.epuestos.setItemText(5,"5")
            
            contenedor = self.mapa
            imagen = QPixmap("MSERG.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "CEAD":
            self.epuestos.setItemText(0,"INDEFINIDO")
            
            contenedor = self.mapa
            imagen = QPixmap("NOIMAGEN.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "TRANSPORTE":
            self.epuestos.setItemText(1,"1")
            self.epuestos.setItemText(2,"2")
            self.epuestos.setItemText(3,"3")
            self.epuestos.setItemText(4,"4")
            
            contenedor = self.mapa
            imagen = QPixmap("MTRANSPORTE.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)
            
        elif oficina == "OTRA INSTITUCIÓN":
            
            self.epuestos.setItemText(0,"INDEFINIDO")
            
            contenedor = self.mapa
            imagen = QPixmap("NOIMAGEN.jpg").scaled(500,300)
            contenedor.setPixmap(imagen)     
            
    def closeEvent(self, event):        
        close = QtWidgets.QMessageBox.question(self,
        "Advertencia ","Volvera al menu inicio", 
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)                    
        if close == QtWidgets.QMessageBox.Yes:                
            event.accept()
        else:    
            event.ignore()  
            
    
#------------------------------------------------------------------------------#
class inicio(QtWidgets.QMainWindow, Ui_MInicio):
    
    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.idatos.clicked.connect(self.bidatos)
        self.cdatos.clicked.connect(self.bcdatos)
            
    def bidatos(self):
        registro(self).exec_()
    
    def bcdatos(self):
        consulta(self).exec_()
    
    def closeEvent(self, event):        
        close = QtWidgets.QMessageBox.question(self,
        "Advertencia ","¿Desea cerrar el sistema?", 
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)                    
        if close == QtWidgets.QMessageBox.Yes:                
            event.accept()
        else:    
            event.ignore()
#------------------------------------------------------------------------------#
if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = inicio()
    window.show()
    app.exec_()