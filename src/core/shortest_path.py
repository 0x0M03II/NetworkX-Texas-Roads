# Implement Dijkstra's Shortest Path on Nodes Objects in Graph

class Dijkstras:
    
    def DijkstraShortestPath():
        '''
        DSP Pseudocode from Grad school book

        INITIALIZE-SINGLE-SOURCE(G, s)
        S == 0
        Q == 0

        For every v in G.V:
            INSERT(Q, v)
        
        While Q is not empty:
            u = EXTRACT-MIN(Q)
            S = S union {u}

            for every v in AdjacencyList[u]:
                RELAX(u, v, w)
                if RELAX changed distance
                    Reduce(u, v, w)
        
        Remember, relaxing is for any (u, v) in the set of edges E,
            - if a shorter path to v exists through u
                - such that u.distance + weight(edge) < v.distance
                - update v.distance = u.distance + weight(edge)
        '''

