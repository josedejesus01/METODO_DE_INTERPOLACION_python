# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:06:33 2021

@author: JOSE
"""
def formula(x,fx):
    b0=fx[0]
    b1=(fx[1]-fx[0])/(x[1]-x[0])
    b2=(((fx[2]-fx[1])/(x[2]-x[1]))-((fx[1]-fx[0])/(x[1]-x[0])))/(x[2]-x[0])
    f2=b0+b1*(x[3]-x[0])+b2*(x[3]-x[0])*(x[3]-x[1])
    return(f2)
x=[]
fx=[]
for i in range(0,3):
    vx=float(input("introduce el valor para x("+str(i+1)+"]\n"))
    x.append(vx)
    vfx=float(input("introduce el valor para fx["+str(i+1)+"]\n"))
    fx.append(vfx)  
vx=float(input("introduce el valor de x para calcular f(x)\n"))
x.append(vx)
print ("el valor de fx es  ",formula(x,fx))
