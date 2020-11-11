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
    k=float(input('Conductividad térmica: '))
    N=int(input('Número de nodos (incluir los nodos extremos): '))
    
    return(L, k, N)

def Temp_Dir():
    TA=float(input('Temperatura al inicio de la barra: '))
    TB=float(input('Temperatura al final de la barra: '))
    return (TA,TB)

def Temp_New():
    TA=float(input('Temperatura al inicio de la barra: '))
    TB=float(input('Derivada de la temperatura al final de la barra: '))
    return (TA,TB)
            
#2) CREACIÓN DE MATRIZ
def Crea_Matriz(n,m):
    """
    Función que crea una matriz con las dimensiones dadas
    """
    return np.zeros((n,m))

# 3) LLENADO DE LAS MATRICES
# 3.1)Tipo Dirichlet
def Matriz_dir(L,TA,TB,k,N):
    """
    Función que crea las matrices para condiciones Dirichlet
    Utiliza la función Crea_Matriz para crear cada matriz 
    Además calcula algunos valores extra a usar en otro momento
    """
    
    #Tamaño de las divisiones
    h=L/(N-1)
    
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

# 3.2)Tipo Newmman I
def Matriz_NewI(L,TA,TB,k,N):
    """
    Función que crea las matrices para condiciones Dirichlet
    Utiliza la función Crea_Matriz para crear cada matriz 
    Además calcula algunos valores extra a usar en otro momento
    """
    
    #Tamaño de las divisiones
    h=L/(N-1)
    
    #Cálculo de r
    r=k/(h**2)
    
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
    
    #Matriz de Temperaturas en todo el dominio
    Temp=Crea_Matriz(N,1)
    Temp[0]=TA
    
    #Matriz de distancias
    Dist=Crea_Matriz(N,1)
    Dist[0]=0
    for i in range (1,N):
        Dist[i]=Dist[i-1]+h
    
    return (h,r,A,Tf,Temp,Dist)

# 3.3)Tipo Newmman IV
def Matriz_NewIV(L,TA,TB,k,N,h):
    """
    Función que crea las matrices para condiciones Dirichlet
    Utiliza la función Crea_Matriz para crear cada matriz 
    Además calcula algunos valores extra a usar en otro momento
    """
    
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
    
    #Matriz de Temperaturas en todo el dominio
    Temp=Crea_Matriz(N,1)
    Temp[0]=TA
    
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

#6) SOLUCIÓN APROXIMADA
def Sol_Aprox(A,Tf,Temp,Q,r,N,cond):
    """
    Función que resuelve el sistema de matrices [A][x]=[b] y debuelve la solución
    """
    
    #Definicion de la matriz b
    b=Tf+(1/r)*Q
    
    #Resolviendo el sistema
    if cond==1:
        Temp[1:N-1] = np.linalg.solve(A,b)
    else:
        Temp[1:N] = np.linalg.solve(A,b)
    
    return Temp

#7) GRÁFICAS
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