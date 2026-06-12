class Edge:
    to: 'Node'

class Node:
    val: int
    edges: list[Edge]
    def __init__(self):
        self.edges = []

class Graph:
    nodes: Dict[int, Node] = {}
    
    def __init__(self):
        pass

    def addEdge(self, src: int, dst: int) -> None:
        createdNode = False

        dstNode = self.nodes.get(dst)
        if dstNode == None:
            dstNode = Node()
            dstNode.val = dst
            self.nodes[dst] = dstNode
            createdNode = True
        # else: print("found {d}".format(d=dst))
        srcNode = self.nodes.get(src)
        if srcNode == None:
            srcNode = Node()
            srcNode.val = src
            self.nodes[src] = srcNode
            createdNode = True
        # else: print("found {s}".format(s=src))
        
        # search for dstNode in srcNode edges
        found = False
        for edge in srcNode.edges:
            if edge.to.val == dst:
                found = True
                break
            
        if createdNode or not found:
            newEdge = Edge()
            newEdge.to = dstNode
            srcNode.edges.append(newEdge)
            # print("appended {d} to {s}".format(d=dst,s=src))
            

    def removeEdge(self, src: int, dst: int) -> bool:
        dstNode = self.nodes.get(dst)
        if dstNode == None:
            return False
        srcNode = self.nodes.get(src)
        if srcNode == None:
            return False
        # search for dstNode in srcNode edges
        for i in range(len(srcNode.edges)):
            edge = srcNode.edges[i]
            if edge.to.val == dst:
                srcNode.edges.pop(i)
                return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        dstNode = self.nodes.get(dst)
        if dstNode == None:
            return False
        srcNode = self.nodes.get(src)
        if srcNode == None:
            return False
        
        # search for dstNode from srcNode
        visited: set[Node] = set()
        foundPath = None
        pathStart = [srcNode]
        foundPath = self.__dfs(visited, pathStart, dst)
        return foundPath != None


    def __dfs(self, visited: set[Node], path: list[Node], dst:int) -> list[Node] | None:
        root = path[len(path) - 1]
        visited.add(root)
        # print("Edges for {r}: ".format(r=root.val) + ",".join(str(edge.to.val) for edge in root.edges))
        for edge in root.edges:
            nextNode = edge.to
            if nextNode in visited:
                continue
            currentPath = path + [nextNode]
            # print("Path: " + ",".join(str(node.val) for node in currentPath))
            if nextNode.val == dst:
                # print("Found!!")
                return currentPath
            searchResult = self.__dfs(visited, currentPath, dst)
            if searchResult != None:
                return searchResult
        return None

