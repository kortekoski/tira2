import heapq

class BestRoute:
    def __init__(self, nodelist):
        self.nodes = range(1, len(nodelist) + 1)
        self.graph = {node: [] for node in range(1, len(nodelist)+ 1)}

        for node in self.nodes:
            #viitataan listan indeksiin, josta saadaan paino kaarille
            weight = nodelist[node-1]

            #jos node - paino >= 0, luodaan kaari "vasemmalle"
            if node - weight > 0:
                self.add_edge(node, node-weight, weight)
            
            #luodaan kaari oikealle, jos node + paino < suurin node
            if node + weight <= self.nodes[-1]:
                self.add_edge(node, node+weight, weight)
        
    def add_edge(self, node_a, node_b, weight):
        self.graph[node_a].append((node_b, weight))

    def start_end(self):
        return (self.nodes[0], self.nodes[-1])
        
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

        

        if distances[end_node] == float("inf"):
            return -1
        return distances[end_node]

def calculate(t):
    pointgraph = BestRoute(t)
    startend = pointgraph.start_end()
    distance = pointgraph.find_route(startend[0], startend[1])
    return distance

if __name__ == "__main__":
    print(calculate([1, 1, 1, 1])) # 3
    print(calculate([3, 2, 1])) # -1
    print(calculate([3, 5, 2, 2, 2, 3, 5])) # 10
    print(calculate([7, 5, 3, 1, 4, 2, 4, 6, 1])) # 32