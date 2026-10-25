# =====================================================================
#DFS
# =====================================================================
graph = {
    1: [2], 2: [1, 3, 6, 8], 3: [2, 4, 6, 7], 4: [3, 6],
    5: [6], 6: [2, 3, 4, 5], 7: [3], 8: [2]
}

def dfs(node, visited=[]):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)
    return visited

print("Graph Representation:\n")
for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")

print("\nDFS VISITED LIST (Starting from 1):\n")
print(dfs(1))

# =====================================================================
#BFS
# =====================================================================

graph = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'],
    'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']
}

def bfs(start):
    visited, queue = {start}, [start]
    print("BFS Traversal Order:")
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                queue.append(n)

bfs('A')



# =====================================================================
#UCS uniform cost search algorithm
# =====================================================================

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

# =====================================================================
#A* algorithm
# =====================================================================

from queue import PriorityQueue

graph = {
    'Arad': {'Sibiu': 140, 'Zerind': 75},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Pitesti': 97},
    'Zerind': {'Arad': 75},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Sibiu': 97, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

h = {
    'Arad': 366, 'Sibiu': 253, 'Zerind': 374,
    'Fagaras': 176, 'Pitesti': 100, 'Bucharest': 0
}

def astar(start, goal):
    pq = PriorityQueue()
    pq.put((h[start], 0, start, [start]))
    visited = set()

    while not pq.empty():
        f, cost, city, path = pq.get()

        if city == goal:
            print("Path:", path)
            print("Cost:", cost)
            return

        if city not in visited:
            visited.add(city)

            for next_city, distance in graph[city].items():
                if next_city not in visited:
                    g = cost + distance
                    f = g + h[next_city]
                    pq.put((f, g, next_city, path + [next_city]))

    print("No path found")

start = input("Enter source: ").title()
goal = input("Enter goal: ").title()

if start in graph and goal in graph:
    astar(start, goal)
else:
    print("City does not exist")
# =====================================================================
#QUEEN
# =====================================================================

def solve_n_queens(n, col=0, board=[]):
    if col == n:
        return [board]
    return [
        sol for row in range(n)
        if all(r != row and abs(r - row) != col - c for c, r in enumerate(board))
        for sol in solve_n_queens(n, col + 1, board + [row])
    ]

n = int(input("Enter board size (e.g., 4 or 8): "))
results = solve_n_queens(n)
print(f"\nFound {len(results)} solutions!\n")

for i, board in enumerate(results, 1):
    print(f"--- Solution #{i} ---")
    for r in board:
        print(". " * r + "Q " + ". " * (n - r - 1))
    print()

# =====================================================================
#NLTK text processing and preprocessing
# =====================================================================
#tokenization

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "I am learning Python programming"

print(word_tokenize(text))
#stemming

from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "plays", "running"]

for word in words:
    print(ps.stem(word))
#Lemmatization

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

lm = WordNetLemmatizer()

words = ["cars", "playing", "mice", "running"]

for word in words:
    print(lm.lemmatize(word))
