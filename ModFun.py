"""
ModFun
=====
Created on Tue Nov 10 17:24:52 2020

Este módulo de funciones esta definido para el apoyo en la solución de
problemas de conducción de calor en estado estacionario
Con condiciones de frontera tipo Dirichlet o Newmman
Para casos donde la conductividad térmica es constante o variable
Con o sin fuentes en el dominio

Funciónes que contiene 
----------------------------------------------
LecDatos
    Lectura de datos iniciales del problema a travez del teclado

Conductividad
    Lectura de la conductividad térmica
    
Lec_Temp
    Lectura de temperaturas iniciales
    
Fuentes
    Lectura de fuentes

Tipo_Fuente
    Diferentes comportamientos de fuentes

Crea_Matriz
    Creación e inicialización de matrices
    
Matriz_ll
    Llenado de matrices 

CondMedia
    Cálculo de conductividad en puntos medios

Imprime_Matriz
    Imprimir matrices en terminal

Sol_Aprox
    Cálculo de la solución numérica

Graf
    Gráficas de resultados

"""
#importar bibliotecas útiles en el programa
import numpy as np
import random as rm
import matplotlib.pyplot as plt

#1) LECTURA DE DATOS
def LecDatos():
    """
    Función que ayuda en la lectura de datos iniciales del problema
    La función regresa los valores para su uso posterior
    
    Parameters
    -------------
        Ningun parámetro de entrada
    
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
        O valor de la derivada al final de la barra
    Q:float array
        Arreglo de los valores de las fuentes en el dominio
    h:float
        Distancia entre nodos
    tipof:integer
        Tipo de método de solución que se va a usar, estas pueden ser:
            1=Dirichlet
            2=Newmman I
            3=Newmman IV
    Dist:float array
        Arreglo de valores del eje x para gráficas
    opc:integer
        Tipo de condiciones de frontera, estas pueden ser 
            1=Dirichlet
            2=Newmman
    tk:integer
        Comportamineto de la conductividad térmica, estas pueden ser:
            1=Constante
            2=Cosenoidal
            3=Aleatoria
    """
    print('DATOS DE ENTRADA')
    L=float(input('Longitud de la barra: '))
    N=int(input('Número de nodos (incluir los nodos extremos): '))
    [k,tk]=Conductividad(L,N)
    [TA,TB,opc]=Lec_Temp()
    [Q,h,tipof]=Fuentes(opc,N,L)
    
    #Matriz de distancias
    Dist=Crea_Matriz(N,1)
    for i in range (1,N):
        Dist[i]=Dist[i-1]+h
        
    return(L, k, N,TA,TB,Q,h,tipof,Dist,opc,tk)

#2) LECTURA DE CONDUCTIVIDAD
def Conductividad(L,N):
    """
    Función que lee los valores de conductividad térmica
    o los calcula, segun sea su comportamiento.

    Parameters
    ----------
    L : float
        Longitud del dominio
    N : integer
        Número de nodos del dominio

    Returns
    -------
    k : float or float array
        Valor de la conductividad (constante) 
        o arreglo de valores de conductividad (variable)
    tk : integer
        Comportamiento de la conductividad
            1=Constante
            2=Cosenoidal
            3=Aleatoria
    """
    tk=4
    while ((tk!=1) and (tk!=2) and (tk!=3)):
        print('\nComportamiento de la conductividad termica:')
        tk=int(input('\t1) constante\n\t2) cosenoidal\n\t3) aleatoria\n\t'))
        if tk==1:
            k=float(input('Conductividad térmica: '))
        elif tk==2:
            x=np.linspace(0,L,N)
            k=Crea_Matriz(N,1)
            for i in range (N):
                k[i]=np.fabs(np.sin(4*np.pi*x[i]))
        elif tk==3:
            k=Crea_Matriz(N,1)
            for i in range (N):
                k[i]=rm.random()
        else:
            print('Opcion no valida')
    return (k,tk)

#3) LECTURA DE TEMPERATURAS
def Lec_Temp():
    """
    Función que ayuda a la lectura de las temperaturas
    segun las condiciones de frontera que se tengan
    
    Parameters
    ----------
    Ningún parámetro de entrada
    
    Returns
    -------
    TA : float
        Temperatura al inicio del dominio
    TB : float
        Temperatura al final del dominio o valor de la derivada
        segun las condiciones de frontera usadas
    opc : integer
        Tipo de condiciones de frontera a usar
    """
    opc=4
    while ((opc!=1) and (opc!=2)):
        print('\nCondiciones de frontera:')
        opc=int(input('\t1) Dirichlet\n\t2) Newman\n\t'))
        if opc==1:
            TA=float(input('Temperatura al inicio de la barra: '))
            TB=float(input('Temperatura al final de la barra: '))
        elif opc==2:
            TA=float(input('Temperatura al inicio de la barra: '))
            TB=float(input('Derivada de la temperatura al final de la barra: '))
        else:
            print('Opcion no valida')
    return(TA,TB,opc)

#4) LECTURA DE FUENTES
def Fuentes(opc,N,L):
    """
    Función que lee los datos de fuentes en el dominio 
    o genera los valores segun sea el tipo de fuente a usar

    Parameters
    ----------
    opc : integer
        Tipo de condiciones de frontera
    N : integer
        Número de nodos del dominio
    L : float
        Longitud del dominio

    Returns
    -------
    Q : float array
        Valores de las fuentes 
    h : float
        distancia entre nodos
    tipo : integer
        Modelo para calcular la solución del sistema

    """
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
                Q[N-2]=Q[N-2]/2
                tipo=3
            else:
                 print('Opcion no valida')
    return (Q,h,tipo)

#5) LLENADO DE FUENTES
def Tipo_Fuente(Q,h):
    """
    Función que coloca los valores de fuentes en el arreglo Q
    según el modelo con el que se va a realizar el calculo de la solución

    Parameters
    ----------
    Q : float array
        Arreglo donde se vaciarán los valores de fuentes
    h : float
        Distancia entre nodos

    Returns
    -------
    Q : float array
        Arreglo con los valores de fuentes en el dominio

    """
    m=Q.shape[0]
    tf=4
    while ((tf!=1) and (tf!=2)and (tf!=3)):
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

#6) CREACIÓN DE MATRIZ
def Crea_Matriz(n,m):
    """
    Función que crea una matriz de dimensiones definidas 
    inicializada en cero

    Parameters
    ----------
    n : integer
        Número de filas
    m : integer
        Número de columnas

    Returns
    -------
    array
        Matriz inicializada en cero de tamaño nxm

    """
    return (np.zeros((n,m)))

#7) LLENADO DE LAS MATRICES
def Matriz_ll(TA,TB,N,k,h,tipof,tk):
    """
    Función que llena las matrices a usar enla aproximación

    Parameters
    ----------
    TA : float
        Temperatura al inicio del dominio
    TB : float
        Temperatura (o valor de la derivada) al final del dominio
    N : integer
        Número de nodos del dominio
    k : float or float array
        Valor(es) de la conductividad térmica
    h : float
        Distancia entre nodos
    tipof : integer
        Tipo de método de solución que se va a usar
    tk : integer
        Comportamiento de la conductividad térmica

    Returns
    -------
    A : float array
        Matriz de coeficientes del sistema
    Tf : float array
        Matriz de temperaturas en las fronteras
    Temp : froat array
        Matriz de temperaturas en todo el dominio

    """
    #Matriz de Temperaturas en todo el dominio
    Temp=Crea_Matriz(N,1)
    Temp[0]=TA
    
    if (tipof==1 and tk==1):     #Dirichlet, k constante
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
    elif (tipof==2 and tk==1):       #Newmman I, k constante
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
    elif(tipof==3 and tk==1):       #Newmman IV, k constante
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
    else:                           #k no constante
        #Matriz de coeficientes
        A=Crea_Matriz(N-2,N-2)
        for i in range (N-2):
            for j in range(N-2):
                if (i==j):
                    A[i][j]=-(CondMedia(k[i+2],k[i+1])+CondMedia(k[i+1],k[i]))
                if(i-j==1):
                    A[i][j]=CondMedia(k[i+1],k[i])
                if(i-j==-1):
                    A[i][j]=CondMedia(k[i+2],k[i+1])
        #Matriz de temperaturas en frontera
        Tf=Crea_Matriz(N-2,1)
        Tf[0]=-TA*CondMedia(k[0],k[1])
        Tf[N-3]=-TB*CondMedia(k[N-2],k[N-1])
        
        #temperatura al final de la barra
        Temp[N-1]=TB
    
    return (A,Tf,Temp)

#8) cONDUCTIVIDAD EN PUNTOS MEDIOS
def CondMedia(k1,k2):
    """
    Fucnión que cacula la conductividad en puntos medios entre nodos
    usando promedio aritmético

    Parameters
    ----------
    k1 : float
        Valor de la conductividad en el punto i
    k2 : float
        Valor de la conductividad en el punto i+1 o i-1

    Returns
    -------
    km : float
        Valor de la conductividad en el punto medio

    """
    km=(k1+k2)/2
    return km

#9) IMPRIMIR MATRICES
def Imprime_Matriz(a):
    """
    Función de apoyo para impresión de matrices

    Parameters
    ----------
    a : array
        Matriz que se va a imprimir

    Returns
    -------
    None.

    """
    [n,m]=a.shape
    print('\n')
    for i in range (n):
        for j in range (m):
            print(a[i][j],end=' ')
        print('\n')

#10) SOLUCIÓN APROXIMADA
def Sol_Aprox(A,Tf,Temp,Q,N,cond,tk,k,h):
    """
    Función que calcula la solución del sistema

    Parameters
    ----------
    A : array
        Matriz de coeficientes del sistema
    Tf : array
        Matriz de valores de temperaturas en fronteras
    Temp : array
        Matriz de valores de temperaturas en todo el dominio
    Q : array
        Matriz de valores de fuentes
    N : integer
        Número de nodos en el dominio
    cond : integer
        Tipo de condiciones de frontera usadas
    tk : integer
        Tipo de comportamiento de la consuctividad
    k : float 
        Valor de la conductividad térmica en todo el dominio.
        Usado solo si la consuctividad es constante
    h : float
        Distancia entre nodos

    Returns
    -------
    Temp : array
        Matriz con los valores de temperatura calculados como 
        solución del sistema

    """
    if (cond==1 and tk==1):
        r=k/(h**2)
        #Definicion de la matriz b
        b=Tf+(1/r)*-Q
        #Resolviendo el sistema
        Temp[1:N-1] = np.linalg.solve(A,b)
    elif(cond==2 and tk==1):
        r=k/(h**2)
        #Definicion de la matriz b
        b=Tf+(1/r)*Q
        #Resolviendo el sistema
        Temp[1:N] = np.linalg.solve(A,b)
    else:
        #Definicion de la matriz b
        b=Tf+(h**2)*-Q
        #Resolviendo el sistema
        Temp[1:N-1] = np.linalg.solve(A,b)
    return Temp

#11) GRÁFICAS
def Graf(ng,x,y,nombre,Nx,Ny,linea,title):
    """
    Funció de apoyo para realización de gráficas
    Crea cierta cantidad de gráficas en una misma figura

    Parameters
    ----------
    ng : integer
        Número de gráficas que se van a realizar
    x : array
        arreglo de arreglos. Cada arreglo incluido son las posiciones
        a graficar en el eje x
    y : array
        arreglo de arreglos. Cada arreglo incluido son las posiciones
        a graficar en el eje y
    nombre : string array
        arreglo con los nombres de cada línea en la gráfica
    Nx : string
        Nombre del eje x
    Ny : string
        Nombre del eje y
    linea : array
        Tipo de línea con el que se verá cada linea en la gráfica,
        así como el color
    title : string
        Título de la figura

    Returns
    -------
    None.

    """
    for i in range (0,ng):
        plt.plot(x[i],y[i],linea[i],label=nombre[i])
    plt.title(title)
    plt.xlabel(Nx)
    plt.ylabel(Ny)
    plt.legend()
    plt.show()