#Jack Keane
#Professor Zhang
#CST571_01 Computer Algorithms and Analysis
#Programming Project 1 Djiktra's Algorithm: This program will find the shortest distance and the shortest path
#21 April 2023

graph = {
    'A' : {'B' : 3, 'C': 2},
    'B' : {'A' : 3, 'C': 1, 'D': 4},
    'C' : {'A': 2, 'B': 1, 'D': 6, 'E': 5},
    'D' : {'B': 4, 'C': 6},
    'E' : {'C': 5}
}

def dijkstra(graph, start, end):
    dist = {n: float('inf') for n in graph}
    dist[start] = 0
    visit = set()

    while end not in visit:
        n_current = None
        dist_current = float('inf')
        for n in graph:
            if n not in visit and dist[n] < dist_current:
                n_current = n
                dist_current = dist[n]

        if n_current is None:
            return (float('inf'), [])

        visit.add(n_current)

        for neighbor, weight in graph[n_current].items():
            distance = dist_current + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance

    #Constructing the shortest path
    path = [end]
    while path[-1] != start:
        n = path[-1]
        for neighbor, weight in graph[n].items():
            if dist[neighbor] + weight == dist[n]:
                path.append(neighbor)
                break
    path.reverse()
    return (dist[end], path)

#The Output
start = 'A'
end = 'E'

distance, path = dijkstra(graph, start, end)
print(f"The shortest distance of {start} and {end} is {distance}")
print(f"The shortest path is {', '.join(path)}")
