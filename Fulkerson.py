import networkx as nx

grafo = nx.DiGraph()
grafo.add_nodes_from('ABCDEFGH')
grafo.add_edges_from([
    ('A', 'B', {'capacidad': 4, 'flujo': 0}),
    ('A', 'C', {'capacidad': 5, 'flujo': 0}),
    ('A', 'D', {'capacidad': 7, 'flujo': 0}),
    ('B', 'E', {'capacidad': 7, 'flujo': 0}),
    ('C', 'E', {'capacidad': 6, 'flujo': 0}),
    ('C', 'F', {'capacidad': 4, 'flujo': 0}),
    ('C', 'G', {'capacidad': 1, 'flujo': 0}),
    ('D', 'F', {'capacidad': 8, 'flujo': 0}),
    ('D', 'G', {'capacidad': 1, 'flujo': 0}),
    ('E', 'H', {'capacidad': 7, 'flujo': 0}),
    ('F', 'H', {'capacidad': 6, 'flujo': 0}),
    ('G', 'H', {'capacidad': 4, 'flujo': 0}),
])

def DFS(g, fuente, destino):
    grafo = g.to_undirected()
    visitado = {fuente}
    pila = [(fuente, 0, dict(grafo[fuente]))]
    while pila:
        print("Ultimo en pila: ",pila[-1])
        v, p, vecinos = pila[-1] #ultimo de la lista
        print("P: ",p)
        if v == destino:
            break
        while vecinos:
            u, e = vecinos.popitem()
            if u not in visitado:
                break
        else:
            x = pila.pop()
            print("Pop: ", x)
            continue        
        arista_v_u = g.has_edge(v, u)
        print("V: ", v)
        print("U: ", u)
        print("E: ",e)
        capacidad = e['capacidad']
        flujo = e['flujo']
        vecinos = dict(grafo[u])
        print("Vecinos: ",vecinos)
        if arista_v_u and flujo < capacidad:
            pila.append((u, capacidad - flujo, vecinos))
            visitado.add(u)
        elif not arista_v_u and flujo:
            pila.append((u, flujo, vecinos))
            visitado.add(u)
    reserva = min((f for _, f, _ in pila[1:]), default=0)
    recorrido = [v for v, _, _ in pila]    
    return recorrido, reserva
    
def mostrar_flujo(recorrido, reserva, flujo):
    print('Flujo ha aumentado en', reserva, 
          'en el recorrido', recorrido,
          '. Flujo total: ', flujo)

def ford_fulkerson(g, fuente, destino):
    flujo, recorrido = 0, True
    print("Origen: ", fuente)
    while recorrido:
        recorrido, reserva = DFS(g, fuente, destino)
        flujo += reserva
        for v, u in zip(recorrido, recorrido[1:]):
            if g.has_edge(v, u):
                g[v][u]['flujo'] += reserva
            else:
                g[u][v]['flujo'] -= reserva    
        mostrar_flujo(recorrido, reserva, flujo)
    return

ford_fulkerson(grafo, 'A', 'H')