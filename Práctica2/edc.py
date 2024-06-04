from collections import deque

grafo = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'K'],
    'E': ['C', 'F', 'G', 'K'],
    'F': ['E', 'G'],
    'G': ['E', 'F', 'H', 'I'],
    'H': ['G', 'I'],
    'I': ['G', 'H', 'J', 'K'],
    'J': ['I', 'K'],
    'K': ['D', 'E', 'I', 'J', 'L', 'M', 'N', 'O'],
    'L': ['K', 'O'],
    'M': ['K', 'N'],
    'N': ['K', 'M', 'P', 'O'],
    'P': ['N', '0'],
    'O': ['K', 'L', 'N', 'P']
}

def bfs_hasta_nodo_personalizado(grafo, inicio, objetivo):
    visitados_set = set()
    cola = deque([(inicio, [inicio])])
    visitados_set.add(inicio)

    while cola:
        nodo_actual, camino = cola.popleft()
        print(nodo_actual)

        if nodo_actual == objetivo:
            print(f"Se ha alcanzado el nodo {objetivo}. Camino: {camino}")
            return

        for vecino in grafo[nodo_actual]:
            if vecino not in visitados_set:
                cola.append((vecino, camino + [vecino]))
                visitados_set.add(vecino)

nodo_inicio = 'A'
nodo_objetivo = 'O'
print(f"Recorrido BFS hasta el nodo {nodo_objetivo} desde el nodo {nodo_inicio}:")
bfs_hasta_nodo_personalizado(grafo, nodo_inicio, nodo_objetivo)





   




