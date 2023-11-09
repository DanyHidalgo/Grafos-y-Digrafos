class Node:
    
    def __init__(self, data: str):
        self.data = data
        self.arista = [] 

        #Arista = Direcciones 
        #Nodo = Vertice 


    def __repr__(self):
        return '| Data: {} Aristas: {} |'.format(self.data, self.arista)


class Grafos:

    def __init__(self):
        self.nodes = []
        self.lista_adyascencia = []

    '''
    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next
    

    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.data)

        nodes.append("NIL")
        return " --> ".join(nodes)
    '''

    def lista_adyasecente(self):
        n = len(self.nodes)
        for i in range(n):
            self.lista_adyascencia.append(self.nodes[i].arista)
        

    def insert(self, new_node: Node, conection_node: Node):

        new_node.arista.append(conection_node.data)
        conection_node.arista.append(new_node.data)
        self.nodes.append(new_node)
        self.nodes.append(conection_node)

