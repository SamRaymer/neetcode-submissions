class Solution:
    # We'll use tuples of (x,y) throughout this.
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.countTraversals(grid, {(0,0)}, 0, 0)
    
    def countTraversals(
        self,
        grid: List[List[int]],
        visited: Set[tuple[int, int]],
        x: int, y: int
    ) -> int:
        if not isValidMove(grid, x, y):
            return 0
        # Using depth-first method
        yLen = len(grid)
        xLen = len(grid[0])
        
        if x == xLen - 1 and y == yLen - 1:
            return 1
        
        paths = 0
        newX = x - 1
        if x > 0:
            newTuple = (newX, y)
            if newTuple not in visited:
                visited.add(newTuple)
                paths = paths + self.countTraversals(grid, visited, newX, y)
                visited.remove(newTuple)
        newX = x + 1
        if newX < xLen:
            newTuple = (newX, y)
            if newTuple not in visited:
                visited.add(newTuple)
                paths = paths + self.countTraversals(grid, visited, newX, y)
                visited.remove(newTuple)
        newX = None # for type safety
        newY = y + 1
        if newY < yLen:
            newTuple = (x, newY)
            if newTuple not in visited:
                visited.add(newTuple)
                paths = paths + self.countTraversals(grid, visited, x, newY)
                visited.remove(newTuple)
        newY = y - 1
        if newY >= 0:
            newTuple = (x, newY)
            if newTuple not in visited:
                visited.add(newTuple)
                paths = paths + self.countTraversals(grid, visited, x, newY)
                visited.remove(newTuple)

        return paths
    
def isValidMove(grid: List[List[int]], x: int, y: int) -> bool:
    try:
        return grid[y][x] == 0
    except IndexError:
        print("cant access {x}, {y}".format(x=x, y=y))
        raise