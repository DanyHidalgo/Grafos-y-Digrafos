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

        new_node.arista.append(connection_node.data)
        connection_node.arista.append(new_node.data)



    def lista_adyacencia_a_matriz(self, lista_adyacencia):
        num_nodos = len(self.nodes)

        # Crea una matriz de adyacencia llena de ceros
        matriz_adyacencia = np.zeros((num_nodos, num_nodos))

        # Rellena la matriz de adyacencia con 1s donde hay conexiones en la lista de adyacencia
        for nodo, vecinos in enumerate(lista_adyacencia):
            if nodo in self.nodo_a_indice:
                for vecino in vecinos:
                    if vecino in self.nodo_a_indice:
                        matriz_adyacencia[self.nodo_a_indice[nodo]][self.nodo_a_indice[vecino]] = 1
            else:
                # Aquí puedes manejar el caso donde un nodo no está en el diccionario (opcional)
                print(f"El nodo {nodo} no está en el diccionario")

        # Crea un DataFrame de Pandas a partir de la matriz de adyacencia
        df = pd.DataFrame(matriz_adyacencia, index=range(num_nodos), columns=range(num_nodos))

        return df

