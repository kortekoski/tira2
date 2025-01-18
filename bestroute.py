import heapq

class BestRoute:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in range(1, n + 1)}
        
    def add_road(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))
        self.graph[node_b].append((node_a, weight))
        
    def find_route(self, start_node, end_node):
        #luodaan etäisyyksien sanakirja
        distances = {}
        #jokaisen etäisyydeksi asetetaan loputon
        for node in self.nodes:
            distances[node] = float("inf")
        #aloitussolmun etäisyydeksi asetetaan 0
        distances[start_node] = 0
        #luodaan edellisten solmujen sanakirja
        previous = {}
        #aloitussolmulla ei ole edellistä solmua, joten tämä on None
        previous[start_node] = None
        
        #luodaan keko solmujen etäisyyksille
        queue = []
        #kekoon lisätään aloitussolmu (etäisyys 0, tunnus start_node)
        heapq.heappush(queue, (0, start_node))
        
        #luodaan katsotuille solmuille setti
        visited = set()
        #aloitetaan luuppi, joka kestää niin kauan kuin jonossa on sisältöä
        while queue:
            #solmu a on on solmu, jolla on keon pienin etäisyys
            node_a = heapq.heappop(queue)[1]
            #jos solmussa a on käyty, luuppi aloitetaan alusta
            if node_a in visited:
                continue
            #solmu lisätään käytyihin
            visited.add(node_a)

            #käydään läpi solmusta a alkavat kaaret (solmu, paino)
            for node_b, weight in self.graph[node_a]:
                #uusi etäisyys on etäisyys solmuun a + kaaren ab paino
                new_distance = distances[node_a] + weight
                #jos uusi etäisyys on pienempi kuin solmuun b tallennettu etäisyys
                if new_distance < distances[node_b]:
                    #uusi etäisyys asetetaan etäisyydeksi solmuun b
                    distances[node_b] = new_distance
                    previous[node_b] = node_a
                    #kekoon pusketaan etäisyys solmuun b
                    new_pair = (new_distance, node_b)
                    heapq.heappush(queue, new_pair)

        

        route = []
        node = end_node

        while node:
            route.append(node)
            if node not in previous:
                return -1
            node = previous[node]

        route.reverse()
        return distances[end_node]

if __name__ == "__main__":
    b = BestRoute(5)
    print(b.find_route(3,4))
    b.add_road(3,5,7)
    print(b.find_route(3,4))
    print(b.find_route(1,4))
    b.add_road(3,4,6)
    print(b.find_route(4,5))
    b.add_road(4,5,4)
    b.add_road(1,2,7)
    b.add_road(1,3,4)
    print(b.find_route(3,4))