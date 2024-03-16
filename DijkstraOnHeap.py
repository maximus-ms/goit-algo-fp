import heapq
import networkx as nx
import pandas as pd
from UkraineRoads import UkraineRoads


class MinPriorityQueue:
    def __init__(self, items: list = None):
        self.q = []
        if not items is None:
            try:
                q = list(items)
                heapq.heapify(q)
            except Exception:
                print(
                    f"Input type {type(items)} cannot be converted to list. MinPriorityQueue is created with empty queue!"
                )
            else:
                self.q = q

    def push(self, priority_data):
        heapq.heappush(self.q, priority_data)

    def pop(self):
        item = heapq.heappop(self.q)
        if isinstance(item, (list, set)):
            item = item[1]
        return item

    def update(self):
        heapq.heapify(self.q)

    def __bool__(self):
        return bool(self.q)

    def __str__(self) -> str:
        return str(self.q)


def dijkstra_on_heap(graph, start):
    """
    Dijkstra's algorithm
    to find the shortest paths in a weighted graph using a binary heap
    Input:
        graph: the graph to work with
        start: the vertex to start from
    Return:
        dictionary: minimal distances from the 'start' vertex to each vertex in the graph
    """
    distances = {vertex: [float("infinity"), vertex] for vertex in graph}
    distances[start][0] = 0
    unvisited = MinPriorityQueue(distances.values())

    while unvisited:
        unvisited.update()
        cur_vertex = unvisited.pop()
        if distances[cur_vertex][0] == float("infinity"):
            break
        for neighbor, attr in graph[cur_vertex].items():
            distance = distances[cur_vertex][0] + attr["weight"]
            if distance < distances[neighbor][0]:
                distances[neighbor][0] = distance
    return {vertex: item[0] for vertex, item in distances.items()}


def find_all_distances(graph):
    """
    Function to find all minimal distances between all nodes in the given graph using dijkstra_on_heap()
    Input:
        graph: the graph to work with
    Return:
        dictionary: minimal distances from each vertex to each vertex in the graph
    """
    if not isinstance(graph, nx.Graph):
        raise Exception(
            f"Expected an object of networkx class, provided {type(graph)}"
        )

    # Get order of nodes based on Centrality coefficient
    centrality = nx.degree_centrality(graph)
    node_q = [(-v, node) for node, v in centrality.items()]
    pq = MinPriorityQueue(node_q)
    distances = {}
    while pq:
        start = pq.pop()
        distances[start] = dijkstra_on_heap(graph, start)
    return distances


if __name__ == "__main__":
    # Let's take UkraineRoads from HW6 as a test graph
    U = UkraineRoads()
    # Calculate distances by dijkstra_on_heap()
    distances = find_all_distances(U.g)
    # Calculate distances by method dijkstra from UkraineRoads
    u_distances = U.get_distance_map()
    # Let's check if all calculated distances are same
    cnt = 0
    for city in distances.keys():
        D1 = distances[city]
        D2 = u_distances[city]
        for c in D1.keys():
            if D1[c] != D2[c]:
                print(f"{c:<16} {D1[c]:>3} != {D2[c]:<3}")
                cnt += 1

    if cnt == 0:
        print("All distances a correct")
    # Let's print distances from Kyiv
    print(pd.DataFrame(distances)["Київ"])
