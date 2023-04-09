import numpy as np

class Edge():

    def __init__(self, v1, v2, waga):
        self.vertex1 = v1
        self.vertex2 = v2
        self.waga = waga


class Graph():
    vertexList = []
    visited_DFS = []
    visited_BFS = []
    queue = []

    def __init__(self):
        vertexList = []

    def createVertives(self, ile):
        for i in range(ile):
            lista = []
            self.vertexList.append(lista)

    def addEdge(self, v1, v2, waga):
        self.vertexList[v1].append(Edge(v1, v2, waga))

    def removeEdge(self, v1, v2):
        for i in range(len(self.vertexList[v1])):
            if self.vertexList[v1][i].vertex2 == v2:
                self.vertexList[v1].remove(self.vertexList[v1][i])

    def checkEdge(self, pierwsza, druga):
        for i in range(len(self.vertexList[pierwsza])):
            if(self.vertexList[pierwsza][i].vertex2 == druga):
                return True
        return False

    def printNeighbourIndices(self, idx):
        print(f'Sąsiedzi wierzchołka {idx}: ', end='')
        for i in range(len(self.vertexList[idx])):
            print(f'{self.vertexList[idx][i].vertex2} waga: {self.vertexList[idx][i].waga}', end=', ')
        print()

    def printAllNeighbourIndices(self):
        for i in range(len(self.vertexList)):
            print(f'Sąsiedzi wierzchołka {i}: ', end='')
            for j in range(len(self.vertexList[i])):
                print(f'{self.vertexList[i][j].vertex2} waga: {self.vertexList[i][j].waga}', end=', ')
            print()

    def vertexDegree(self, idx):
        return len(self.vertexList[idx])

    def getNumberOfVertex(self):
        return len(self.vertexList)

    def getNumberOfEdges(self):
        countEdges = 0
        for i in range(len(self.vertexList)):
            countEdges += len(self.vertexList[i])
        return countEdges

    def getWeight(self, pierwsza, druga):
        for i in range(len(self.vertexList[pierwsza])):
            if self.vertexList[pierwsza][i].vertex2 == druga:
                return self.vertexList[pierwsza][i].waga

    def clearGraph(self):
        self.vertexList.clear()

    def readFromFile(self, path):
        self.clearGraph()
        f = open(path)
        lines = f.readlines()
        count = 0
        for i in lines:
            if count == 0:
                self.createVertives(int(i))
                count += 1
            else:
                splitek = i.split(' ')
                self.addEdge(int(splitek[0]), int(splitek[1]), int(splitek[2]))

        f.close()

    def sortGraf(self):
        for i in range(len(self.vertexList)):
            self.vertexList[i].sort(key=lambda x: x.vertex2)

    def bfs(self, vertex):
        self.visited_BFS.append(vertex)
        self.queue.append(vertex)

        while self.queue:
            m = self.queue.pop(0)
            print(m, end=', ')

            for i in self.vertexList[m]:
                if i.vertex2 not in self.visited_BFS:
                    self.visited_BFS.append(i.vertex2)
                    self.queue.append(i.vertex2)
        print()

    def dfs(self, vertex):
        if vertex not in self.visited_DFS:
            print(vertex, end=', ')
            self.visited_DFS.append(vertex)
            for i in self.vertexList[vertex]:
                self.dfs(i.vertex2)

    def floyd(self):
        v = len(self.vertexList)
        dist = np.zeros((v, v))
        for i in range(v):
            for j in range(v):
                if i == j:
                    dist[i][j] = 0
                else:
                    dist[i][j] = 999999

        for i in range(v):
            for j in range(len(self.vertexList[i])):
                dist[i][self.vertexList[i][j].vertex2] = self.vertexList[i][j].waga

        for k in range(v):
            for i in range(v):
                for j in range(v):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        for i in range(v):
            print()
            for j in range(v):
                print(dist[i][j], end='   ')


################## TESTY ##################
graf = Graph()
graf.readFromFile('./floyd.txt')
graf.sortGraf()
#graf.removeEdge(5, 3)
graf.printNeighbourIndices(5)
print()
graf.printAllNeighbourIndices()
print()
print("Czy krawędź istnieje: " + str(graf.checkEdge(5, 3)))
print("Stopień wierzchołka 5: " + str(graf.vertexDegree(5)))
print()
print("BFS: ")
graf.bfs(5)
print("DFS: ")
graf.dfs(5)
print()
print()
print("Liczba wierzchołków: " + str(graf.getNumberOfVertex()))
print("Liczba krawędzi: " + str(graf.getNumberOfEdges()))
print("Waga podanej krawędzi: " + str(graf.getWeight(5, 9)))
print()
print("Macierz Floyda: ", end='')
graf.floyd()
print()
print()

#dodanie i usuniecie krawedzi
print("Czy krawędź 6,8 istnieje? " + str(graf.checkEdge(6, 8)))
graf.addEdge(6, 8, 3)
print("Dodano krawędź 6,8")
print("Czy krawędź 6,8 istnieje? " + str(graf.checkEdge(6, 8)))
graf.removeEdge(6, 8)
print("Usunięto krawędź 6,8")
print("Czy krawędź 6,8 istnieje? " + str(graf.checkEdge(6, 8)))