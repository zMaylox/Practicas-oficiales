graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : ['G','H'],
  'G' : [],
  'H' : ['Y','Z'],
  'Y' : [],
  'Z' : []
}

visited = []  # Lista para realizar un seguimiento de los nodos visitados.
queue = []     #Inicializar una cola

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Código del conductor
bfs(visited, graph, 'A')