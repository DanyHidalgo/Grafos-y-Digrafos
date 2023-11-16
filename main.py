from grafos import Node, Grafos
from digrafo import NodeD, Digrafos


# Nodes instantiation
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

# Node in memory
print(node_a)
# print(id(node_a))

print('--------------------GRAFOS--------------------')
# Create Grafo
grafo = Grafos()

# Insert at beginning
grafo.insert(node_a, node_b)

print(node_a)
print(node_b)
print(grafo.nodes)
grafo.lista_adyasecente()
lista_adyacencia = grafo.lista_adyascencia
print(lista_adyacencia)
matriz_adyacencia = grafo.lista_adyacencia_a_matriz()

print(matriz_adyacencia)

print(node_a.arista)



print('-------------------DIGRAFOS-------------------')

node_a = NodeD('A')
node_b = NodeD('B')
node_c = NodeD('C')
node_d = NodeD('D')
node_e = NodeD('E')
node_f = NodeD('F')
digrafo = Digrafos()

digrafo.insert(node_a, node_b)

print(node_a)
print(node_b)
print(digrafo.nodes)

matriz_adyacencia_digrafo = digrafo.lista_adyacencia_a_matriz()

print(matriz_adyacencia_digrafo)




