# Node class for each vertex
import json

class Node:
    def __init__(self, id):
        self.id = id
        self.distance = float('inf')
        self.predecessor = None
    
    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def to_dict(self):
        return {
            'id': self.id,
            'distance': self.distance,
            'predecessor': self.predecessor.id if self.predecessor else None
        }

    @staticmethod
    def from_dict(data, node_cache):
        node = Node(data['id'])
        node.distance = data['distance']
        if data['predecessor'] is not None:
            node.predecessor = node_cache[data['predecessor']]
        return node