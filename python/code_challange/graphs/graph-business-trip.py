from graph import Graph

def busness_trip(Graph,array):
        direction1 = False
        direction2 = False
        total = 0
        for vertex in range(len(array) - 1):
            adjacency = Graph.adjacent_list[array[vertex]]
            direction2 = False
            for edges in adjacency:
                if array[vertex + 1] == edges.vertex:
                    total += edges.weight
                    direction1 = True
                    direction2 = True
        path = direction1 and direction2
        if not path:
            total = 0
            path = False
            return f'{path},${total}'
        return f'{path},${total}'
