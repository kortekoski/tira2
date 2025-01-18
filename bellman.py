import time
import random
import heapq

class BellmanFord:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.edges = []
        
    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))
        
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        for _ in range(len(self.nodes) - 1):
            for edge in self.edges:
                node_a, node_b, weight = edge
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    
        return distances

class Dijkstra:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in range(1, n + 1)}
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        
    def find_distances(self, start_node):
        distances = {}
        for node in self.nodes:
            distances[node] = float("inf")
        distances[start_node] = 0
        
        queue = []
        heapq.heappush(queue, (0, start_node))
        
        visited = set()
        while queue:
            node_a = heapq.heappop(queue)[1]
            if node_a in visited:
                continue
            visited.add(node_a)

            for node_b, weight in self.graph[node_a]:
                new_distance = distances[node_a] + weight
                if new_distance < distances[node_b]:
                    distances[node_b] = new_distance
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)
                    
        return distances

if __name__=="__main__":
    d = Dijkstra(5000)

    kaaret = []

    for a in range(1, 5001):
        for b in range(a+1, 5001):
            if b - a < 10:
                kaaret.append((a, b))
    
    random.shuffle(kaaret)

    for kaari in kaaret:
        d.add_edge(kaari[0], kaari[1], random.randint(1, 1000))

    aloitusaika1 = time.time()
    print(d.find_distances(1))
    suoritusaika1 = time.time() - aloitusaika1
    print("aika:", suoritusaika1)

    #aloitusaika2 = time.time()
    #random_heap(lista2)
    #suoritusaika2 = time.time() - aloitusaika2
    #print("aika:", suoritusaika2)