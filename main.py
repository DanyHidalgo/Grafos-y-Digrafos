from grafos import Node, Grafos


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

# Create LL
ll = Grafos()

# Insert at beginning
ll.insert(node_a, node_b)

print(node_a)
print(node_b)
print(ll.nodes)
ll.lista_adyasecente()
lista_adyacencia = ll.lista_adyascencia
print(lista_adyacencia)
matriz_adyacencia = ll.lista_adyacencia_a_matriz()

print(matriz_adyacencia)

print(node_a.arista)