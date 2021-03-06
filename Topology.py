import networkx as nx
import itertools

class Topology(object):
    def __init__(self,directed=False):
        if directed:
            self.topology = nx.DiGraph
        else:
            self.topology = nx.Graph()
        self.directed = directed

    @staticmethod
    def create_1_way_ring(number_of_islands = 4):
        archipelago = nx.DiGraph()
        archipelago.add_nodes_from(range(1,number_of_islands+1))
        for each_island in range(1,number_of_islands+1):
            if each_island == number_of_islands:
                archipelago.add_edge(each_island,1)
            else:
                archipelago.add_edge(each_island,(each_island+1))
        return archipelago



    @staticmethod
    def create_chain(number_of_islands = 4):
        archipelago = nx.DiGraph()
        archipelago.add_nodes_from(range(1, number_of_islands + 1))
        for each_island in range(1, number_of_islands):
            archipelago.add_edge(each_island, (each_island + 1))
        return archipelago

    @staticmethod
    def create_ring(number_of_islands=4):
        archipelago = nx.Graph()
        archipelago.add_nodes_from(range(1, number_of_islands + 1))
        for each_island in range(1, number_of_islands + 1):
            if each_island == number_of_islands:
                archipelago.add_edge(each_island,1)
            else:
                archipelago.add_edge(each_island, (each_island + 1))
        return archipelago


    @staticmethod
    def create_1_2_ring(number_of_islands = 4):
        archipelago = nx.Graph()
        archipelago.add_nodes_from(range(1, number_of_islands + 1))
        for each_island in range(1, number_of_islands + 1):

            for step in range(1,3):
                to_edge = each_island + step
                if to_edge > number_of_islands:
                    to_edge = to_edge % number_of_islands
                archipelago.add_edge(each_island,to_edge)

        return archipelago


    @staticmethod
    def create_1_2_3_ring(number_of_islands=4):
        archipelago = nx.Graph()
        archipelago.add_nodes_from(range(1, number_of_islands + 1))
        for each_island in range(1, number_of_islands + 1):

            for step in range(1, 4):
                to_edge = each_island + step
                if to_edge > number_of_islands:
                    to_edge = to_edge % number_of_islands
                archipelago.add_edge(each_island, to_edge)

        return archipelago

    @staticmethod
    def create_fully_connected(number_of_islands=4):
        archipelago = nx.Graph()
        archipelago.add_nodes_from(range(1, number_of_islands + 1))
        all_edges = itertools.combinations(range(1,number_of_islands+1),2)
        archipelago.add_edges_from(all_edges)
        return  archipelago


    @staticmethod
    def create_broadcast(number_of_islands = 4, central_node=1):
        archipelago = nx.Graph()
        archipelago.add_nodes_from(range(1, number_of_islands + 1))
        for each_island in range(1,number_of_islands+1):
            if central_node == each_island:
                continue
            archipelago.add_edge(central_node,each_island)
        return archipelago


    def add_edge(self,from_node,to_node,weight=0):
        if self.directed:
            self.topology.add_edge(from_node,to_node,weight = weight)
        else:
            self.topology.add_edge(from_node,to_node)









