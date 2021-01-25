
from queue import PriorityQueue
v = 20
graph = [[] for i in range(v)]
 
# Función para implementar la mejor primera búsqueda
# Da una ruta de salida con el costo más bajo
 
 
def best_first_search(source, target, n):
    visited = [0] * n
    visited[0] = True
    pq = PriorityQueue()
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        print(u, end=" ")
        if u == target:
            break
 
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()
 
# Función para agregar bordes al gráfico
 
 
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
 
 

# implementado usando enteros agregados (x, y, costo);
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)
addedge(10, 14, 1)
addedge(10, 15, 12)
addedge(16, 17, 18)

#En source se pone el numero en donde quiere iniciar, y en target en donde quiere finalizar
#(Si no hay ruta que lo lleve al resultado final, termina en el ultimo)
source = 0
target = 14
best_first_search(source, target, v)
 
# El codigo original está hecho por Jyotheeswar Ganne y lo modificamos
