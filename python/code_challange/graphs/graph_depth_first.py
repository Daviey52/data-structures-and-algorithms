from stack.stack import Stack
from graph import Graph

def depth_first_search(self,vertex):
    if vertex not in self.get_node():
        return []
    result , stack, visited = [], Stack(), set()
    stack.push(vertex)
    while stack:
        top=stack.peek()
        if top not in visited:
            result.append(top.value)
        visited.add(top)
        has_unvisted = False
        children = [edge.vertex for edge in self.get_neighbor(top)]
        for child in children:
            if child not in visited:
                has_unvisted =True
                stack.push(child)
                break
        if not has_unvisted:
            stack.pop()
    return result

