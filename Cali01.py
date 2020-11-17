#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:31:37 2020

@author: josuelg
"""
import ModFun as mf
import numpy as np
#Programa principal
[L, k, N,TA,TB,Q,h,tipo,Dist,opc,tk]=mf.LecDatos()
[A,Tf,Temp]=mf.Matriz_ll(TA,TB,N,k,h,tipo,tk)

f=np.pi/4
y=lambda x:((1-np.cos(f))/np.sin(f))*np.sin(x*f)+np.cos(f*x)
x=np.linspace(0,L,30)

for i in range (N-2):
    A[i][i]=(h**2)*(f**2)-2
    
Temp=mf.Sol_Aprox(A,Tf,Temp,Q,N,opc,tk,k,h)

datx=[x,Dist]
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
