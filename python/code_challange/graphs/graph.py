class Graph:

    def __init__(self):
        self.adjacent_list = {}

    def add_node(self,value):
        v = Vertex(value)
        self.adjacent_list[v] = []
        return v
        # Arguments: value
        # Returns: The added node
        # Add a node to the graph or add to adj list

    def add_edge(self,start_node,end_node, weight=0):
        if start_node not in self.adjacent_list:
            return ' Start node not available in graph'

        if end_node not in self.adjacent_list:
            return 'end node not available in graph'

        adjacencies = self.adjacent_list[start_node]
        adjacencies.append((end_node,weight))
            # Arguments: 2 nodes to be connected by the edge, weight (optional)
            # Returns: nothing
            # Adds a new edge between two nodes in the graph
            # If specified, assign a weight to the edge
            # Both nodes should already be in the Graph

    def get_node(self):
        return self.adjacent_list.keys()
            # Arguments: none
            # Returns all nodes in graph as a collection (set, list, or similar)

    def get_neighbor(self,vertex):
        return self.adjacent_list.get(vertex, [])

            # Arguments: node
            # Returns a collection of edges connected to the given node
                # Include the weight of connection in returned collection

    def size(self):
        return len(self.adjacent_list)

            # Arguments: none
            # Returns the total number of nodes in the graph

    def breadth_first(self,vertex):
        queue = []
        visited = set()
        results= []
        queue.append(vertex)
        visited.add(vertex)

        while len(queue):
            current_vertex = queue.pop(0)
            results.append(vertex.value)
            neighbors = self.get_neighbor(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return results

class Vertex:
    def __init__(self,value):
        self.value = value

class Edge:
    def __init__(self ,vertex,weight=1):
        self.vertex = vertex
        self.weight = weight

