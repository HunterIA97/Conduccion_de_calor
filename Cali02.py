#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:21:56 2020

@author: josuelg
"""

import ModFun as mf
import numpy as np
import matplotlib.pyplot as plt

#Programa principal
[L,k,N]=mf.LecDatos()
[TA,TB]=mf.Temp_New()

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
Q=mf.Crea_Matriz(N-1,1)
for i in range(N-2):
    Q[i]=np.exp(h*i)
print('\n\tMatrices para Nwemman I\n')
print('\n\tMatriz de Coeficientes')
mf.Imprime_Matriz(A)

print('\n\tMatriz de Temperaturas a lo largo de la barra')
mf.Imprime_Matriz(Temp)

print('\n\tMatriz de Temperaturas en fronteras')
mf.Imprime_Matriz(Tf)
    
print('\n\tMatriz de Fuentes')
mf.Imprime_Matriz(Q)

Temp=mf.Sol_Aprox(A,Tf,Temp,Q,r,N,2)

datx.append(Dist)
daty.append(Temp)
Nombre.append('Solución Newmman I')
linea.append('-bo')

[A,Tf,Temp]=mf.Matriz_NewIV(L,TA,TB,k,N,h)
Q[N-2]=np.exp(L)/2
print('\n\tMatrices para Nwemman IV\n')
print('\n\tMatriz de Coeficientes')
mf.Imprime_Matriz(A)

print('\n\tMatriz de Temperaturas a lo largo de la barra')
mf.Imprime_Matriz(Temp)

print('\n\tMatriz de Temperaturas en fronteras')
mf.Imprime_Matriz(Tf)
    
print('\n\tMatriz de Fuentes')
mf.Imprime_Matriz(Q)

Temp=mf.Sol_Aprox(A,Tf,Temp,Q,r,N,2)

datx.append(Dist)
daty.append(Temp)
Nombre.append('Solución Newmman IV')
linea.append('-ro')

mf.Graf(3,datx,daty,Nombre,nx,ny,linea,'Temperatura de la barra')