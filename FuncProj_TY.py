#importar bibliotecas utiles en el programa
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk #Biblioteca que nos permite trrabajar con la interfaz gráfica
from tkinter import *
from tkinter import messagebox #Biblioteca para mostrar advertencias
from tkinter import filedialog
import os

global Long,T1,T2,kt,Nodos,nQuo,Q,Temp,y,L,TA,TB,k,N,nQ,stuff,Valid


def listaCast(L,TA,TB,k,N,Q):
    '''
    Función que "comprime" en una lista los datos de entrada del usuario para pasarlos como único argumento en una función.
    La función regresa los valores para su uso posterior.

    Parameters
    -------------
    L:float
        Longitud de la barra
    k:float or float array
        Conductividad de la barra, puede ser un solo valor o un arreglo
    N:integer
        Número de nodos en el dominio (incluye los nodos de los extremos)
    TA:float
        Temperatura al inicio del dominio
    TB:float
        Temperatura al final de la barra
    Q:float array
        Arreglo de los valores de las fuentes en el dominio

    Returns
    -------------
    listaCasteo:float list
        Lista que contiene  los datos L,k,N,TA,TB y Q,ingresados por el usuario.
    

    '''
    listaCasteo=[L,TA,TB,k,N,Q]
    return listaCasteo

def CastLs(Tinic,L,TA,TB,k,N):
    '''
    Función que "comprime" en una lista los datos de fuente/sumideros dados por el 
    usuario y genera una matriz de fuentes/sumideros de N-2xQ
    La función regresa los valores para su uso posterior.

    Parameters
    -------------
    Tinic:string list
        Datos de fuentes y sumideros (cada nodo debe estar separado por una coma)
    L:float
        Longitud de la barra
    k:float or float array
        Conductividad de la barra, puede ser un solo valor o un arreglo
    N:integer
        Número de nodos en el dominio (incluye los nodos de los extremos)
    TA:float
        Temperatura al inicio del dominio
    TB:float
        Temperatura al final de la barra

    Returns
    -------------
    L:float
        Longitud de la barra
    k:float or float array
        Conductividad de la barra, puede ser un solo valor o un arreglo
    N:integer
        Número de nodos en el dominio (incluye los nodos de los extremos)
    TA:float
        Temperatura al inicio del dominio
    TB:float
        Temperatura al final de la barra
    Q: ndarray
        Arreglo que contiene los valores de las fuentes

    
    '''
    Q=[-float(i) for i in Tinic.get().split(",")]

    Q=(np.asarray(Q)).reshape((len(Q),1))
    print(Q.shape[0])
    return [L,TA,TB,k,N,Q]
#1) LECTURA DE DATOS

def LecDatos(L,TA,TB,k,N,nQ):
    '''
    Función que genera una lista de datos 

    Parameters
    -------------
    Tinic:string list
        Datos de fuentes y sumideros (cada nodo debe estar separado por una coma)
    L:float
        Longitud de la barra
    k:float or float array
        Conductividad de la barra, puede ser un solo valor o un arreglo
    N:integer
        Número de nodos en el dominio (incluye los nodos de los extremos)
    TA:float
        Temperatura al inicio del dominio
    TB:float
        Temperatura al final de la barra
    nQ:integer
        Numero de fuentes 

    Returns
    -------------
    Tinic:string list
        Datos de fuentes y sumideros (cada nodo debe estar separado por una coma)
    L:float
        Longitud de la barra
    k:float or float array
        Conductividad de la barra, puede ser un solo valor o un arreglo
    N:integer
        Número de nodos en el dominio (incluye los nodos de los extremos)
    TA:float
        Temperatura al inicio del dominio
    TB:float
        Temperatura al final de la barra
    Q:integer
        Numero de fuentes 

    '''
    Q=Crea_Matriz(N-2,1)
    return(L,TA, TB, k, N,Q)

def LectDatos2(L,TA,TB,k,N,nQ):
    '''
    Función que genera una lista de datos 

    Parameters
    -------------
    Tinic:string list
        Datos de fuentes y sumideros (cada nodo debe estar separado por una coma)
    L:float
        Longitud de la barra
    k:float or float array
        Conductividad de la barra, puede ser un solo valor o un arreglo
    N:integer
        Número de nodos en el dominio (incluye los nodos de los extremos)
    TA:float
        Temperatura al inicio del dominio
    TB:float
        Temperatura al final de la barra
    nQ:integer
        Numero de fuentes 

    Returns
    -------------
    Ningun parametro de salida

    '''
    win23=tk.Toplevel()#Permite crear una ventana que tendra los atributos de la ventana principal
    win23.title("Condición Dirichlet Fuentes y Sumideros")
    win23.geometry("620x250+500+0")#Tamaño+posición
    win23.configure(background="#F49729")
    messagebox.showinfo("Fuentes y/o Sumideros","Existen "+str(nQ)+" sumideros y/o fuentes. Indica en cual(es) nodo(s) central(es) se encuentra(n) y su valor")
    l1 = Label(win23, text='Temperatura Inicial en los nodos centrales (No considerar las fronteras) : '+'\n\n'+'Utiliza un signo negativo para el valor aquellos nodos que representen sumideros')
    l1.grid(row=0,sticky="nsew", padx=15, pady=15)

    Tinic = Entry(win23)

    lisTemNodos = ['0,' for i in range(N-2)]; lisTemNodos.pop(-1)
    lisTemNodos.append(lisTemNodos[-1][:1])

    Tinic.insert(0, lisTemNodos)
    Tinic.grid(row=5,sticky="nsew", padx=15, pady=15)
    CalcFuentes=Button(win23,text="Calcular y graficar solución numérica considerando fuentes/sumideros con los datos de entrada de la interfaz",command= lambda: calcularGraf2(CastLs(Tinic,L,TA,TB,k,N)))
    CalcFuentes.grid(row=20,sticky="nsew", padx=15, pady=15)
    LeerArch=Button(win23,text="Leer fuentes/sumideros desde archivo .txt",command= lambda: RFuenSum(L,TA,TB,k,N))           
    LeerArch.grid(row=23,sticky="nsew", padx=15, pady=15)
    

#2) CREACIÓN DE MATRIZ
def Crea_Matriz(n,m):
    """
    Función que crea una matriz con las dimensiones dadas
    """
    return np.zeros((n,m))




# 3) LLENADO DE LAS MATRICES
def Matriz_ll(L,TA,TB,k,N):
    """
    Función que crea las matrices con la información útil
    Utiliza la función Crea_Matriz para crear cada matriz 
    Además calcula algunos valores extra a usar en otro momento
    """

    print("Esta es L:",L)
    print("Esta es k:",k)
    print("Esta es N",N)

    
    #Tamaño de las divisiones
    h=L/(N-1)
    print("Estas es h:",h)
    
    #Cálculo de r

    r=k/(h**2)

    #Matriz de coeficientes
    A=Crea_Matriz(N-2,N-2)
    for i in range(N-2):
        for j in range(N-2):
            if (i==j):
                A[i][j]=-2
            if(np.fabs(i-j)==1):
                A[i][j]=1
    
    #Matriz de temperaturas frontera
    Tf=Crea_Matriz(N-2,1)
    Tf[0]=-TA
    Tf[N-3]=-TB
    
    #Matriz de Temperaturas en todo el dominio
    Temp=Crea_Matriz(N,1)
    Temp[0]=TA
    Temp[N-1]=TB
    
    #Matriz de distancias
    Dist=Crea_Matriz(N,1)
    Dist[0]=0
    for i in range (1,N):
        Dist[i]=Dist[i-1]+h
    return (h,r,A,Tf,Temp,Dist)



#4) IMPRIMIR MATRICES
def Imprime_Matriz(a):
    """
    Funcion de apoyo para imprimir en pantalla la matriz dada
    """
    [n,m]=a.shape
    print('\n')
    for i in range (n):
        for j in range (m):
            print(a[i][j],end=' ')
        print('\n')
    return()

#5) FUNCION ANALITICA CASO 1
def F_Real(TA,TB,L,N):
    """
    Función que calcula la solución analítica
    """

    y=lambda x: TA+x*(TB-TA)/L
    x=np.linspace(0,L,N)
    
    return (x,y(x))

#6) SOLUCION APROXIMADA CASO 1
def Sol_Aprox(A,Tf,Temp,Q,r,N):
    """
    Función que resuelve el sistema de matrices [A][x]=[b] y debuelve la solución
    """

    print(len(Q))
    print(len(Tf+(1/r)))
    
    #Definicion de la matriz b
    b=Tf+(1/r)*Q
    
    #Resolviendo el sistema
    Temp[1:N-1] = np.linalg.solve(A,b)
    
    return Temp

#7) GRAFICAS
def Graf(x,y,nombre,Nx,Ny,linea,titulo):
    """
    Función para realización de gráficas de resultados
    """
    plt.plot(x,y,linea,label=nombre)
    plt.title(titulo)
    plt.xlabel(Nx)
    plt.ylabel(Ny)
    plt.legend()
    plt.grid()
    SavePlot(nombre)

def Graf2fig(x1,x2,y1,y2,nombre,Nx,Ny,linea):
    fig, axes=plt.subplots(1,2)
    #Renglon 0 columna 1
    axes[0].plot(x1,y1,c='r',label="Solución Aproximada ")
    axes[0].set_title("Solución Aproximada")
    axes[0].set_xlabel(Nx)
    axes[0].set_ylabel(Ny)
    axes[0].legend()
    axes[0].grid()

    #Renglon 0 columna 2
    axes[1].scatter(x2,y2,c='b',label="Solución Analítica ")
    axes[1].set_title("Solución Analítica")
    axes[1].set_xlabel(Nx)
    axes[1].set_ylabel(Ny)
    axes[1].legend()
    axes[1].grid()

    plt.tight_layout()









def calcErr1(Temp,y):
    Err=Temp.ravel()-y
    print(Err)
    EucNorm=np.linalg.norm(Err)
    print(EucNorm)
    return EucNorm





#Programa principal
    
def calcularGraf(listArg):

    Ls=[]
    [Ls.append(float(i)) for i in listArg]
    [L,TA,TB,k,N,nQ]=Ls
    N=int(N)
    nQ=int(nQ)
    if nQ ==0:
        [L,TA, TB, k, N,Q]=LecDatos(L,TA,TB,k,N,nQ)
        [h,r,A,Tf,Temp,Dist]=Matriz_ll(L,TA,TB,k,N)
        print('\n\tMatriz de Coeficientes')
        Imprime_Matriz(A)
        print('\n\tMatriz de Temperaturas a lo largo de la barra')
        Imprime_Matriz(Temp)
        print('\n\tMatriz de Temperaturas en fronteras')
        Imprime_Matriz(Tf)
        print('\n\tMatriz de Fuentes')
        Imprime_Matriz(Q)
        [x,y]=F_Real(TA,TB,L,N) 
        Temp=Sol_Aprox(A,Tf,Temp,Q,r,N)
        error1 = calcErr1(Temp,y)
        messagebox.showinfo("Cálculo del Error", "El error calculado es: "+str(error1))
        Graf2fig(Dist,x,Temp,y,'Solución aproximada','Longitud','Temperatura','-bo')
        WDataAnNum("SoluciónSinFuentes",y,Temp,error1)
        #Graf(x,y,'Solución análitica','Distancia','Temperatura','C1--','Solución analítica y numérica')
        plt.show()

        return(Temp,y)
    
    else:
        if nQ>N-2:
            ma=N-2
            messagebox.showinfo("Error", "Puedes tener "+str(ma)+" fuentes y/o sumideros como máximo dados los nodos en los que se está discretizando y las condiciones de frontera"+"\n\n"+" Revisa tus entradas")
        else:
            LectDatos2(L,TA,TB,k,N,nQ)




def calcularGraf2(listArg):
    Ls=[]
    [Ls.append(i) for i in listArg]
    [L,TA,TB,k,N,Q]=Ls
    N=int(N)

    ma=N-2
    if Q.shape[0]!=ma:
        messagebox.showinfo("Error", "Debes tener "+str(ma)+" datos iniciales incluidos fuentes y/o sumideros  dados los nodos en los que se está discretizando y las condiciones de frontera"+"\n\n"+" Revisa tus entradas")
    else:
        #Ls=[]
        #[Ls.append(i) for i in listArg]
        #[L,TA,TB,k,N,Q]=Ls
        N=int(N)
        [h,r,A,Tf,Temp,Dist]=Matriz_ll(L,TA,TB,k,N)
        print('\n\tMatriz de Coeficientes')
        Imprime_Matriz(A)
        print('\n\tMatriz de Temperaturas a lo largo de la barra')
        Imprime_Matriz(Temp)
        print('\n\tMatriz de Temperaturas en fronteras')
        Imprime_Matriz(Tf)
        print('\n\tMatriz de Fuentes')
        Imprime_Matriz(Q)
        [x,y]=F_Real(TA,TB,L,N)
        Temp=Sol_Aprox(A,Tf,Temp,Q,r,N)
        WDataNum("SoluciónFuentesSumideros",Temp)
        Graf(Dist,Temp,'Solución Númerica','Distancia','Temperatura','-bo','Solución analítica considerando fuentes/sumideros')
        plt.show()

    return(Temp,y)



#Lectura de datos desde el archivo y calculo de la solución
def RData():
    '''
    Lectura  almacenamiento y casteo de los datos desde el archivo de texto.

    '''
    archivoDatos=filedialog.askopenfilename(title="Abrir archivo",filetypes=(("Text Files","*.txt"),))
    archivoDatos=open(archivoDatos,'r')
    stuff=archivoDatos.read()
    archivoDatos.close()
    #Almacenamos y casteamos
    Ls=[]
    stuff=stuff.split(',')
    [Ls.append(float(i)) for i in stuff]
    [L,TA,TB,k,N,nQ]=Ls
    N=int(N)
    nq=int(nQ)


    #Calculamos la solución con los datos casteados
    calcularGraf(listaCast(L,TA,TB,k,N,nQ))

    return()

def RFuenSum(L,TA,TB,k,N):
    '''
    Función que lee las fuentes y sumideros dadas por el usuario

    '''
    archivoFuentes=filedialog.askopenfilename(title="Abrir archivo",filetypes=(("Text Files","*.txt"),))
    archivoFuentes=open(archivoFuentes,'r')
    Tinic=archivoFuentes.read()
    archivoFuentes.close()

    Q=[-float(i) for i in Tinic.split(",")]
    print(len(Q))
    Q=(np.asarray(Q)).reshape((len(Q),1))
    #Q=Q.reshape((4,1))
    print(Q)
    #Calculamos la solución con los datos casteados
    calcularGraf2(listaCast(L,TA,TB,k,N,Q))


#Escritura de resultados en .txt para el caso en el que existe una solución real y una analítica.
def WDataAnNum(nombre,Analitica,Numerica,error):
    '''
    Guarda los resultados en un archivo .txt

    '''
    f= open(nombre+".txt","w+")
    f.write("Solución Analítica \r\n" +np.array_str(Analitica)+"\n\n")
    f.write("Solución Numérica \r\n" +np.array_str(Numerica.reshape(1,6))+"\n\n")
    f.write("El error es de : \r\n" +str(error))
    f.close()


def WDataNum(nombre,Numerica):
    '''
    Guarda los resultados en un archivo .txt

    '''
    f= open(nombre+".txt","w+")
    f.write("Solución Numérica \r\n"+np.array_str(Numerica.reshape(1,6)))
    f.close()

def SavePlot(nombre):
    '''
    Guarda las imagenes en jpg
    '''
    plt.savefig(str(nombre)+'.png')


##################################################CALIBRACIONES##################################################################################################


#FUNCIONES PRINCIPALES DE LAS CALIBRACIONES:


#1) LECTURA DE DATOS
def LecDatosCal(L, N,opcCond, opcTemp):
    """
    Función que ayuda en la lectura de datos iniciales del problema
    La función regresa los valores para su uso posterior
    """
    L=float(L)
    N=int(N)
    k=Conductividad(L,N,opcCond)
    [TA,TB,opc]=Lec_Temp(opcTemp, k)
    [Q,h,tipo]=Fuentes(opc,N,L)
    #Cálculo de r
    r=k/(h**2)
    #Matriz de distancias
    Dist=Crea_Matriz(N,1)
    for i in range (1,N):
        Dist[i]=Dist[i-1]+h
    return(L, k, N,TA,TB,Q,h,r,tipo,Dist,opc)

def Conductividad(L,N,opcCond):
    global conduct2
    global k
    if opcCond==1:
        global conduct2
        win23=tk.Toplevel()#Permite crear una ventana que tendra los atributos de la ventana principal
        win23.title("Comportamiento de la conductividad")
        win23.geometry("350x210+500+200")#Tamaño+posición
        win23.configure(background="#2E2E2E")
        menubar = Menu(win23)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=infoConduct1)
        helpmenu.add_command(label="About...", command= infoEquipo)
        menubar.add_cascade(label="Help", menu=helpmenu)
        win23.config(menu=menubar)

        conductEnt = Entry(win23)
        conductEnt.insert(0, '1')
        conductEnt.grid(row=5, column=20,sticky="nsew", padx=15, pady=15)
        l1 = Label(win23, text='Conductividad térmica:',bg="green",fg="white")
        l1.grid(row=5,sticky="nsew", padx=15, pady=15)
        def getCond():
            global k
            k = float(conductEnt.get())
            print(k)
            win23.destroy()
            win23.update()
            return k
        btnContin1=tk.Button(win23,text="Continuar", bg = "#E4AB3B" ,fg = 'black',command=getCond)
        btnContin1.grid(row=100,sticky="nsew", padx=15, pady=15)
        print('K de este ejercicio es:', k)
        return k
    

    elif opcCond==2:
        y=lambda x:np.fabs(np.sin(4*np.pi*x))
        x=np.linspace(0,L,N)
        k=y(x)
        return k
    elif opcCond==3:
        y=lambda x:np.random(x)
        x=np.linspace(0,L,N)
        k=y(x)
        return k
    elif opcCond==4:
        win23=tk.Toplevel()#Permite crear una ventana que tendra los atributos de la ventana principal
        win23.title("Comportamiento de la conductividad")
        win23.geometry("350x210+500+200")#Tamaño+posición
        win23.configure(background="#2E2E2E")
        menubar = Menu(win23)
        filemenu = Menu(menubar, tearoff=0)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=infoConduct1)
        helpmenu.add_command(label="About...", command= infoEquipo)
        menubar.add_cascade(label="Help", menu=helpmenu)
        win23.config(menu=menubar)
        e1=tk.Label(win23,text="MENU PRINCIPAL",bg="#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12))
        e1.pack(padx=5,pady=5,ipadx=5,ipady=5)

        opc = IntVar()
        R2 = Radiobutton(win23, text='Conductividad cosenoidal', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12), variable = opc, value=2)
        R2.pack( anchor = W )
        R3 = Radiobutton(win23, text='Conductividad aleatoria', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12), variable = opc, value=3)
        R3.pack( anchor = W )

        def validar2():
            if opc.get()==2:
                y=lambda x:np.fabs(np.sin(4*np.pi*x))
                x=np.linspace(0,L,N)
                k=y(x)
                return k
            elif opc.get()==3:
                y=lambda x:np.random(x)
                x=np.linspace(0,L,N)
                k=y(x)
                return k
        botonVerif=tk.Button(win23,text="Validar selección",bg="#E4AB3B",fg="black",command=validar2)
        botonVerif.pack(side=tk.TOP)
        return k

def Lec_Temp(opcTemp, k):
    print('La K de antes es:', k)
    global TA, TB, opc
    if opcTemp == 1:
        global TA, TB, opc
        opc = 1
        win24=tk.Toplevel()#Permite crear una ventana que tendra los atributos de la ventana principal
        win24.title("Condiciones de frontera")
        win24.geometry("350x210+500+200")#Tamaño+posición
        win24.configure(background="#2E2E2E")
        menubar = Menu(win24)
        filemenu = Menu(menubar, tearoff=0)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=infoConduct1)
        helpmenu.add_command(label="About...", command= infoEquipo)
        menubar.add_cascade(label="Help", menu=helpmenu)
        win24.config(menu=menubar)
        e1=tk.Label(win24,text="Condiciones de frontera Dirichlet",bg="#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12))
        e1.grid(row =1, column=5, padx=5, pady=5)
        t1 = Label(win24, text='Temperatura al inicio de la barra:', bg="green",fg="white")
        t1.grid(row=5,sticky="nsew", padx=15, pady=15)
        t2 = Label(win24, text='Temperatura al final de la barra:', bg="green",fg="white")
        t2.grid(row=7,sticky="nsew", padx=15, pady=15)
        temp1 = Entry(win24)
        temp1.insert(0, '100')
        temp1.grid(row=5, column=3,sticky="nsew", padx=15, pady=15)
        temp2 = Entry(win24)
        temp2.insert(0, '500')
        temp2.grid(row=7, column=3,sticky="nsew", padx=15, pady=15)

        def getTemps(opcc):
            global TA, TB, opc
            TA = temp1.get()
            TB = temp2.get()
            opc = opcc
            print(TA, TB, opc)
            return(TA, TB, opc)

        btnContin2=tk.Button(win24,text="Continuar", bg = "#E4AB3B" ,fg = 'black', command= getTemps(opc))
        btnContin2.grid(row=100,sticky="nsew", padx=15, pady=15)
        return(TA, TB, opc)

    elif opcTemp == 2:
        opc = 2
        win24=tk.Toplevel()#Permite crear una ventana que tendra los atributos de la ventana principal
        win24.title("Condiciones de frontera")
        win24.geometry("350x210+500+200")#Tamaño+posición
        win24.configure(background="#2E2E2E")
        menubar = Menu(win24)
        filemenu = Menu(menubar, tearoff=0)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=infoConduct1)
        helpmenu.add_command(label="About...", command= infoEquipo)
        menubar.add_cascade(label="Help", menu=helpmenu)
        win24.config(menu=menubar)
        e1=tk.Label(win24,text="Condiciones de frontera Neumman",bg="#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12))
        e1.pack(padx=5,pady=5,ipadx=5,ipady=5)
        t1 = Label(win24, text='Temperatura al inicio de la barra:',bg="green",fg="white")
        t1.grid(row=5,sticky="nsew", padx=15, pady=15)
        t2 = Label(win24, text='Derivada de la temperatura al final de la barra:',bg="green",fg="white")
        t2.grid(row=5,sticky="nsew", padx=15, pady=15)
        temp1 = Entry(win24)
        temp1.insert(0, '100')
        temp1.grid(row=5, column=20,sticky="nsew", padx=15, pady=15)
        derTemp2 = Entry(win24)
        derTemp2.insert(0, '500')
        derTemp2.grid(row=7, column=20,sticky="nsew", padx=15, pady=15)

        def getTemps():
            TA = t1.get()
            TB = t2.get()
            opc = opc
            return(TA, TB, opc)

        btnContin2=tk.Button(win24,text="Continuar", bg = "#E4AB3B" ,fg = 'black',command= getTemps)
        btnContin2.grid(row=100,sticky="nsew", padx=15, pady=15)

    elif opcTemp == 3:
        win24=tk.Toplevel()#Permite crear una ventana que tendra los atributos de la ventana principal
        win24.title("Condiciones de frontera")
        win24.geometry("350x210+500+200")#Tamaño+posición
        win24.configure(background="#2E2E2E")
        menubar = Menu(win24)
        filemenu = Menu(menubar, tearoff=0)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help", command=infoConduct1)
        helpmenu.add_command(label="About...", command= infoEquipo)
        menubar.add_cascade(label="Help", menu=helpmenu)
        win24.config(menu=menubar)
        e1=tk.Label(win24,text="Condiciones de frontera",bg="#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12))
        e1.pack(padx=5,pady=5,ipadx=5,ipady=5)

        opc = IntVar()
        R1 = Radiobutton(win24, text='Condiciones Dirichlet', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12), variable = opc, value=1)
        R1.pack( anchor = W )
        R2 = Radiobutton(win24, text='Condiciones Neumann', bg = "#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12), variable = opc, value=2)
        R2.pack( anchor = W )

        def validar2():
            if opc.get()==1:
                opc = 1
                win24=tk.Toplevel()#Permite crear una ventana que tendra los atributos de la ventana principal
                win24.title("Condiciones de frontera")
                win24.geometry("350x210+500+200")#Tamaño+posición
                win24.configure(background="#2E2E2E")
                menubar = Menu(win24)
                filemenu = Menu(menubar, tearoff=0)
                helpmenu = Menu(menubar, tearoff=0)
                helpmenu.add_command(label="Help", command=infoConduct1)
                helpmenu.add_command(label="About...", command= infoEquipo)
                menubar.add_cascade(label="Help", menu=helpmenu)
                win24.config(menu=menubar)
                e1=tk.Label(win24,text="Condiciones de frontera Dirichlet",bg="#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12))
                e1.grid(row =1, column=5, padx=5, pady=5)
                t1 = Label(win24, text='Temperatura al inicio de la barra:', bg="green",fg="white")
                t1.grid(row=5,sticky="nsew", padx=15, pady=15)
                t2 = Label(win24, text='Temperatura al final de la barra:', bg="green",fg="white")
                t2.grid(row=7,sticky="nsew", padx=15, pady=15)
                temp1 = Entry(win24)
                temp1.insert(0, '100')
                temp1.grid(row=5, column=20,sticky="nsew", padx=15, pady=15)
                temp2 = Entry(win24)
                temp2.insert(0, '500')
                temp2.grid(row=7, column=20,sticky="nsew", padx=15, pady=15)

                def getTemps():
                    TA = t1.get()
                    TB = t2.get()
                    opc = opc
                    return(TA, TB, opc)

                btnContin2=tk.Button(win24,text="Continuar", bg = "#E4AB3B" ,fg = 'black',command= getTemps)
                btnContin2.grid(row=100,sticky="nsew", padx=15, pady=15)
            
            elif opc.get()==2:
                opc = 2
                win24=tk.Toplevel()#Permite crear una ventana que tendra los atributos de la ventana principal
                win24.title("Condiciones de frontera")
                win24.geometry("350x210+500+200")#Tamaño+posición
                win24.configure(background="#2E2E2E")
                menubar = Menu(win24)
                filemenu = Menu(menubar, tearoff=0)
                helpmenu = Menu(menubar, tearoff=0)
                helpmenu.add_command(label="Help", command=infoConduct1)
                helpmenu.add_command(label="About...", command= infoEquipo)
                menubar.add_cascade(label="Help", menu=helpmenu)
                win24.config(menu=menubar)
                e1=tk.Label(win24,text="Condiciones de frontera Neumman",bg="#2E2E2E",fg="#E4AB3B",font = ('Helvetica', 12))
                e1.pack(padx=5,pady=5,ipadx=5,ipady=5)
                t1 = Label(win24, text='Temperatura al inicio de la barra:',bg="green",fg="white")
                t1.grid(row=5,sticky="nsew", padx=15, pady=15)
                t2 = Label(win24, text='Derivada de la temperatura al final de la barra:',bg="green",fg="white")
                t2.grid(row=5,sticky="nsew", padx=15, pady=15)
                temp1 = Entry(win24)
                temp1.insert(0, '100')
                temp1.grid(row=5, column=20,sticky="nsew", padx=15, pady=15)
                derTemp2 = Entry(win24)
                derTemp2.insert(0, '500')
                derTemp2.grid(row=7, column=20,sticky="nsew", padx=15, pady=15)

                def getTemps():
                    TA = t1.get()
                    TB = t2.get()
                    opc = opc
                    return(TA, TB, opc)

                btnContin2=tk.Button(win24,text="Continuar", bg = "#E4AB3B" ,fg = 'black',command= getTemps)
                btnContin2.grid(row=100,sticky="nsew", padx=15, pady=15)
            botonVerif=tk.Button(win24,text="Validar selección", bg="#E4AB3B",fg="black",command=validar2)
            botonVerif.pack(side=tk.TOP)



def Fuentes(opc,N,L):
    h=L/(N-1)
    if opc==1:
        Q=Crea_Matriz(N-2,1)
        Q=Tipo_Fuente(Q, h)
        tipo=1
    else: 
        Q=Crea_Matriz(N-1,1)
        tn=3
        while ((tn!=1) and (tn!=2)):
            print('Tipo de Newmman:')
            tn=int(input('\t1) Newmman I\n\t2) Newmman IV\n\t'))
            if tn==1:
                Q=Tipo_Fuente(Q,h)
                Q[N-2]=0
                tipo=2
            elif tn==2:
                Q=Tipo_Fuente(Q,h)
                tipo=3
            else:
                 print('Opcion no valida')
    return (Q,h,tipo)

def Tipo_Fuente(Q,h):
    m=Q.shape[0]
    tf=4
    while ((tf!=1) and (tf!=2) and (tf!=3)):
        print('\nTipo de fuente:')
        tf=int(input('\t1) Puntual\n\t2) Exponencial\n\t3) Sin fuentes\n\t'))
        if tf==1:
            nQ=int(input('Número de fuentes de calor: '))
            if nQ==0:
                print('No hay fuentes de calor')
            else:
                print('Valores de las fuentes (agregar signo menos si es sumidero)')
                for i in range(nQ):
                    x=int(input('Nodo donde se encuentra: '))
                    Q[x-2]=float(input('Valor: '))
        elif tf==2:
            for i in range(m):
                Q[i]=np.exp(h*i)
        elif tf==3:
            Q=Q
        else:
            print('Opcion no valida')
    return (Q)

#2) CREACIÓN DE MATRIZ
def Crea_Matriz(n,m):
    """
    Función que crea una matriz con las dimensiones dadas
    """
    return np.zeros((n,m))

#3) LLENADO DE LAS MATRICES
def Matriz_ll_2(L,TA,TB,N,k,h,tipo):
    """
    Función que crea las matrices y las llena
    Utiliza la función Crea_Matriz para crear cada matriz 
    """
    #Matriz de Temperaturas en todo el dominio
    Temp=Crea_Matriz(N,1)
    Temp[0]=TA
    
    if tipo==1:     #Dirichlet
        #Matriz de coeficientes
        A=Crea_Matriz(N-2,N-2)
        for i in range(N-2):
            for j in range(N-2):
                if (i==j):
                    A[i][j]=-2
                if(np.fabs(i-j)==1):
                    A[i][j]=1
        #Matriz de temperaturas frontera
        Tf=Crea_Matriz(N-2,1)
        Tf[0]=-TA
        Tf[N-3]=-TB
        #temperatura al final de la barra
        Temp[N-1]=TB
    elif tipo==2:       #Newmman I
        #Matriz de coeficientes
        A=Crea_Matriz(N-1,N-1)
        for i in range(N-1):
            for j in range(N-1):
                if (i==j):
                    A[i][j]=-2
                if(np.fabs(i-j)==1):
                    A[i][j]=1
        A[N-2][N-3]=-1
        A[N-2][N-2]=1
        #Matriz de temperaturas frontera
        Tf=Crea_Matriz(N-1,1)
        Tf[0]=-TA
        Tf[N-2]=h*TB
    else:       #Newmman IV
        #Matriz de coeficientes
        A=Crea_Matriz(N-1,N-1)
        for i in range(N-1):
            for j in range(N-1):
                if (i==j):
                    A[i][j]=-2
                if(np.fabs(i-j)==1):
                    A[i][j]=1
        A[N-2][N-2]=-1
        #Matriz de temperaturas frontera
        Tf=Crea_Matriz(N-1,1)
        Tf[0]=-TA
        Tf[N-2]=-h*TB
    
    return (A,Tf,Temp)

#4) IMPRIMIR MATRICES
def Imprime_Matriz(a):
    """
    Función de apoyo para imprimir en pantalla la matriz dada
    """
    [n,m]=a.shape
    print('\n')
    for i in range (n):
        for j in range (m):
            print(a[i][j],end=' ')
        print('\n')

#5) SOLUCIÓN APROXIMADA
def Sol_Aprox11(A,Tf,Temp,Q,r,N,cond):
    """
    Función que resuelve el sistema de matrices [A][x]=[b] y debuelve la solución
    """
    
    #Definicion de la matriz b
    b=Tf+(1/r)*-Q
    
    #Resolviendo el sistema
    if cond==1:
        Temp[1:N-1] = np.linalg.solve(A,b)
    else:
        Temp[1:N] = np.linalg.solve(A,b)
    
    return Temp

#6) GRÁFICAS
def Graf11(ng,x,y,nombre,Nx,Ny,linea,title):
    """
    Función para realización de gráficas de resultados
    """
    for i in range (0,ng):
        plt.plot(x[i],y[i],linea[i],label=nombre[i])
    plt.title(title)
    plt.xlabel(Nx)
    plt.ylabel(Ny)
    plt.legend()
    plt.show()

###########################################CALIBRACIÓN Lineal:#######################################################
def caliLineal(L,N,opcCond, opcTemp):
    [L, k, N,TA,TB,Q,h,r,tipo,Dist,opc]=LecDatosCal(L,N,opcCond, opcTemp)

    [A,Tf,Temp]=Matriz_ll_2(L,TA,TB,N,k,h,tipo)
        
    y=lambda x: TA+x*(TB-TA)/L
    x=np.linspace(0,L,30)

    Temp=Sol_Aprox(A,Tf,Temp,Q,r,N,opc)

    datx=[x,Dist]
    daty=[y(x), Temp]
    Nombre=['Solución analítica','Solución aproximada']
    nx='Distancia'
    ny='Temperatura'
    linea=['C1--','-bo']

    Graf(2,datx,daty,Nombre,nx,ny,linea,'Temperatura de la barra')

    print('Imprimir matrices')
    im=int(input('\t1) SI\n\t2) NO\n\t'))
    if im==1:
        print('\n\tMatriz de Coeficientes')
        Imprime_Matriz(A)
        
        print('\n\tMatriz de Temperaturas a lo largo de la barra')
        Imprime_Matriz(Temp)
        
        print('\n\tMatriz de Temperaturas en fronteras')
        Imprime_Matriz(Tf)
            
        print('\n\tMatriz de Fuentes')
        mImprime_Matriz(Q)
    else:
        print('BUEN DÌA =)')


##################################################CALIBRACION 2:#########################################################

def calibracion2(L,N):
    [L,k,N]=LecDatos(L,N)
    [TA,TB]=Temp_New()

    y=lambda x: np.exp(x)-x-np.e+4
    x=np.linspace(0,L,30)

    datx=[x]
    x=np.linspace(L,0,30)
    daty=[y(x)]
    Nombre=['Solución analítica']
    nx='Distancia'
    ny='Temperatura'
    linea=['C1--']

    [h,r,A,Tf,Temp,Dist]=mf.Matriz_NewI(L,TA,TB,k,N)
    Q=Crea_Matriz(N-1,1)
    for i in range(N-2):
        Q[i]=np.exp(h*i)
    print('\n\tMatrices para Nwemman I\n')
    print('\n\tMatriz de Coeficientes')
    Imprime_Matriz(A)

    print('\n\tMatriz de Temperaturas a lo largo de la barra')
    Imprime_Matriz(Temp)

    print('\n\tMatriz de Temperaturas en fronteras')
    Imprime_Matriz(Tf)
        
    print('\n\tMatriz de Fuentes')
    Imprime_Matriz(Q)

    Temp=Sol_Aprox(A,Tf,Temp,Q,r,N,2)

    datx.append(Dist)
    daty.append(Temp)
    Nombre.append('Solución Newmman I')
    linea.append('-bo')

    [A,Tf,Temp]=Matriz_NewIV(L,TA,TB,k,N,h)
    Q[N-2]=np.exp(L)/2
    print('\n\tMatrices para Newmman IV\n')
    print('\n\tMatriz de Coeficientes')
    Imprime_Matriz(A)

    print('\n\tMatriz de Temperaturas a lo largo de la barra')
    Imprime_Matriz(Temp)

    print('\n\tMatriz de Temperaturas en fronteras')
    Imprime_Matriz(Tf)
        
    print('\n\tMatriz de Fuentes')
    Imprime_Matriz(Q)

    Temp=Sol_Aprox(A,Tf,Temp,Q,r,N,2)

    datx.append(Dist)
    daty.append(Temp)
    Nombre.append('Solución Newmman IV')
    linea.append('-ro')

    Graf(3,datx,daty,Nombre,nx,ny,linea,'Temperatura de la barra')






####################################################### INFORMACIÓN PARA MENUS #############################################################

#Ventana emergente de informacion sobre el equipo
def infoEquipo():
    messagebox.showinfo('Información - Equipo 4 - GEOMAC 2021-1', '''Este programa fue diseñado y creado por:

    López Garrido Josué
    Martínez Pérez José Antonio
    Rodriguez Mendoza Alban Alexis
    
    Estudiantes de Ingeniería Geofísica
    en la Facultad de Ingeniería
    de la UNAM, para la materia de:

    Geofísica Matemática y computacional

    Impartida por el Dr. Luis Miguel de la Cruz Salas''')

#Ventana emergente de información sobre el programa
def infoPrograma():
    messagebox.showinfo('Funcionamiento del programa', '''El archivo de muestra (sample) contiene todos los datos de entrada en el siguiente orden [L,TA,TB,k,N,nQ] 
        El archivo Fuentes/Sumideros debe contener el valor inicial en cada nodo, cada nodo debe estar separado por una coma''')

#Ventana emergente de ayuda para las condiciones tipo 1-1
def infoCondicionTipo1():
    messagebox.showinfo('Funcionamiento del programa', '''
    En las casillas de esta ventana deberás ingresar:  

1. La longitud de la barra en metros [m]\n
2. La temperatura de la frontera A (Frontera 1) en grados Celsius [°C]\n
3. La temperatura de la frontera B (Frontera 2) en grados Celcius [°C]\n
4. La conductividad térmica del material de la barra\n
5. El número total de nodos dentro de la barra incluyendo los de los extremos A y B\n
6. El número de fuentes y/o sumideros en los nodos centrales de la barra (sin contar las fuentes de los extremos A y B) en caso de no haberlos, déjese como 0  ''')


def infoCondicionTipo12():
    messagebox.showinfo('Funcionamiento del programa', '''
    En la casilla de esta ventana::

Se deben modificar los ceros por el valor de la temperatura en los nodos centrales de la barra, en la posición que quieras, sin borrar los otros ceros, pej:

Si se eligieron 6 nodos y 2 fuentes, se deberá ingresar algo como esto:

0, 2000, 0, 3000

Ya que no se consideran los nodos A y B
        ''')

def infoConduct1():
    messagebox.showinfo('Funcionamiento del programa', '''
    Elejir alguna de las dos opciones y
    luego, presionar el botón 'Continuar'
        ''')