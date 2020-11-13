#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:24:52 2020

@author: josuelg
"""
#importar bibliotecas útiles en el programa
import numpy as np
import matplotlib.pyplot as plt

#1) LECTURA DE DATOS
def LecDatos():
    """
    Función que ayuda en la lectura de datos iniciales del problema
    La función regresa los valores para su uso posterior
    """
    print('DATOS DE ENTRADA')
    L=float(input('Longitud de la barra: '))
    N=int(input('Número de nodos (incluir los nodos extremos): '))
    k=Conductividad(L,N)
    [TA,TB,opc]=Lec_Temp()
    [Q,h,tipo]=Fuentes(opc,N,L)
    #Cálculo de r
    r=k/(h**2)
    #Matriz de distancias
    Dist=Crea_Matriz(N,1)
    for i in range (1,N):
        Dist[i]=Dist[i-1]+h
    return(L, k, N,TA,TB,Q,h,r,tipo,Dist,opc)

def Conductividad(L,N):
    opc=4
    while ((opc!=1) and (opc!=2) and (opc!=3)):
        print('\nComportamiento de la conductividad termica:')
        opc=int(input('\t1) constante\n\t2) cosenoidal\n\t3) aleatoria\n\t'))
        if opc==1:
            k=float(input('Conductividad térmica: '))
        elif opc==2:
            y=lambda x:np.fabs(np.sin(4*np.pi*x))
            x=np.linspace(0,L,N)
            k=y(x)
        elif opc==3:
            y=lambda x:np.random(x)
            x=np.linspace(0,L,N)
            k=y(x)
        else:
            print('Opcion no valida')
    return k

def Lec_Temp():
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

#2) CREACIÓN DE MATRIZ
def Crea_Matriz(n,m):
    """
    Función que crea una matriz con las dimensiones dadas
    """
    return np.zeros((n,m))

#3) LLENADO DE LAS MATRICES
def Matriz_ll(L,TA,TB,N,k,h,tipo):
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
def Sol_Aprox(A,Tf,Temp,Q,r,N,cond):
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
def Graf(ng,x,y,nombre,Nx,Ny,linea,title):
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