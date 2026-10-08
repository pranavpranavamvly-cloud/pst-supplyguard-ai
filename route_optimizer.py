import heapq
from collections import defaultdict

def build_network(roads):
    """Build an undirected graph from {(node_a, node_b): {km, hours, open}}."""
    graph = defaultdict(list)
    for (a, b), details in roads.items():
        if not details.get("open", True):
            continue
        graph[a].append((b, float(details["hours"]), float(details["km"])))
        graph[b].append((a, float(details["hours"]), float(details["km"])))
    return graph

def shortest_path(graph, start, end, weight="hours"):
    """Dijkstra shortest path. Returns (path, travel_hours, distance_km)."""
    if start == end:
        return [start], 0.0, 0.0
    queue = [(0.0, start, [start], 0.0)]
    best = {start: 0.0}
    while queue:
        cost, node, path, distance = heapq.heappop(queue)
        if node == end:
            return path, cost, distance
        if cost > best.get(node, float("inf")):
            continue
        for neighbor, hours, km in graph.get(node, []):
            edge_cost = hours if weight == "hours" else km
            new_cost = cost + edge_cost
            if new_cost < best.get(neighbor, float("inf")):
                best[neighbor] = new_cost
                new_distance = distance + km
                heapq.heappush(queue, (new_cost, neighbor, path + [neighbor], new_distance))
    return [], None, None
