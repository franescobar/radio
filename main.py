#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from radio.basics import *

#---- Inicio descripción del circuito

circuito = Circuit("Proyecto simulacion 1")

"""
GND = circuito.addNode()
Ra = circuito.addResistor(4, n1, n2)
Va = circuito.addVDC(3.3, n1, GND)
Ia = circuito.addVDC(3.3, n1, GND)
"""
GND = circuito.addNode()
n1 = circuito.addNode()
n2 = circuito.addNode()
n3 = circuito.addNode()
n4 = circuito.addNode()

Ra = circuito.addResistor(800, n1, n2)
Rb = circuito.addResistor(100, n4, GND)
Rc = circuito.addResistor(10000, n2, n4)
Rd = circuito.addResistor(1000, n2, n3)

Ia = circuito.addIDC(0.14, GND, n1)
Ib = circuito.addIDC(0.30, n3, GND)

# --------- Fin de la descripción del circuito

# --------- Solución del circuito

circuito.solve()

# --------- Mostrar resultados

# Specify second circuit just to make sure
circuito = Circuit('Test circuit')

