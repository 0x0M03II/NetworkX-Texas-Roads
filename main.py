import networkx as nx
import sys
import os

# Define the path to the 'src' directory
PROGRAM_ROOT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
SRC_DIRECTORY = os.path.join(PROGRAM_ROOT_DIRECTORY, 'src')

sys.path.append(SRC_DIRECTORY)

# Now you can import from your packages
from core.initialize_single_shortest import InitializeShortestPath
from utils.load_data_network import LoadNetworkData
from core.node_object import Node

DATA_SOURCE_FILE = os.path.join(
    PROGRAM_ROOT_DIRECTORY,
    'data',
    'roadNet-TX.txt')

DATA_STORAGE_FILE = os.path.join(
    PROGRAM_ROOT_DIRECTORY,
    'data',
    '_init_load_data.json'
)

if __name__ == "__main__":

# Uncomment below to load raw data from TXT file
# and serialize as JSON

    upload = LoadNetworkData(DATA_SOURCE_FILE)
    upload.save_graph_data_json(DATA_STORAGE_FILE)

# Initialize Graph
    G = nx.DiGraph()

    print("[+] Loading serialized graph data")
    InitializeShortestPath.load_serialized_data_json(
        DATA_STORAGE_FILE, G)
    
    print("[+] Building Initialize path cost estimates")
    
    print("[+] Computing Shortest Path using Dijkstra's algorithm")

