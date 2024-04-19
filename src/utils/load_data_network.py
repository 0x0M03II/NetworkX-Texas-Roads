import os
import json
import networkx as nx
from core import Node

class LoadNetworkData:
    def __init__(self, filename):
        self.filename = filename
        self.G = nx.DiGraph()
        self.load_network_data()  # Call the loading function

    def load_network_data(self):
        print(f"[+] Loading graph data from source TXT file {self.filename}")
        with open(self.filename, 'r') as file:
            node_cache = {}
            for line in file:
                if line.startswith("#"):
                    continue

                source_id, target_id  = \
                    line.strip().split()

                source_node = node_cache.setdefault(
                    source_id, Node(source_id))

                target_node = node_cache.setdefault(
                    target_id, Node(target_id))

                self.G.add_edge(source_node, target_node)

    def save_graph_data_json(self, filepath=None):
        if filepath is None:
            # try generic local name
            filepath = '_init_load_data.json'
            if not os.path.exists(filename):
                raise FileNotFoundError

        print(f"Saving serialized network graph data in {filepath}.")
        node_data = {node.id: node.to_dict() for node in self.G.nodes()}
        edge_data = [(edge[0].id, edge[1].id) for edge in self.G.edges()] 
        graph_json = {
            'nodes': list(node_data.values()),
            'edges': edge_data
        }
        
        with open(filepath, 'w') as file:
            json.dump(graph_json, file)
