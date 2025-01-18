import heapq

class BestRoute:
    def __init__(self, nodegrid):
        self.nodes = []
        self.xmax = len(nodegrid[0])
        self.ymax = len(nodegrid)

        j = 1
        for row in nodegrid:
            i = 1
            for number in row:
                self.nodes.append((i, j, number))
                i += 1
            j += 1

        self.graph = {node: [] for node in self.nodes}

        for i in range(0, len(self.nodes)):
            #yli rajojen: 
            # jos x > 1, luodaan kaari vasemmalle
            if self.nodes[i][0] > 1:
                self.add_edge(self.nodes[i], self.nodes[i-1], self.nodes[i-1][2])
            # jos x < xmax, luodaan kaari oikealle
            if self.nodes[i][0] < self.xmax:
                self.add_edge(self.nodes[i], self.nodes[i+1], self.nodes[i+1][2])
            # jos y > 1, luodaan kaari ylös
            if self.nodes[i][1] > 1:
                self.add_edge(self.nodes[i], self.nodes[i-self.xmax], self.nodes[i-self.xmax][2])
            # jos y < ymax, luodaan kaari alas
            if self.nodes[i][1] < self.ymax:
                self.add_edge(self.nodes[i], self.nodes[i+self.xmax], self.nodes[i+self.xmax][2])
        
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
            #avaimen arvona on tuple: ensin tuple, jossa on (x, y, numero) ja sitten kaaren paino
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
        result = 0

        while node:
            if node[2] == 10:
                result += 1
            node = previous[node]


        if distances[end_node] == float("inf"):
            return -1
        return result

def gridify(l):
    labyrinth = l[1:-1]
    new = []

    for row in labyrinth:
        brow = row[1:-1]
        new.append(brow)

    print(new)
    grid = []

    start_node = 0
    end_node = 1

    index = 0
    j = 1
    for row in new:
        grid.append([])
        i = 1
        for character in row:
            if character == '.':
                grid[index].append(1)
            elif character == '*':
                grid[index].append(10)
            elif character == 'A':
                start_node = (i, j)
                grid[index].append(1)
            elif character == 'B':
                end_node = (i, j)
                grid[index].append(1)
            i += 1
        j += 1
        index += 1
    
    return (grid, start_node, end_node)


def count(r):
    gridstartend = gridify(r)
    grid = gridstartend[0]
    pointgraph = BestRoute(grid)
    start = (gridstartend[1][0], gridstartend[1][1], 1)
    end = (gridstartend[2][0], gridstartend[2][1], 1)
    distance = pointgraph.find_route(start, end)
    return distance

if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    
    print(count(r)) # 2