"""-------------------- RADIO ---------------------------



-------------------------------------------- 24 july, 2020"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Circuit():

    def __init__(self):

        self.name = "Circuit Name"
        self.currentList = []

    def play(self): # No se asuste son nombres temporales
        pass

class Node():

    def __init__(self, name = ""):
        
        self.name = name

    def getV(self, nam = ""):
        
        print("Tome su pinche tension")

class Source():
    pass    

class Resistor():

    def __init__(self, value):
        
        node_0 = Node()
        node_1 = Node()
        self.value = value



