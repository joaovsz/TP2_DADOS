import heapq

class DijkstraModifiedAlgorithm:
    def __init__(self, graph=None, charging_stations=None, flight_graph=None, mandatory_stops=None, max_connection_time=None):
        self.graph = graph
        self.charging_stations = charging_stations or []
        self.flight_graph = flight_graph
        self.mandatory_stops = mandatory_stops or {}
        self.max_connection_time = max_connection_time

    def find_cheapest_routes(self, start, destination):
        if not self.flight_graph:
            raise ValueError("Nenhum grafo de voos foi definido.")

        priority_queue = [(0, start, [])]
        visited = {}
        valid_routes = []

        while priority_queue:
            total_cost, current_airport, path = heapq.heappop(priority_queue)

            if current_airport in visited and visited[current_airport] <= total_cost:
                continue
            visited[current_airport] = total_cost

            path = path + [current_airport]

            if current_airport == destination:
                valid_routes.append((path, total_cost))
                continue  

            for neighbor, (flight_cost, connection_time) in self.flight_graph[current_airport].items():
                if connection_time <= self.max_connection_time:
                    extra_cost = self.mandatory_stops.get((current_airport, neighbor), 0)
                    heapq.heappush(priority_queue, (total_cost + flight_cost + extra_cost, neighbor, path))

        return valid_routes if valid_routes else None

    def find_best_routes(self, start, destination, max_autonomy):
        if not self.graph:
            raise ValueError("Nenhum grafo de rotas foi definido.")

        priority_queue = [(0, start, max_autonomy, [])]
        visited = {}
        valid_routes = []

        while priority_queue:
            time_spent, current_node, remaining_range, path = heapq.heappop(priority_queue)

            if current_node in visited and visited[current_node] >= remaining_range:
                continue
            visited[current_node] = remaining_range

            path = path + [current_node]

            if current_node == destination:
                valid_routes.append((path, time_spent))
                continue  

            for neighbor, travel_time in self.graph[current_node].items():
                if travel_time > remaining_range:
                    for station in self.charging_stations:
                        if station != current_node:
                            heapq.heappush(priority_queue, (time_spent + travel_time, station, max_autonomy, path + [station]))
                else:
                    heapq.heappush(priority_queue, (time_spent + travel_time, neighbor, remaining_range - travel_time, path))

        return valid_routes if valid_routes else None
