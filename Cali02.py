#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 18:21:56 2020

@author: josuelg
"""

import ModFun as mf
import numpy as np

#Programa principal
[L, k, N,TA,TB,Q,h,tipof,Dist,opc,tk]=mf.LecDatos()

[A,Tf,Temp]=mf.Matriz_ll(TA,TB,N,k,h,tipof,tk)

y=lambda x: np.exp(x)-x-np.e+4
x=np.linspace(0,L,30)

Temp=mf.Sol_Aprox(A,Tf,Temp,Q,N,opc,tk,k,h)

datx=[x,Dist]
x=np.linspace(L,0,30)
daty=[y(x), Temp]
Nombre=['Solución analítica','Solución aproximada']
nx='Distancia'
ny='Temperatura'
linea=['C1--','-bo']

mf.Graf(2,datx,daty,Nombre,nx,ny,linea,'Temperatura de la barra')

print('Imprimir matrices')
im=int(input('\t1) SI\n\t2) NO\n\t'))
if im==1:
    print('\n\tMatriz de Coeficientes')
    mf.Imprime_Matriz(A)
    
    print('\n\tMatriz de Temperaturas a lo largo de la barra')
    mf.Imprime_Matriz(Temp)
    
    print('\n\tMatriz de Temperaturas en fronteras')
    mf.Imprime_Matriz(Tf)
        
    print('\n\tMatriz de Fuentes')
    mf.Imprime_Matriz(Q)
else:
    print('BUEN DÌA =)')
