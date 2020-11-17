#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:47:55 2020

@author: josuelg
"""
import ModFun as mf
#Programa principal
[L, k, N,TA,TB,Q,h,tipof,Dist,opc,tk]=mf.LecDatos()

[A,Tf,Temp]=mf.Matriz_ll(TA,TB,N,k,h,tipof,tk)
    
Temp=mf.Sol_Aprox(A,Tf,Temp,Q,N,opc,tk,k,h)
datx=[Dist]
daty=[Temp]
Nombre=['Solución numérica']
nx='Distancia'
ny='Temperatura'
linea=['-bo']

mf.Graf(1,datx,daty,Nombre,nx,ny,linea,'Temperatura de la barra')

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
