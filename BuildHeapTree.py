import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = (
            color  # additional argument for storing the color of the node.
        )
        self.id = str(uuid.uuid4())  # unique identifier for each node


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
        node_size=2500,
        node_color=colors,
    )
    plt.show()


def build_heap_tree(heap, ix=0):
    if ix >= len(heap):
        return None
    node = Node(heap[ix])
    node.left = build_heap_tree(heap, 2 * ix + 1)
    node.right = build_heap_tree(heap, 2 * ix + 2)
    return node


if __name__ == "__main__":
    # Let's take a list and make a heap
    heap_array = [12, 1, 9, 5, 8, 4, 2, 5, 11, 7, 9, 5]
    heapq.heapify(heap_array)
    # Build a binary tree
    heap_tree_root = build_heap_tree(heap_array)
    # Draw the tree
    print(f"Heap tree list: {heap_array}")
    draw_tree(heap_tree_root)
