class Node:
    val: int
    def __init__(self, val: int):
        self.parent: Node = self
        self.val = val

class UnionFind:
    storage: Dict[int,Node] = {}
    rank: Dict[int, int] = {}
    roots: set[int]
    def __init__(self, n: int):
        self.roots = set()
        for i in range(n):
            self.storage[i] = Node(i)
            self.rank[i] = 1
            self.roots.add(i)
            print("Roots len " + str(len(self.roots)))

    def find(self, x: int) -> int:
        curNode = self.storage[x]
        while curNode.parent != curNode:
            curNode = curNode.parent
        return curNode.val

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    
    def __buildPathSet(self, x: int) -> set[Node]:
        path: set[Node] = set()
        curNode = self.storage[x]
        selfParented = False
        while not selfParented:
            path.add(curNode)
            selfParented = curNode == curNode.parent
            if not selfParented:
                curNode = curNode.parent
        return path

    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x, y): return False
        xRoot = self.storage[self.find(x)]
        yRoot = self.storage[self.find(y)]
        if self.rank[xRoot.val] > self.rank [yRoot.val]:
            self.roots.remove(yRoot.val)
            yRoot.parent = xRoot
            return True
        if self.rank[xRoot.val] < self.rank [yRoot.val]:
            self.roots.remove(xRoot.val)
            xRoot.parent = yRoot
            return True
        
        yRoot.parent = xRoot
        self.roots.remove(yRoot.val)
        self.rank[xRoot.val] += 1

        return True

    def getNumComponents(self) -> int:
        return len(self.roots)

