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
ll.insert(node_b, node_c)
ll.insert(node_c, node_d)
ll.insert(node_d, node_a)
ll.insert(node_a, node_e)
ll.insert(node_b, node_f)

print(node_a)
print(node_b)
print(ll.nodes)
ll.lista_adyasecente()
lista_adyacencia = ll.lista_adyascencia
print(lista_adyacencia)
matriz_adyacencia = ll.lista_adyacencia_a_matriz(lista_adyacencia)

print(matriz_adyacencia)

