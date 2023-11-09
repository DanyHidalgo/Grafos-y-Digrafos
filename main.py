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
ll.insert(node_a,node_b)

print(node_a)
print(node_b)
print(ll.nodes)
ll.lista_adyasecente()
n = ll.lista_adyascencia
print(n)
ll.lista_adyacencia_a_matriz(n)
