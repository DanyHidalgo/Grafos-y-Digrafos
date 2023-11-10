import pandas as pd
import numpy as np

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
        self.nodo_a_indice = {}

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
        

    def insert(self, new_node: Node, connection_node: Node):
    # Verifica si los nodos ya existen en el grafo
        if new_node not in self.nodes:
            self.nodes.append(new_node)
            self.nodo_a_indice[new_node] = len(self.nodes) - 1
            print(f"Agregado nuevo nodo: {new_node.data} con índice {self.nodo_a_indice[new_node]}")
        
        if connection_node not in self.nodes:
            self.nodes.append(connection_node)
            self.nodo_a_indice[connection_node] = len(self.nodes) - 1
            print(f"Agregado nuevo nodo: {connection_node.data} con índice {self.nodo_a_indice[connection_node]}")

        new_node.arista.append(connection_node)
        connection_node.arista.append(new_node)




    def lista_adyacencia_a_matriz(self):
        num_nodos = len(self.nodes)

        # Crea una matriz de adyacencia llena de ceros
        matriz_adyacencia = np.zeros((num_nodos, num_nodos))

        for nodo in self.nodes:
            indice_nodo = self.nodo_a_indice[nodo]
            for vecino in nodo.arista:
                indice_vecino = self.nodo_a_indice[vecino]
                matriz_adyacencia[indice_nodo][indice_vecino] = 1

        # Crea un DataFrame de Pandas a partir de la matriz de adyacencia
        df = pd.DataFrame(matriz_adyacencia, index=range(num_nodos), columns=range(num_nodos))

        return df


