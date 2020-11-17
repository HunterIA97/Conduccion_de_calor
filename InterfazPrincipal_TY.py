"""
InterfazPrincipal
=====
Created on  Nov 2020

@author: Equipo 4 GeoMaC

Este programa contiene la interfaz grafica principal generada con la biblioteca Tkinter para 
el problema de conducción de calor en estado estacionario.

Funciónes que contiene 
----------------------------------------------
abrirventanaMetodo1
    Ventana que solicita al usuario la información necesaria para calcular el problema
    de conducción estacionaria con y sin fuentes

CasteoLista
    Función que permite castear y comprimir los valores de entrada del ususario
    
abrirventanaMetodo2
   Ventana que solicita al usuario la información necesaria para calcular el problema
    de calibración 1

abrirventanaMetodo3
   Ventana que solicita al usuario la información necesaria para calcular el problema
    de calibración 2

abrirventanaMetodo4
   Ventana que solicita al usuario la información necesaria para calcular el problema
    de calibración 3

validar
    Función que verifica la opción a ejecutar seleccionada por el usuario


"""
#Importamos las librerias
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#Importamos las funciones desarrolladas
from FuncProj_TY import *

global Long,T1,T2,kt,Nodos,nQuo,listArg

#Definimos cada una de las ventanas nuevas que se abrirán
def abrirventanaMetodo1():
    """
    Función que contiene la ventana que solicita los datos de entrada 
    al usuario en el caso de conducción estacionaria con y sin fuentes.
    
    Parameters
    ----------
    Ningún parámetro de entrada
    
    Returns
    -------
    Ningún parámetro de salida
 
    """
    win2=tk.Toplevel(ventana)#Permite crear una ventana que tendra los atributos de la ventana principal
    win2.title("Dirichlet")
    win2.geometry("450x450+500+0")#Tamaño+posición
    win2.configure(background="#F49729")
     
    l1 = Label(win2, text='Longitud del conductor: ',bg="green",fg="white")
    l2 = Label(win2, text='Temperatura frontera A: ',bg="green",fg="white")
    l3 = Label(win2, text='Temperatura frontera B: ',bg="green",fg="white")
    l4 = Label(win2, text='Condcuctividad térmica: ',bg="green",fg="white")
    l6 = Label(win2, text='Numero de nodos: ',bg="green",fg="white")
    l7 = Label(win2, text='Numero de fuentes/sumideros: ',bg="green",fg="white")
   
    #Ubicamos cada una de las etiquetas en la ventana
    l1.grid(row=0,sticky="nsew", padx=15, pady=15)
    l2.grid(row=20,sticky="nsew", padx=15, pady=15)
    l3.grid(row=40,sticky="nsew", padx=15, pady=15)
    l4.grid(row=60,sticky="nsew", padx=15, pady=15)
    l6.grid(row=80,sticky="nsew", padx=15, pady=15)
    l7.grid(row=90,sticky="nsew", padx=15, pady=15)


    def CasteoLista():
        """
        Función que obtiene los datos ingresados por el usuario y
        los castea a datos flotantes.

        Parameters
        ----------
        Ningún parámetro de entrada
        
        Returns
        -------
        listArg: float list
            Lista de datos flotantes que se obtuvieron del usuario
 
        """
        listArg=listaCast(float(Long.get()),float(T1.get()),float(T2.get()),float(kt.get()),int(Nodos.get()),int(nQuo.get()))
        return listArg

    #Solicitamos los datos al usuario
    Long = Entry(win2)
    Long.insert(0,'.5')
    T1 = Entry(win2)
    T1.insert(0, '100')
    T2 = Entry(win2)
    T2.insert(0, '500')
    kt = Entry(win2)
    kt.insert(0, '1')
    Nodos = Entry(win2)
    Nodos.insert(0, '6')
    nQuo=Entry(win2)
    nQuo.insert(0,'4')

    #Ubicamos las entradas en la ventana
    Long.grid(row=0, column=20,sticky="nsew", padx=15, pady=15)
    T1.grid(row=20, column=20,sticky="nsew", padx=15, pady=15)
    T2.grid(row=40, column=20,sticky="nsew", padx=15, pady=15)
    kt.grid(row=60, column=20,sticky="nsew", padx=15, pady=15)
    Nodos.grid(row=80, column=20,sticky="nsew", padx=15, pady=15)
    nQuo.grid(row=90, column=20,sticky="nsew", padx=15, pady=15)
    
    #Boton para calcular y graficar
    botonCalc=tk.Button(win2,text="Calcular y Graficar Solución Análitica y Númerica",command=lambda: calcularGraf(CasteoLista()))
    #Boton para leer los datos desde el .txt
    RBtn=tk.Button(win2,text="Leer los datos desde un archivo de texto",command=lambda: RData())

    botonCalc.grid(row=100,column=0, padx=15, pady=15)
    RBtn.grid(row=150,column=0, padx=15, pady=15)


    return()


        
def abrirventanaMetodo2():
    """
    Función que contiene la ventana que solicita los datos de entrada 
    al usuario para la calibración lineal.
    
    Parameters
    ----------
    Ningún parámetro de entrada
    
    Returns
    -------
    Ningún parámetro de salida
    """
    win2=tk.Tk()
    win2.title("Calibracion Linel")
    win2.geometry("350x210+500+200")#Tamaño+posición
    win2.configure(background="#2E2E2E")

    e2=tk.Label(win2,text="Datos de entrada",bg="#2E2E2E", fg="#E4AB3B", font=('Helvetica', 12))
    e2.grid(row=0,sticky="nsew", padx=15, pady=15)
    l1 = Label(win2, text='Longitud de la barra: ',bg="green",fg="white")
    l2 = Label(win2, text='Número de nodos: ',bg="green",fg="white")
    l1.grid(row=5,sticky="nsew", padx=15, pady=15)
    l2.grid(row=20,sticky="nsew", padx=15, pady=15)
    Long = Entry(win2)
    Long.insert(0,'.5')
    Ns = Entry(win2)
    Ns.insert(0, '6')
    Long.grid(row=5, column=20,sticky="nsew", padx=15, pady=15)
    Ns.grid(row=20, column=20,sticky="nsew", padx=15, pady=15)
    opcCond = 1
    opcTemp = 1
    btnContin1=tk.Button(win2,text="Continuar", bg = "#E4AB3B" ,fg = 'black',command=lambda: caliLineal(Long.get(), Ns.get(), opcCond, opcTemp))
    btnContin1.grid(row=100,sticky="nsew", padx=15, pady=15)

    #MenúCalibracion1:
    menubar3 = Menu(win2)
    helpmenu3 = Menu(menubar3, tearoff=0)
    helpmenu3.add_command(label="Help", command=infoPrograma)
    helpmenu3.add_command(label="About...", command= infoEquipo)
    menubar3.add_cascade(label="Help", menu=helpmenu3)
    win2.config(menu=menubar3)
    return()


def abrirventanaMetodo3():
    """
    Función que contiene la ventana que solicita los datos de entrada 
    al usuario para la calibración 1.
    
    Parameters
    ----------
    Ningún parámetro de entrada
    
    Returns
    -------
    Ningún parámetro de salida

    """

    win2=tk.Tk()
    win2.title("Calibración 1")
    win2.geometry("470x200+500+200")#Tamaño+posición
    win2.configure(background="#2E2E2E")
    e2=tk.Label(win2,text="Calibración 01",bg="#2E2E2E",fg="#E4AB3B", font=('Helvetical', 12))
    e2.grid(row=1,sticky="nsew", padx=15, pady=15)
    e3 = tk.Label(win2, text = '''
        Esta calibración aún está en proceso de ser implementada.     
        Por favor utiliza el siguiente botón para llamar una terminal     
        y ejecutar el programa 'Cali01.py' desde ahi:''', bg = '#FFFB00', fg = 'black', font=('Helvetica', 12))
    e3.grid(row=3)

    menubar2 = Menu(win2)
    helpmenu2 = Menu(menubar2, tearoff=0)
    helpmenu2.add_command(label="Help", command=infoPrograma)
    helpmenu2.add_command(label="About...", command= infoEquipo)
    menubar2.add_cascade(label="Help", menu=helpmenu2)
    win2.config(menu=menubar2)
    def newcmd():
        os.system("start /wait cmd /k {command}")
    btnContin1=tk.Button(win2,text="Abrir nueva terminal", bg = "#E4AB3B" ,fg = 'black',command=newcmd)
    btnContin1.grid(row=20,sticky="nsew", padx=15, pady=15)
    return()

def abrirventanaMetodo4():
    '''
    Función que contiene la ventana que solicita los datos de entrada 
    al usuario para la calibración 2.
    
    Parameters
    ----------
    Ningún parámetro de entrada
    
    Returns
    -------
    Ningún parámetro de salida

    '''
    win2=tk.Tk()
    win2.title("Calibración 2")
    win2.geometry("470x200+500+200")#Tamaño+posición
    win2.configure(background="#2E2E2E")
    e2=tk.Label(win2,text="Calibración 02",bg="#2E2E2E",fg="#E4AB3B", font=('Helvetical', 12))
    e2.grid(row=1,sticky="nsew", padx=15, pady=15)
    e3 = tk.Label(win2, text = '''
        Esta calibración aún está en proceso de ser implementada.     
        Por favor utiliza el siguiente botón para llamar una terminal     
        y ejecutar el programa 'Cali02.py' desde ahi:''', bg = '#FFFB00', fg = 'black', font=('Helvetica', 12))
    e3.grid(row=3)

    menubar2 = Menu(win2)
    helpmenu2 = Menu(menubar2, tearoff=0)
    helpmenu2.add_command(label="Help", command=infoPrograma)
    helpmenu2.add_command(label="About...", command= infoEquipo)
    menubar2.add_cascade(label="Help", menu=helpmenu2)
    win2.config(menu=menubar2)
    def newcmd():
        os.system("start /wait cmd /k {command}")
    btnContin1=tk.Button(win2,text="Abrir nueva terminal", bg = "#E4AB3B" ,fg = 'black',command=newcmd)
    btnContin1.grid(row=20,sticky="nsew", padx=15, pady=15)
    return()

def abrirventanaMetodo5():
    """
    Función que contiene la ventana que solicita los datos de entrada 
    al usuario para la calibración 3.
    
    Parameters
    ----------
    Ningún parámetro de entrada
    
    Returns
    -------
    Ningún parámetro de salida
 
    """
    win2=tk.Tk()#Permite crear una ventana que tendra los atributos de la ventana principal
    win2.title("Calibración 3")
    win2.geometry("470x200+500+200")#Tamaño+posición
    win2.configure(background="#2E2E2E")
    e2=tk.Label(win2,text="Calibración 03",bg="#2E2E2E",fg="#E4AB3B", font=('Helvetical', 12))
    e2.grid(row=1,sticky="nsew", padx=15, pady=15)
    e3 = tk.Label(win2, text = '''
        Esta calibración aún está en proceso de ser implementada.     
        Por favor utiliza el siguiente botón para llamar una terminal     
        y ejecutar el programa 'Cali03.py' desde ahi:''', bg = '#FFFB00', fg = 'black', font=('Helvetica', 12))
    e3.grid(row=3)

    menubar2 = Menu(win2)
    helpmenu2 = Menu(menubar2, tearoff=0)
    helpmenu2.add_command(label="Help", command=infoPrograma)
    helpmenu2.add_command(label="About...", command= infoEquipo)
    menubar2.add_cascade(label="Help", menu=helpmenu2)
    win2.config(menu=menubar2)
    def newcmd():
       """
    Función que nos permite abrir una nueva terminal para ejecutar las calibraciones.
    
    Parameters
    ----------
    Ningún parámetro de entrada
    
    Returns
    -------
    Ningún parámetro de salida
 
    """
    os.system("start /wait cmd /k {command}")
    btnContin1=tk.Button(win2,text="Abrir nueva terminal", bg = "#E4AB3B" ,fg = 'black',command=newcmd)
    btnContin1.grid(row=20,sticky="nsew", padx=15, pady=15)
    return()


#Ventana principal
ventana=tk.Tk()
ventana.title("Transferencia de Calor 1D")
ventana.geometry('380x225')
ventana.configure(background="#2E2E2E")

#Barra de menu dentro de la ventana principal:
menubar = Menu(ventana)
#Menu 'File':
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=ventana.quit)
#Menu 'Help':
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=infoPrograma)
helpmenu.add_command(label="About...", command= infoEquipo)

menubar.add_cascade(label="Help", menu=helpmenu)

#Vamos a poner una etiqueta para que ahí el ususario escoga el metodo
e1=tk.Label(ventana,text="MENU PRINCIPAL",bg="#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12))
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)

seleccionador = IntVar()
R1 = Radiobutton(ventana, text='Condiciones tipo Dirichlet con y sin fuentes', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12) ,variable = seleccionador, value=1)
R1.pack( anchor = W )
#R2 = Radiobutton(ventana, text='Calibración Lineal', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12), variable = seleccionador, value=2)
#R2.pack( anchor = W )
R3 = Radiobutton(ventana, text='Calibración 1', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12), variable = seleccionador, value=3)
R3.pack( anchor = W )
R4 = Radiobutton(ventana, text='Calibración 2', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12), variable = seleccionador, value=4)
R4.pack( anchor = W )
R5 = Radiobutton(ventana, text='Calibración 3', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12), variable = seleccionador, value=5)
R5.pack( anchor = W )

#Condicion para verificar el caso a implementar
def validar():
    """
    Función que valida la opción seleccionada por el usuario y ejecuta
    una función según sea el caso seleccionado
    Parameters
    ----------
    Ningún parámetro de entrada
        
    Returns
    -------
    Ningún parametro de salida

    """
    if seleccionador.get()==1:
        abrirventanaMetodo1()
    elif seleccionador.get()==2:
        abrirventanaMetodo2()
    elif seleccionador.get()==3:
        abrirventanaMetodo3()
    elif seleccionador.get()==4:
        abrirventanaMetodo4()
    elif seleccionador.get()==5:
        abrirventanaMetodo5()
    return()

#Boton para seleccionar el metodo
botonVerif=tk.Button(ventana,text="Validar selección",bg="#E4AB3B",fg="black",command=validar)
botonVerif.pack(side=tk.TOP)

ventana.config(menu=menubar)
ventana.mainloop()







