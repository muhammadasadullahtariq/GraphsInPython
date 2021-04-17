#creating class for nodes
class adj_node:
    def _init_(self, vertex):
        self.vertex = vertex
        self.next = None
#creating class for bidirectional search
class bds:
    def _init_(self, vertices):
#initializing vertices and graph with vertices
        self.vertices = vertices
        self.graph = [None] * self.vertices
#initializing parent nodes
        self.src_parent = [None] * self.vertices
        self.dest_parent = [None] * self.vertices
#initializing visited nodes as False
        self.src_visited = [False] * self.vertices
        self.dest_visited = [False] * self.vertices
#initializing queue for forward and backward searches
        self.src_queue = list()
        self.dest_queue = list()

#adding undirected edge to list
    def add_edge(self, src, dest):
        node = adj_node(dest)
        node.next = self.graph[src]
#assigning adjacent nodes to graph
        self.graph[src] = node
        node = adj_node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node
#creating func() for BFS
    def bfs(self, direction='forward'):
        if direction == 'forward':
#directing forward search
            current = self.src_queue.pop(0)
            connected_node = self.graph[current]
            while connected_node:
                vertex = connected_node.vertex
                if not self.src_visited[vertex]:
                    self.src_queue.append(vertex)
                    self.src_visited[vertex] = True
                    self.src_parent[vertex] = current
                connected_node = connected_node.next

        else:
#directing backward search
            current = self.dest_queue.pop(0)
            connected_node = self.graph[current]
            while connected_node:
                vertex = connected_node.vertex

                if not self.dest_visited[vertex]:
                    self.dest_queue.append(vertex)
                    self.dest_visited[vertex] = True
                    self.dest_parent[vertex] = current

                connected_node = connected_node.next

#checking for intersecting vertex
    def is_intersecting(self):
        for x in range(self.vertices):
            if (self.src_visited[x] and
                    self.dest_visited[x]):
                return x
#returning intersecting node if exists
        return -1

#printing the path of search
    def print_path(self, intersectnode, src, dest):
        path = list()
        path.append(intersectnode)
        x = intersectnode
        while x != src:
            path.append(self.src_parent[x])
            x = self.src_parent[x]
        path = path[::-1]
        x = intersectnode
        while x != dest:
            path.append(self.dest_parent[x])
            x = self.dest_parent[x]
        path = list(map(str, path))
        print(' '.join(path))
#creating func() for bds
    def bidirectionalsearch(self, src, dest):
#adding source node to queue and set visited as True
        self.src_queue.append(src)
        self.src_visited[src] = True
        self.src_parent[src] = -1
#adding destination node to queue and set visited as True
        self.dest_queue.append(dest)
        self.dest_visited[dest] = True
        self.dest_parent[dest] = -1
        while self.src_queue and self.dest_queue:
            # BFS in forward direction from Source Vertex
            self.bfs(direction='forward')
            # BFS in reverse direction from Destination Vertex
            self.bfs(direction='backward')
#checking for intersecting vertex
            intersection = self.is_intersecting()
            if intersection != -1:
                print(f"Path exists between {src} and {dest}")
                print(f"Intersection at {intersection}")
                self.print_path(intersection, src, dest)
                exit(0)
        return -1
#specifing the interpreter for highest priorty
if _name_ == '_main_':
    num = 13
#defining source and destination index
    src = 0
    dest = 12
    graph = bds(num)
    graph.add_edge(0, 4)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(2, 6)
    graph.add_edge(4, 6)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)
    graph.add_edge(7, 9)
    graph.add_edge(8, 9)
    graph.add_edge(9, 10)
    graph.add_edge(10, 11)
    graph.add_edge(10, 12)
    result = graph.bidirectionalsearch(src, dest)