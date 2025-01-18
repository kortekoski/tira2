import heapq

class TrainPrices:
    def __init__(self):
        self.graph = {}
        self.prices = {}

    def add_city(self, name):
        self.graph[name] = []
        self.prices[name] = []

    def add_train(self, city1, city2, price):
        self.graph[city1].append((city2, price))
        self.graph[city2].append((city1, price))
    

    def check_graph(self):
        return self.graph

    def find_prices(self):
        #katsotaan jokaisen kaupungin kohdalla etäisyydet muihin kaupunkeihin
        for city in sorted(list(self.graph.keys())):
            start_node = city
        
            #luodaan etäisyyksien sanakirja
            distances = {}
            #jokaisen etäisyydeksi asetetaan loputon
            for node in sorted(list(self.graph.keys())):
                distances[node] = float("inf")
            #aloitussolmun etäisyydeksi asetetaan 0
            distances[start_node] = 0
            
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
                        #kekoon pusketaan etäisyys solmuun b
                        new_pair = (new_distance, node_b)
                        heapq.heappush(queue, new_pair)

            #lopuksi distances-sanakirjassa on etäisyydet muihin kaupunkeihin katsotusta kaupungista
            self.prices[city] = distances

        #hinnat on pricesissä, muotoillaan kivemmaksi
        chart = [[] for _ in range(len(self.graph.keys())+1)]
        chart[0].append(None)
        kaupungit = sorted(list(self.graph.keys()))
        for city in kaupungit:
            chart[0].append(city)

        for i in range(1, len(self.graph.keys())+1):
            kaupunki = kaupungit[i-1]
            chart[i].append(kaupunki)
            hinnat = list(self.prices[kaupunki].items())
            print("hinnat:", hinnat)
            for hinta in hinnat:
                if hinta[1] == float("inf"):
                    chart[i].append(-1)
                else:
                    chart[i].append(hinta[1])

        return chart

if __name__ == "__main__":
    t = TrainPrices()

    t.add_city("Helsinki")
    t.add_city("Turku")
    t.add_city("Tampere")
    t.add_city("Oulu")

    #print(t.check_graph())

    t.add_train("Helsinki", "Tampere", 20)
    t.add_train("Helsinki", "Turku", 10)
    t.add_train("Tampere", "Turku", 50)
    #print(t.check_graph())

    print(t.find_prices())

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]