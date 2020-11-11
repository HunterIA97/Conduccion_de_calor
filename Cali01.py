#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:40:44 2020

@author: josuelg
"""

import ModFun as mf
import numpy as np
#Programa principal
[L,k,N]=mf.LecDatos()
[TA,TB]=mf.Temp_Dir()
Q=mf.Crea_Matriz(N-2,1)
nQ=int(input('Número de fuentes de calor: '))
if nQ==0:
    print('No hay fuentes de calor')
else:
    for i in range(nQ):
        x=int(input('Nodo donde se encuentra: '))
        f=int(input('\tTipo\n1) Fuente\n2) Sumidero\n'))
        if f==1:
            Q[x-2]=1
        else:
            Q[x-2]=-1
    
[h,r,A,Tf,Temp,Dist]=mf.Matriz_dir(L,TA,TB,k,N)
print('\n\tMatriz de Coeficientes')
mf.Imprime_Matriz(A)

print('\n\tMatriz de Temperaturas a lo largo de la barra')
mf.Imprime_Matriz(Temp)

print('\n\tMatriz de Temperaturas en fronteras')
mf.Imprime_Matriz(Tf)
    
print('\n\tMatriz de Fuentes')
mf.Imprime_Matriz(Q)
    
y=lambda x: TA+x*(TB-TA)/L
x=np.linspace(0,L,30)

Temp=mf.Sol_Aprox(A,Tf,Temp,Q,r,N,1)

datx=[x,Dist]
daty=[y(x), Temp]
Nombre=['Solución analítica','Solución aproximada']
nx='Distancia'
ny='Temperatura'
linea=['C1--','--bo']

mf.Graf(2,datx,daty,Nombre,nx,ny,linea,'Temperatura de la barra')
