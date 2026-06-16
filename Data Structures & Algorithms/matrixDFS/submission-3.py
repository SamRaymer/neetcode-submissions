class Solution:
    # We'll use tuples of (x,y) throughout this.
    def countPaths(self, grid: List[List[int]]) -> int:
        return len(self.listTraversals(grid, [(0,0)], set(), 0, 0))
    
    def listTraversals(
        self,
        grid: List[List[int]],
        path: List[tuple[int, int]],
        visited: Set[tuple[int, int]],
        x: int, y: int
    ) -> List[List[tuple[int, int]]]:
        if not isValidMove(grid, x, y):
            return []
        if (x, y) in visited:
            return []
        visited = visited.copy()
        visited.add((x,y))
        # Using depth-first method
        yLen = len(grid)
        xLen = len(grid[0])
        
        if x == xLen - 1 and y == yLen - 1:
            return [path]
        
        paths = []
        newX = x - 1
        if x > 0:
            newTuple = (newX, y)
            newPath = path.copy()
            newPath.append(newTuple)
            paths = paths + self.listTraversals(grid, newPath, visited, newX, y)
        newX = x + 1
        if newX < xLen:
            newTuple = (newX, y)
            newPath = path.copy()
            newPath.append(newTuple)
            paths = paths + self.listTraversals(grid, newPath, visited, newX, y)
        newX = None # for type safety
        newY = y + 1
        if newY < yLen:
            newTuple = (x, newY)
            newPath = path.copy()
            newPath.append(newTuple)
            paths = paths + self.listTraversals(grid, newPath, visited, x, newY)
        newY = y - 1
        if newY >= 0:
            newTuple = (x, newY)
            newPath = path.copy()
            newPath.append(newTuple)
            paths = paths + self.listTraversals(grid, newPath, visited, x, newY)

        return paths
    
def isValidMove(grid: List[List[int]], x: int, y: int) -> bool:
    try:
        return grid[y][x] == 0
    except IndexError:
        print("cant access {x}, {y}".format(x=x, y=y))
        raise