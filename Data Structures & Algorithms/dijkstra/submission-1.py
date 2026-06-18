import queue
from functools import total_ordering

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        @total_ordering
        class EdgeDistance:
            destination: int
            dist: int
            def __init__(self, u, v):
                self.destination = u
                self.dist = v
            def __lt__(self, other):
                return self.dist < other.dist
            def __eq__(self, other):
                return self.dist == other.dist        
            def __iter__(self):
                return iter((self.destination, self.dist))

        toVisit: queue.PriorityQueue[EdgeDistance] = queue.PriorityQueue()
        shortestByVertexId: Dict[int, int] = {}
        graph: Dict[int, Set[tuple[int, int]]] = {}
        for i in range(n):
            shortestByVertexId[i] = -1
            graph[i] = set()
        for edge in edges:
            source, destination, weight = edge
            graph[source].add((destination, weight))
        toVisit.put(EdgeDistance(src, 0))
        # for source, edgeSet in graph.items():
        #     print(edgeSet)

        while not toVisit.empty():
            edge = toVisit.get()
            destination, distance = edge
            # print("{u}, {v} - {w} left".format(u=destination, v=distance, w=toVisit.qsize()))
            currentShortest = shortestByVertexId[destination]
            if currentShortest == -1:
                shortestByVertexId[destination] = distance
            else:
                continue
            for nextDest, nextWeight in graph[destination]:
                toVisit.put(EdgeDistance(nextDest, distance + nextWeight))

        return shortestByVertexId
