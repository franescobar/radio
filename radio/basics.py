"""-------------------- RADIO ---------------------------



-------------------------------------------- 24 july, 2020"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

class Circuit():

    def __init__(self, cname):

        self.name = cname
        self.VDCList = []
        self.resistorList = []
        self.nodeList = []

    def solve(self):

        # Build b
        b = np.zeros([len(self.nodeList) - 1 + len(self.VDCList), 1])
        vdc = [source.value for source in self.VDCList]
        b[-len(vdc):, 0] = vdc
        
        print(b)
        # Build A
        A = np.zeros([len(self.nodeList) - 1 + len(self.VDCList),
                      len(self.nodeList) - 1 + len(self.VDCList)])
       
        # Include coefficients of LCK due to resistances
        for R in self.resistorList:
            # Get terminal indices (GND will have index -1)
            i = self.nodeList.index(R.nodeA) - 1
            j = self.nodeList.index(R.nodeB) - 1
            # Add entries to A
            if i == -1:
                A[j, j] += 1/R.value
            elif j == -1:
                A[i, i] += 1/R.value
            else:
                A[i, i] += 1/R.value
                A[j, j] += 1/R.value
                A[i, j] -= 1/R.value
                A[j, i] -= 1/R.value

        # Include coefficients due to voltage sources
        for (k, vdc) in enumerate(self.VDCList):
            # Get terminal indices (GND will again have index -1)
            i = self.nodeList.index(vdc.nodePlus) - 1
            j = self.nodeList.index(vdc.nodeMinus) - 1
            # Add entries to A
            if i != -1:
                # LCK
                print(k)
                A[i, len(self.nodeList) - 1 + k] = -1
                # LTK
                A[len(self.nodeList) - 1 + k, i] = 1
            if j != -1:
                # LCK
                A[j, len(self.nodeList) - 1 + k] = 1
                # LTK
                A[len(self.nodeList) - 1 + k, j] = -1

        print(A)
        # Solve
        # x = np.matmul(np.linalg.inv(A), b)
        # Print voltages
        # print('Node voltages: ', x[:len(self.nodeList)])
        pass

    def addNode(self):

        n = Node()
        self.nodeList.append(n)
        return n

    def addResistor(self, value, n0, n1):

        r = Resistor(value, n0, n1)
        self.resistorList.append(r)
        return r

    def addVDC(self, value, np, nm):

        v = VDC(value, np, nm)
        self.VDCList.append(v)
        return v

class Node():

    def __init__(self, name = ""):
        pass

    def getV(self, nam = ""):
        
        print("Tome su pinche tension")

class VDC():

    def __init__(self, value, np, nm):           # Plus node and minus node
        
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
