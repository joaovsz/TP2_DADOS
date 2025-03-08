import heapq

class DijkstraAlgorithm:
    def __init__(self, graph):
        self.graph = graph
    
    def find_shortest_path(self, start, end=None):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        previous_nodes = {}
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_node == end:
                break
            
            for neighbor, weight in self.graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        if end is not None:
            return self._reconstruct_path(previous_nodes, start, end), distances[end]
        return distances
    
    def _reconstruct_path(self, previous_nodes, start, end):
        path = []
        current = end
        while current in previous_nodes:
            path.insert(0, current)
            current = previous_nodes[current]
        if path:
            path.insert(0, start)
        return path
