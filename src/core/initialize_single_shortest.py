import sys
import json
from core import Node

class InitializeShortestPath(object):

    @classmethod
    def InitializeShortestPath(cls, NetworkGraphObject):
        for node in NetworkGraphObject.G.nodes:
            node.distance = float('inf')
            node.predecessor = None

    @classmethod
    def load_serialized_data_json(self, filepath=None, NetworkGraphObject=None):
        if NetworkGraphObject is None:
            raise ValueError("Missing Network Graph Object")

        if filepath is None:
            filepath = '_init_load_data.json'
            if not os.path.exists(filename):
                raise FileNotFoundError

        print(f"[+] Opening network graph data file {filepath}")
        with open(filepath, 'r') as file:
            graph_data = json.load(file)

        node_cache = {}
        for node_info in graph_data['nodes']:
            node = Node.from_dict(node_info, node_cache)
            node_cache[node.id] = node
            NetworkGraphObject.add_node(node)

        for source_id, target_id in graph_data['edges']:
            source_node = node_cache[source_id]
            target_node = node_cache[target_id]
            NetworkGraphObject.add_edge(source_node, target_node, weight=1)