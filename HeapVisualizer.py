import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from numpy import random


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = (
            color  # additional argument for storing the color of the node.
        )
        self.id = str(uuid.uuid4())  # unique identifier for each node

    def add_child(self, node):
        if self.left is None:
            self.left = node
        elif self.right is None:
            self.right = node
        else:
            raise Exception("Left and right are already set")


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # using an ID and storing the node value
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(
                graph, node.right, pos, x=r, y=y - 1, layer=layer + 1
            )
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # use the node value for labels

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=800,
        node_color=colors,
    )
    plt.show()


def draw_heap(heap):
    heap_l = len(heap)

    def tree_add_node(root, curr_ix):
        child_ix = 2 * curr_ix + 1
        for _ in range(2):
            if child_ix < heap_l:
                node = Node(heap[child_ix])
                root.add_child(node)
                tree_add_node(node, child_ix)
                child_ix += 1

    if heap_l == 0:
        print("Heap is empty and cannot be drawn")
        return
    root = Node(heap[0])
    tree_add_node(root, 0)
    draw_tree(root)


if __name__ == "__main__":
    data = list(random.randint(50, size=26))
    heapq.heapify(data)
    print(data)
    draw_heap(data)
