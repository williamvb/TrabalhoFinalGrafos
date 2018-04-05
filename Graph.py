import sys
import math
from Vertice import *

class Graph:

    def __init__(self,cells):
        self.numberOfVertices = len(cells)
        self.order = int(math.sqrt(self.numberOfVertices))
        self.blocDimension = int(math.sqrt(self.order))
        self.vertices = self.buildVertices(cells,self.numberOfVertices)
        self.blocs = self.buildBlocs(self.numberOfVertices,self.blocDimension,self.order)
        self.mergeNeighbors(self.order)

    def buildVertices(self,cells,numberOfVertices):
        vertices = {}
        for i in range(numberOfVertices):
            vertices[i] = Vertice(i,cells[i])
        return vertices

    def buildBlocs(self,numberOfVertices,blocDimension,order):
        blocList = []
        for firstBlocVertical in range (0,numberOfVertices,blocDimension*order):
            for firstBlocHorizontal in range(firstBlocVertical, firstBlocVertical+order, blocDimension):
                bloc = set()
                for vertical in range(firstBlocHorizontal,firstBlocHorizontal + order*blocDimension-1,order):
                    for horizontal in range(vertical,vertical+blocDimension):
                        bloc.add(horizontal)
                blocList.append(bloc)
        return blocList

    def lineNeighbors(self,index,order):
        mod = index % order
        dif = order - mod
        lim = index + dif

        neighbors = set()
        for i in range(index-mod,lim):
            neighbors.add(i)
        return neighbors

    def columnNeighbors(self,index,order):
        neighbors = set()
        for goingUp in range(index,0,-order):
            neighbors.add(goingUp)
        for goindDown in range(index,self.numberOfVertices,order):
            neighbors.add(goindDown)
        return neighbors

    def blocNeighbors(self,index):
        for bloc in self.blocs:
            if index in bloc:
                return bloc

    def mergeNeighbors(self,order):
        for vertice in self.vertices:
            lineNeighbors = self.lineNeighbors(vertice,order)
            columnNeighbors = self.columnNeighbors(vertice,order)
            blocNeighbors = self.blocNeighbors(vertice)
            neighbors = lineNeighbors | columnNeighbors | blocNeighbors
            self.assignNeihbors(vertice,neighbors)

    def assignNeihbors(self,vertice,neighbors):
        for neighbor in neighbors:
            if (vertice != neighbor):
                self.vertices[vertice].setNeighbor(self.vertices[neighbor])
        self.vertices[vertice].calcSaturation()

    def biggerSaturation(self):
        biggerSaturation = 0
        biggerIndex = 0
        for vertice in self.vertices:
            if self.vertices[vertice].getSaturation() > biggerSaturation and self.vertices[vertice].getContent() == "N":
                biggerSaturation = self.vertices[vertice].getSaturation()
                biggerIndex = vertice
        return biggerIndex

    def allColorful(self):
        for vertice in self.vertices:
            if self.vertices[vertice].getContent() == "N":
                return False
        return True

    def uncoloredVertices(self):
        uncoloredVertices = set()
        for vertice in self.vertices:
            if (self.vertices[vertice].getContent() == "N"):
                uncoloredVertices.add(vertice)
        return uncoloredVertices

    def dSatur(self):
        if self.allColorful():
            return True
        biggerSaturation = self.biggerSaturation()
        possibleColors = self.vertices[biggerSaturation].possibleColors(self.order)
        if possibleColors == -1:
            return False
        if not possibleColors:
            return False
        for color in possibleColors:
            self.vertices[biggerSaturation].setContent(color)
            self.vertices[biggerSaturation].neighborsSaturationUp()
            if self.dSatur():
                return True
            else:
                self.vertices[biggerSaturation].neighborsSaturationDown()
                self.vertices[biggerSaturation].setContent("N")
        return False

    def solve(self,output_name):
        if self.dSatur():
            print ("Solução encontrada! Resposta no arquivo:",output_name)
        else:
            print("Solução não encontrada!")

    def writeFile(self,output_name):
        output_file = open(output_name, "w+")
        for vertices in self.vertices:
            if(vertices % self.order == 0 and vertices != 0):
                print("",file=output_file)
            print(self.vertices[vertices].getContent(),"",end="",file=output_file)
