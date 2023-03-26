class un_graph:
    def __init__(self):
        self.node_list = []
        self.edges = {}
        self.hm = {}
    
    def add_node(self,name):
        self.node_list.append(name)
        self.edges[name] = []
    
    def add_edge(self, node1, node2, distance, heading):
        if(self.node_list.count(node1) == True and self.node_list.count(node2) == True):
            self.edges[node1].append(node2) 
            self.edges[node2].append(node1)
            key1 = node1 + "," + node2
            key2 = node2 + "," + node1
            self.hm[key1] = [distance, heading]
            if(heading > 180):
                self.hm[key2] = [distance, heading - 180]
            else:
                self.hm[key2] = [distance, heading + 180]
        else:
            print("Node non existant.")
    
    def constr(self, ls):
        for i in range(len(ls)):
            if(self.node_list.count(ls[i][0]) == False):
                self.add_node(ls[i][0])
            if(self.node_list.count(ls[i][1]) == False):
                self.add_node(ls[i][1])
            if(self.edges[ls[i][0]].count(ls[i][1]) == False and self.edges[ls[i][1]].count(ls[i][0]) == False):   
                self.add_edge(ls[i][0], ls[i][1], int(ls[i][2]), int(ls[i][3]))
   
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.edges.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

def update_list(ls, doc):
    file = open(doc)
    ls = []
    print(f"Updating list from {doc} ...")
    while True:
        line = file.readline()
        if(line == ""):
            break
        else:
            l = line.strip().split(",")
            ls.append(l)
    return ls
    print("List has been updated.")