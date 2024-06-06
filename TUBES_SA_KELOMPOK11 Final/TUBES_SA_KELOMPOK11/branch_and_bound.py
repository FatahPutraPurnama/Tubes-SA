import time
from collections import defaultdict

def branch_and_bound(flights, start, end):
    def dfs(city, distance, path, best, visited):
        if city == end:
            if distance < best[0]:
                best[0] = distance
                best[1] = path[:]
            return

        for neighbor, dist in graph.get(city, []):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                dfs(neighbor, distance + dist, path, best, visited)
                path.pop()
                visited.remove(neighbor)

    graph = defaultdict(list)
    for flight in flights:
        graph[flight.start].append((flight.end, flight.distance))

    best = [float('inf'), []]
    visited = set([start])
    start_time = time.time()  # Mulai pengukuran waktu
    dfs(start, 0, [start], best, visited)
    end_time = time.time()  # Akhiri pengukuran waktu
    return best, end_time - start_time
