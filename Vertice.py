class Vertice:

    def __init__(self,index,content):
        self.index = index
        self.content = content
        self.neighbors = []
        self.saturation = 0
        self.degree = 0

    def getContent(self):
        return self.content

    def setContent(self,content):
        self.content = content

    def calcSaturation(self):
        for neighbor in self.neighbors:
            if neighbor.getContent() != "N":
                self.saturation += 1

    def saturationUp(self):
        self.saturation += 1

    def saturationDown(self):
        self.saturation += 1

    def getSaturation(self):
        return self.saturation

    def setNeighbor(self,vertice):
        self.neighbors.append(vertice)
        self.degree += 1

    def possibleColors(self,order):
        possibilities = list(range(1,order+1))
        setOfpossibilities = set(possibilities)
        alreadyExist = set()
        for neighbor in self.neighbors:
            if neighbor.getContent() == "N":
                continue
            alreadyExist.add(int(neighbor.getContent()))
        setOfpossibilities = setOfpossibilities - alreadyExist
        if (len(setOfpossibilities) == 0):
            return -1
        return list(setOfpossibilities)

    def neighborsSaturationUp(self):
        for neighbor in self.neighbors:
            neighbor.saturationUp()

    def neighborsSaturationDown(self):
        for neighbor in self.neighbors:
            neighbor.saturationDown()
