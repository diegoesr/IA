class Grafo:
    def __init__(self):
        self.vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G'}
        self.vecinos = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'G'],
            'F': ['C'],
            'G': ['E']
        }
        self.d = {u: 0 for u in self.vertices}
        self.f = {u: 0 for u in self.vertices}

    def obtener_vecinos(self, u):
        return self.vecinos[u]

def DFS_Limitado(grafo, limite):
    V = grafo.vertices
    estado = {u: 'NO_VISITADO' for u in V}
    padre = {u: None for u in V}
    tiempo = [0]

    for inicio in V:
        if estado[inicio] == 'NO_VISITADO':
            DFS_Limitado_Visitar(grafo, inicio, estado, padre, tiempo, limite)

def DFS_Limitado_Visitar(grafo, u, estado, padre, tiempo, limite):
    if limite == 0:
        return

    estado[u] = 'VISITADO'
    tiempo[0] += 1
    grafo.d[u] = tiempo[0]

    for v in grafo.obtener_vecinos(u):
        if estado[v] == 'NO_VISITADO':
            padre[v] = u
            DFS_Limitado_Visitar(grafo, v, estado, padre, tiempo, limite - 1)

    estado[u] = 'TERMINADO'
    tiempo[0] += 1
    grafo.f[u] = tiempo[0]

# se crea una instancia del grafo
grafo = Grafo()

# llama a la función DFS_Limitado con el grafo previamente creado con un límite de 3
DFS_Limitado(grafo, 3)
print("DFS Limitado:", grafo.d, grafo.f)
