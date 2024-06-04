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

def DFS_Iterativo(grafo):
    V = grafo.vertices
    estado = {u: 'NO_VISITADO' for u in V}
    padre = {u: None for u in V}
    tiempo = [0]

    for inicio in V:
        if estado[inicio] == 'NO_VISITADO':
            stack = [inicio]

            while stack:
                u = stack.pop()
                if estado[u] == 'NO_VISITADO':
                    estado[u] = 'VISITADO'
                    tiempo[0] += 1
                    grafo.d[u] = tiempo[0]

                    for v in grafo.obtener_vecinos(u):
                        if estado[v] == 'NO_VISITADO':
                            padre[v] = u
                            stack.append(v)

                    estado[u] = 'TERMINADO'
                    tiempo[0] += 1
                    grafo.f[u] = tiempo[0]

# crea una instancia del grafo
grafo = Grafo()

# llama a la función DFS_Iterativo con el grafo previamentecreado
DFS_Iterativo(grafo)
print("DFS Iterativo:", grafo.d, grafo.f)
