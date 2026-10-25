graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

for node in graph:
    print(node, "->", graph[node])

#UCS practical

import heapq

graph = {
    'arad': {'sibiu': 140, 'zerind': 75, 'timisoara': 118},
    'zerind': {'arad': 75, 'oradea': 71},
    'oradea': {'zerind': 71, 'sibiu': 151},
    'sibiu': {'arad': 140, 'oradea': 151, 'fagaras': 99, 'rimnicu vilcea': 80},
    'fagaras': {'sibiu': 99, 'bucharest': 211},
    'rimnicu vilcea': {'sibiu': 80, 'craiova': 146, 'pitesti': 97},
    'pitesti': {'rimnicu vilcea': 97, 'craiova': 138, 'bucharest': 101},
    'bucharest': {'fagaras': 211, 'pitesti': 101}
}

def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, city, path = heapq.heappop(pq)

        if city == goal:
            print("Path:", path)
            print("Cost:", cost)
            return

        if city not in visited:
            visited.add(city)

            for next_city, distance in graph[city].items():
                if next_city not in visited:
                    heapq.heappush(
                        pq,
                        (cost + distance, next_city,
                         path + [next_city])
                    )

    print("No path found")

start = input("Enter source: ").lower()
goal = input("Enter goal: ").lower()

if start in graph and goal in graph:
    ucs(start, goal)
else:
    print("City does not exist")
