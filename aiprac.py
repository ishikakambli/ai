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


# =====================================================================
#**Text Classification with Scikit-Learn**
# =====================================================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
text = ["I love this", "This is good", "I hate this", "This is bad"]
label = ["Positive", "Positive", "Negative", "Negative"]

# Convert text into numbers
cv = CountVectorizer()
X = cv.fit_transform(text)

# Train the model
model = MultinomialNB()
model.fit(X, label)

# Test new text
test = ["I love good"]
test_data = cv.transform(test)

# Predict result
print("Classification:", model.predict(test_data)[0])
# =====================================================================
#Program to classify the email as SPAM and HAM (NOT SPAM)
# =====================================================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "Win money now",
    "Claim your free prize",
    "Hello how are you",
    "Let's meet tomorrow"
]

labels = ["Spam", "Spam", "Ham", "Ham"]

cv = CountVectorizer()
X = cv.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

test = ["Win free money"]
X_test = cv.transform(test)

print("Email is:", model.predict(X_test)[0])
# =====================================================================
#Program to classify the product review into positive and negative.
# =====================================================================

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

reviews = [
    "This product is good",
    "I love this product",
    "This product is bad",
    "I hate this product"
]

labels = ["Positive", "Positive", "Negative", "Negative"]

cv = CountVectorizer()
X = cv.fit_transform(reviews)

model = MultinomialNB()
model.fit(X, labels)

test = ["This product is good"]
X_test = cv.transform(test)

print("Review:", test[0])
print("Sentiment:", model.predict(X_test)[0])
# =====================================================================
#Working with Huggingface and Gemini LLMs 
# =====================================================================
#Hugging face for Text Generation
from transformers import pipeline

generator = pipeline("text-generation",model="gpt2")
prompt = "text generation is very useful because"
output = generator(prompt,max_new_tokens=20)
print(output[0]["generated_text"])

#Hugging face for Text summarization

from transformers import pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
articles = [
    "Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and human language. It enables tasks such as text classification, translation, summarization, and question answering. Modern NLP often uses transformer-based models.",

    "Mindfulness is a practice of being aware of the present moment. Research shows it helps reduce stress, improves concentration, and supports emotional regulation. Many schools and workplaces now include mindfulness exercises into daily routines."
]
summaries = summarizer(
    articles,
    max_new_tokens=50,
    min_length=15,
    do_sample=False
)
for article, summary in zip(articles, summaries):
    print("Original:", article)
    print("\nSummary:", summary['summary_text'], "\n")

#Huggingface for Sentiment Analysis

from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

texts = [
    "I love teaching Natural Language Processing!",
    "This assignment is terribly confusing.",
    "The workshop was very helpful and fun!",
    "I didn't like the food",
    "I loved the pizza"
]

for t in texts:
    result = sentiment(t)[0]
    print(f"Text: {t}\n -> Label: {result['label']}, Score: {result['score']:.4f}\n")
    
#Gemini for Text Generation(pip install google-generativeai)

import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

prompt = "Write a short poem about sunrise."
response = model.generate_content(prompt)

print("Gemini Response:")
print(response.text)
