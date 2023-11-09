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



    def lista_adyacencia_a_matriz(self, lista_adyacencia):
        num_nodos = len(lista_adyacencia)

        # Crea una matriz de adyacencia llena de ceros
        matriz_adyacencia = np.zeros((num_nodos, num_nodos))

        # Rellena la matriz de adyacencia con 1s donde hay conexiones en la lista de adyacencia
        for nodo, vecinos in enumerate(lista_adyacencia):
            for vecino in vecinos:
                matriz_adyacencia[nodo][vecino] = 1

        # Crea un DataFrame de Pandas a partir de la matriz de adyacencia
        df = pd.DataFrame(matriz_adyacencia, index=range(num_nodos), columns=range(num_nodos))

        return df
