from functools import total_ordering
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        toVisit: List[tuple[int, int]] = []
        shortestByVertexId: Dict[int, int] = {}
        graph: Dict[int, Set[tuple[int, int]]] = {}
        for i in range(n):
            shortestByVertexId[i] = -1
            graph[i] = set()
        for edge in edges:
            source, destination, weight = edge
            graph[source].add((destination, weight))
        heapq.heappush(toVisit, (0, src))
        # for source, edgeSet in graph.items():
        #     print(edgeSet)

        while len(toVisit) > 0:
            edge = heapq.heappop(toVisit)
            distance, destination = edge
            # print("{u}, {v} - {w} left".format(u=destination, v=distance, w=toVisit.qsize()))
            currentShortest = shortestByVertexId[destination]
            if currentShortest == -1:
                shortestByVertexId[destination] = distance
            else:
                continue
            for nextDest, nextWeight in graph[destination]:
                heapq.heappush(toVisit,(distance + nextWeight, nextDest))

        return shortestByVertexId
