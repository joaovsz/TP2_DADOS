import heapq

class PrimAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def minimum_spanning_tree(self, start):
        mst = []
        visited = set()
        priority_queue = [(0, start, None)]
        total_cost = 0

        while priority_queue:
            weight, node, previous = heapq.heappop(priority_queue)

            if node in visited:
                continue
            visited.add(node)

            if previous is not None:
                mst.append((previous, node, weight))
                total_cost += weight

            for neighbor, cost in self.graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (cost, neighbor, node))

        return mst, total_cost
