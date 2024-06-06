import heapq
from collections import defaultdict
import time

def dijkstra(flights, start, end):
    graph = defaultdict(list)
    for flight in flights:
        graph[flight.start].append((flight.end, flight.distance))

    pq = []
    heapq.heappush(pq, (0, start, []))
    visited = set()

    start_time = time.time()  # Mulai pengukuran waktu
    while pq:
        total_distance, current, path = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if current == end:
            end_time = time.time()  # Akhiri pengukuran waktu
            return (total_distance, path), end_time - start_time

        for neighbor, distance in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (total_distance + distance, neighbor, path))

    end_time = time.time()  # Akhiri pengukuran waktu
    return (float('inf'), []), end_time - start_time



