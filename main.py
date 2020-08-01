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
n5 = circuito.addNode()

Ra = circuito.addResistor(4, n1, n2)
Rb = circuito.addResistor(4, n2, n3)
Rc = circuito.addResistor(8, n3, n5)
Rd = circuito.addResistor(3, n3, n5)
Re = circuito.addResistor(12, n5, n4)
Rf = circuito.addResistor(7, n2, n4)
Rg = circuito.addResistor(6, n4, GND)

Va = circuito.addVDC(3.3, n1, GND)
Vb = circuito.addVDC(5, n2, n4)
Vc = circuito.addVDC(12, n3, n5)


# --------- Fin de la descripción del circuito

# --------- Solución del circuito

circuito.solve()

# --------- Mostrar resultados

# Specify second circuit just to make sure
circuito = Circuit('Test circuit')

