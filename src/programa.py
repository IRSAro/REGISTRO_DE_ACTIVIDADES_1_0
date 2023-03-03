# -*- coding: utf-8 -*-
# CODIGO PARA EL REGISTRO DE ACTIVIDADES UTILIZANDO PYQT5 Y PYTHON 3.8
# NOMBRE: REGISTRO DE ACTIVIDADES 1.0
# AUTOR: ROSANA SANCHEZ
# CORREO: rosaxna_31@hotmail.es

#------------------------------------------------------------------------------#
#Importamos todas las caracteristicas del entorno grafico
#Cada interfas es creada en otro documento .py para tener comodidad al realizar 
#modificacionbes

from inicio import *
from registro import *
from consulta import *

#------------------------------------------------------------------------------#
from datetime  import date, time, datetime #libreria de para el uso de tiempo
from sqlite3 import connect                # Libreria para la base de datos 

#------------------------------------------------------------------------------#
#Conectamos con el archivo de db al que llamamos DATOS

conectar = connect('DATOS.db')   
puntero = conectar.cursor()

#------------------------------------------------------------------------------#
#Se crea la tabla donde estaran los campos que se van a registrar y conectamos
# InfID = Numero de identificación del registro
# Fecha = Fecha de cuando se creo el registro
# Hora = Horario en el que fue realizado la actividad
# Oficina = Para quien se realizo la actividad y o el lugar donde se realizo
# Soporte = Que tipo de soporte / actividad se realizo en esa oficina
# Descripcion = Descripcio de la activiad realizada
# Puesto = Puesto de trabajo yo ubicacion del computador de la oficina
# Bien = Numero de bien muble del equipo si se requiere
# IP / MAC = imformacion opcional 
# Observacion = Algun comentario o nota para complementar el registro
# Estatus = Indica si la activida fue culminada, esta en proceso o no se culmino

puntero.execute("""CREATE TABLE IF NOT EXISTS Reportes (InfID INTEGER PRIMARY 
KEY AUTOINCREMENT, Fecha TEXT, Hora TEXT,  Oficina TEXT, Soporte TEXT, 
Descripcion TEXT, Puesto TEXT, Bien TEXT, IP TEXT, MAC TEXT, Observacion TEXT, 
Estatus TEXT)""")        
conectar.commit()

#------------------------------------------------------------------------------#
# Nota: 1. los nombres de las class son indiferentes a los llamados en from
#       2. Qtwidget.QDialog son SubClass de los from llamados registro y 
#          consulta.
#       3. QDialog como su nombre lo indica es una ventana emergente para 
#          solicitar/consultar informacón/dar información.
#       4. QMainWindow es la ventana que soportara todos los Widget utilizados
#           en el programa.
#
#       5. Estructura de las SubClass:
#
#   class "Nombre"(QtWidgets.QDialog,"Nombre de la class del .py de registro o consulta"): 
#
#       def __init__(self, *args, **kwargs):
#           #Despliega Qdialog como si fuera un QMainWindow
#           #con todas las caracteristicas de la class del .py 
#           QtWidgets.QMainWindow.__init__(self, *args, **kwargs) 
#           self.setupUi(self)
#
#        6. Estructura de la Class principal:
#       
#   class "Nombre"(QtWidgets.QMainWindow, "Nombre de la class del .py de inicio"):    
#       def __init__(self, *args, **kwargs):        
#           QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
#           self.setupUi(self)
#
#   if __name__ == "__main__":
#       app = QtWidgets.QApplication([])
#       window = "Nombre de la class principal"()
#       window.show()
#       app.exec_()
#
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# Clase donde podremos ver todos los reportes utilizando QTableWidget 
#
class consulta(QtWidgets.QDialog, Ui_MConsulta): 

    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        #Conectamos a la base de datos y guardamos los datos
        
        conectar = connect('DATOS.db')  
        puntero = conectar.cursor()      
        puntero.execute("SELECT InfID,Fecha,Hora,Oficina,Soporte,Descripcion,Puesto,Bien,IP,MAC,Observacion,Estatus FROM Reportes")        
        
        datos = puntero.fetchall()
        conectar.close()
        
        # datos es una variable tipo list con tuple. ejem
        # 1.Tuple 1
        # 2.Tuple 2
        # 3.Tuple 3
        
        # Tuple es una lista de elementos dentro de usa sola variable separados 
        # por comas. ejem
        # lista = ("primero","segundo","tercero","...")
        
        #len(datos) devuelve un valor entero con la cantidad de elementos en la 
        #lista.
        #setRowCount crea tantas filas como le sean indicadas en la tabla, 
        #en este caso la cantidad de reportes es proporcinal a lo que indica la 
        #funcion len.
        
        limite=len(datos) #cantidad de filas de la list
        
        #self."Nombre de el objeto".creamosfilas(numero de filas)
        
        self.visordereportes.setRowCount(limite)
        
        #-----------------------------------------------------------------------
        # Para mostrar los reportes tenemos que movilizarnos atraves de la list 
        # con tuples por ello utilizaremos la siguiente rutina:
        
        fila = 0   
        columna = 0
        
        while fila < limite:
            
            datotuple = datos[fila] #Guardamos un tuple de la list
            
            while columna < 12:
                
                # Nos desplazamos por cada elemto del tuple para mostrarlo, el
                # str combierte cualquir elemento en una cadena de caracteres 
                # para poder mostralo en el Qtable
                
                elementodetuple=str(datotuple[columna])
                
                # Combertimos el elemento del tuple en un item de Qtable
                datoparamostrar = QtWidgets.QTableWidgetItem(elementodetuple)
                
                # Mostramos los datos en la fila y la columna correspondientes 
                # con la siguente liena
                
                self.visordereportes.setItem(fila,columna,datoparamostrar)
                columna=columna+1   
                
            # Una vez que termine de mostrar la fila correspondiente llevamos
            # la columna en 0 y incrementamos la fila para mostrar el siguiente 
            # tuple
            
            columna=0
            fila=fila+1
        #-----------------------------------------------------------------------
         
    #--------------------------------------------------------------------------#    
    
    # Funcion incluida en PyQt5 donde al cerrar la ventana podemos elegir la 
    # si continuar cerrando o cancelar, el mensaje puede cambiar.
    
    def closeEvent(self, event):
        
        close = QtWidgets.QMessageBox.question(self,
        "Advertencia ","Volvera al menu inicio", # El mensaje puede cambiar 
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)                    
        if close == QtWidgets.QMessageBox.Yes:                
            event.accept()
        else:    
            event.ignore()
    #--------------------------------------------------------------------------#
    
#------------------------------------------------------------------------------#
# Clase donde podremos registrar cada uno de los reportes
#    
class registro(QtWidgets.QDialog, Ui_MRegistro):
    
    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        # Tomamos la fecha actual
        fecha=datetime.now()
        # Guardamos la fecha como una cadena de caracteres con formato dd/mm/aa
        tfecha= fecha.strftime("%d/%m/%y")
        
        #Mostramos la fecha con el Widget mfecha del registro.py
        self.mfecha.setText(tfecha)
        
        # En el programa tenemos dos ComboBox que cambian su contenido segun 
        # lo requerido, si se activa cada uno muestra elementos diferente en los
        # ComboBox restantes.
        
        self.eoficina.activated.connect(self.cargarlistadepuestos)
        self.esoporte.activated.connect(self.cargarsoportes)
        
        #Conecta el Boton cargardatos con la rutina para guardar el reporte
        self.cargardatos.clicked.connect(self.guardarreporte)
    
    # Carga la informacion del ComboBox de descripcion dependiendo de lo que 
    # este el ComboBox de Soporte
    
    def cargarsoportes(self):
        
        # Lista del comboxBox de descripcion (numero de lista, texto)
        
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
        self.edescripcion.setItemText(12,"")
        self.edescripcion.setItemText(13,"")
        self.edescripcion.setItemText(14,"")
        self.edescripcion.setItemText(15,"")
        self.edescripcion.setItemText(16,"")
        
        # Agarramos lo que esta en el combox de soportes y realizamos 
        # las correspondientes comparaciones, para mostrar segun lo indicado.
        
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

    # Agarramos lo que esta en el combox de oficina y realizamos 
    # las correspondientes comparaciones, para mostrar la cantidad de puesto y 
    # el  mapa que muestra donde se encuentran ubicados esos puestos de trabajo. 
    
    def cargarlistadepuestos(self):
        
        # Lista del comboxBox de los puestos de trabajo (numero de lista, texto)
        
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
        
        # El contenedor erreda todas las propiedades de el Widget para cargar la
        # imagen, Pixelamos y le damo la escla que tiene el self.mapa para 
        # mostrarlo con contenedor.setPixmap(imagen).
        
        contenedor = self.mapa
        imagen = QPixmap("NOIMAGEN.jpg").scaled(500,300)
        contenedor.setPixmap(imagen)
        
        # Agarramos lo que esta en el combox de oficina y realizamos 
        # las correspondientes comparaciones, para mostrar segun lo indicado.
        
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
    
    
    #Funcion donde si le damos click al boton guardar 
    # seleccionamos y guardamos en la base de datos la informacion
    
    def guardarreporte(self):
        
        fecha=datetime.now()
        # El ID es el Key por ende tiene que se una variable int, para esto 
        # seleccionamos en orden años, mes, dia, hora, minuto y segundos para 
        # crear un numero unico consecutivo y lo convertimos en int
        
        tid=fecha.strftime("%y%m%d%H%M%S")
        infid          = int(tid)
        
        inffecha       = fecha.strftime("%d/%m/%y")
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
        
        #Creamos un tuple con los datos ya ingresados
        
        data =(infid,inffecha,infturno,infoficina,infsoporte,infdescripcion,infpuesto,infbien,infip,infmac,infnota,infestatus)
        
        #Insertamos la informacion en la base de datos
        
        puntero.execute("""INSERT INTO Reportes
        (InfID,Fecha, Hora,  Oficina, Soporte,Descripcion, Puesto, Bien, IP, MAC, Observacion, Estatus)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""", data)                
        conectar.commit()
        
        #mostramos una ventana confirmando que se guardaron los datos y continuamos
        
        QtWidgets.QMessageBox.information(self, "Información", 
        """Se registro correctamente""", QtWidgets.QMessageBox.Ok)
        
    def closeEvent(self, event):        
        close = QtWidgets.QMessageBox.question(self,
        "Advertencia ","Volvera al menu inicio", 
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)                    
        if close == QtWidgets.QMessageBox.Yes:                
            event.accept()
        else:    
            event.ignore()
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#
# Clase principal  con QMainWindow que despliega todas las funciones
#

class inicio(QtWidgets.QMainWindow, Ui_MInicio):
    
    def __init__(self, *args, **kwargs):
        
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.idatos.clicked.connect(self.bidatos)
        self.cdatos.clicked.connect(self.bcdatos)
        
    #LLamamos a la class registro        
    def bidatos(self):
        registro(self).exec_()
        
    #llamamos a la class consulta
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
            
if __name__ == "__main__":

    app = QtWidgets.QApplication([])
    window = inicio()
    window.show()
    app.exec_()