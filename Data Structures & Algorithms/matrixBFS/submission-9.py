import queue
class Solution:
    toVisit: queue.Queue[tuple[int, int, int]] # x, y, depth
    visited: Set[tuple[int, int]] # x, y
    grid: List[List[int]]
    def shortestPath(self, grid: List[List[int]]) -> int:
        self.visited = set()
        self.toVisit = queue.Queue()
        self.toVisit.put((0,0,0))
        self.visited.add((0,0))
        self.grid = grid
        pathLen = None
        while pathLen == None and not self.toVisit.empty():
            pathLen = self.checkNext()
        if pathLen == None: return -1
        else: return pathLen
                
        
    def checkNext(self) -> int | None:
        if self.toVisit.empty(): return None

        x, y, depth = self.toVisit.get()
        if not self.isValid(x, y):
            return None
        yLen = len(self.grid)
        xLen = len(self.grid[0])

        if x == xLen - 1 and y == yLen - 1:
            return depth
        
        if x > 0 and ((x - 1, y) not in self.visited):
            self.toVisit.put((x - 1, y, depth + 1))
            self.visited.add((x - 1, y))
        if x < (xLen - 1) and ((x + 1, y) not in self.visited):
            self.toVisit.put((x + 1, y, depth + 1))
            self.visited.add((x + 1, y))
        if y > 0 and ((x, y-1) not in self.visited):
            self.toVisit.put((x, y-1, depth + 1))
            self.visited.add((x, y - 1))
        if y < (yLen - 1) and ((x, y+1) not in self.visited):
            self.toVisit.put((x, y+1, depth + 1))
            self.visited.add((x, y + 1))
        return None


    def isValid(self, x: int, y: int) -> bool: 
        return self.grid[y][x] != 1