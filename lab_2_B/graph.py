
class Graph:
    """
    The purpose of the class is to provide a clean way to define a graph for
    a searching algorithm:
    """

    def __init__(self):
        self.edges = {} # dictionary of edges NODE: NEIGHBOURS

    def neighbours(self, node):
        """
        The function returns the neighbour of the node passed to it,
        which is essentially the value of the key in the edges dictionary.

        :params node: (string) a node in the graph

        :return: (list) neighbouring nodes
        """

        return self.edges[node]



if __name__ == "__main__":
    # testing out the graph class
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {
        'A': set(['B', 'D']),
        'B': set(['A','E','C']),
        'C': set(['B', 'E', 'G']),
        'D': set(['A','E','F']),
        'E': set(['B', 'C', 'D', 'G']),
        'F': set(['D','G']),
        'G': set(['F','E','C'])
    }

    print("Cost going from A to D is:", graph.get_cost('A','D'))