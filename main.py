#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from radio.basics import *

#---- Inicio descripción del circuito

circuito = Circuit("Proyecto simulacion 1")

GND = circuito.addNode()
n1 = circuito.addNode()
n2 = circuito.addNode()
n3 = circuito.addNode()
n4 = circuito.addNode()

Ra = circuito.addResistor(1, n1, n2)
Rb = circuito.addResistor(1, n2, GND)
Rc = circuito.addResistor(1, n2, n4)
Rd = circuito.addResistor(1, n4, n3)
Re = circuito.addResistor(1, n3, GND)

Va = circuito.addVDC(12, n1, GND)
Vb = circuito.addVDC(5, n4, n3)

# --------- Fin de la descripción del circuito

Ra.getV()
print("El valor de Ra es: " + str(Ra.value))
print("El valor de Va es: " + str(Va.value))

# --------- Solución del circuito

circuito.solve()

# --------- Mostrar resultados

# Specify second circuit just to make sure
circuito = Circuit('Test circuit')

