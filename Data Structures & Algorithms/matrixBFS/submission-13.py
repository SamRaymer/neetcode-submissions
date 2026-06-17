import collections
class Solution:
    
    def shortestPath(self, grid: List[List[int]]) -> int:
        yLen = len(grid)
        xLen = len(grid[0])
        def isValid(x: int, y: int) -> bool: 
            return grid[y][x] != 1

        toVisit: collections.deque[tuple[int, int, int]] = collections.deque() # x, y, depth
        visited: Set[tuple[int, int]] = set()
        if not isValid(0,0): return -1
        toVisit.append((0,0,0))
        visited.add((0,0))
        pathLen = None

        while pathLen == None and len(toVisit) > 0:
            x, y, depth = toVisit.popleft()

            if x == xLen - 1 and y == yLen - 1:
                return depth
            
            if x > 0 and ((x - 1, y) not in visited) and isValid(x-1, y):
                toVisit.append((x - 1, y, depth + 1))
                visited.add((x - 1, y))
            if x < (xLen - 1) and ((x + 1, y) not in visited) and isValid(x+1, y):
                toVisit.append((x + 1, y, depth + 1))
                visited.add((x + 1, y))
            if y > 0 and ((x, y-1) not in visited) and isValid(x, y-1):
                toVisit.append((x, y-1, depth + 1))
                visited.add((x, y - 1))
            if y < (yLen - 1) and ((x, y+1) not in visited) and isValid(x, y+1):
                toVisit.append((x, y+1, depth + 1))
                visited.add((x, y + 1))
        if pathLen == None: return -1
        else: return pathLen
                
        
    def checkNext(self) -> int | None:

        return None
