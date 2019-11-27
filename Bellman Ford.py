from random import *
from math import *
INF = float("inf")

def generarGrafoConPesos(n,m):
    mat = [[] for i in range(n)]
    for j in range(m):
        v1 = randint(0, n - 1)
        v2 = randint(0, n - 1)
        w = randint(1, 10)
        adyacentes = [x[0] for x in mat[v1]]
        adyacentes2 = [x[0] for x in mat[v2]]
        while(v2 in adyacentes or v2 == v1 or v1 in adyacentes2):
            v1 = randint(0, n - 1)
            v2 = randint(0, n - 1)
        mat[v1] += [(v2,w)]
    return mat

def BellmanFord(g, inicio):
    distancia = [INF]*len(g) #las distancias son todas infinitas en la primera instancia
    pi = [(-1,-1)] * len(g) #cada nodo aun no tiene predecesor
    # se sabe que la distancia del nodo inicio es de 0 ya que estamos ahi
    distancia[inicio] = 0
    for i in range(len(g) -1): #Recorrido es el numero de nodos
        for u in range(len(g)): #Numero de vértices
            for v, w in g[u]:
                # Si la distancia se ha encontrado y la distancia al nodo es menor a la que ya tenía...
                if distancia[u] != INF and distancia[u]+w < distancia[v]:
                    distancia[v] = distancia[u]+w
                    pi[v] = (u,w)
    return distancia,pi

mat = generarGrafoConPesos(7,12)
dist, predecesores = BellmanFord(mat, 0)
print(dist, predecesores)

def hacerRecorridosBellmanFord(g,inicio):
    distancia, predecesores = BellmanFord(g, inicio)
    recorrido = []
    for u in range(len(predecesores)):
        if predecesores[u][0] > -1:
            recorrido += [(predecesores[u][0],u,predecesores[u][1])]
    return recorrido
recorrido = hacerRecorridosBellmanFord(mat, 0)
print(recorrido)