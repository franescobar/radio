"""-------------------- RADIO ---------------------------



-------------------------------------------- 24 july, 2020"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Circuit():

    def __init__(self, cname):

        self.name = cname
        self.VDCList = []
        self.resistorList = []
        self.nodeList = []

    def solve(self):
        pass

    def addNode(self):

        n = Node()
        self.nodeList.append(n)
        return n

    def addResistor(self, value, n0, n1):

        r = Resistor(value, n0, n1)
        self.resistorList.append(r)
        return r

    def addVDC(self, value, np,nm):

        v = VDC(value, np,nm)
        self.resistorList.append(v)
        return v

class Node():

    def __init__(self, name = ""):
        pass

    def getV(self, nam = ""):
        
        print("Tome su pinche tension")

class VDC():

    def __init__(self, value, np,nm):           # Plus node and minus node
        
        self.nodePlus = np
        self.nodeMinus = nm
        self.value = value
 

class Resistor():

    def __init__(self, value, n0, n1):
        
        self.nodeA = n0
        self.nodeB = n1
        self.value = value

    def getV(self):
        
        print("Tome su pinche tension")



