import uuid
import networkx as nx
import matplotlib.pyplot as plt
from numpy import random

from DijkstraOnHeap import MinPriorityQueue

class HeapTree(MinPriorityQueue):
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
                raise Exception(f"Node '{self.val}' already has left and right child")

    def __init__(self, items: list = None) -> None:
        super().__init__(items)
        self._reset_tree()

    def _reset_tree(self):
        self.root = None
        self.graph = None
        self.pos = None

    def _add_edges(self, node, x=0, y=0, layer=1):
        if node is not None:
            self.graph.add_node(
                node.id, color=node.color, label=node.val
            )  # using an ID and storing the node value
            if node.left:
                self.graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2**layer
                self.pos[node.left.id] = (l, y - 1)
                self._add_edges(node.left, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                self.graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2**layer
                self.pos[node.right.id] = (r, y - 1)
                self._add_edges(node.right, x=r, y=y - 1, layer=layer + 1)

    def _build_graph(self):
        self.graph = nx.DiGraph()
        self.pos = {self.root.id: (0, 0)}
        self._add_edges(self.root)

    def build_tree(self):
        heap_l = len(self.q)

        def tree_add_node(root, curr_ix):
            child_ix = 2 * curr_ix + 1
            for _ in range(2):
                if child_ix < heap_l:
                    node = HeapTree.Node(self.q[child_ix])
                    root.add_child(node)
                    tree_add_node(node, child_ix)
                    child_ix += 1

        if heap_l == 0:
            print("Heap is empty and cannot be drawn")
            return
        self.root = HeapTree.Node(self.q[0])
        tree_add_node(self.root, 0)

        self._build_graph()

    def show(self):
        if not self.graph:
            self.build_tree()
        colors = [node[1]["color"] for node in self.graph.nodes(data=True)]
        labels = {
            node[0]: node[1]["label"] for node in self.graph.nodes(data=True)
        }  # use the node value for labels

        plt.figure(figsize=(8, 5))
        nx.draw(
            self.graph,
            pos=self.pos,
            labels=labels,
            arrows=False,
            node_size=800,
            node_color=colors,
        )
        plt.show()

    def push(self, priority_data):
        self._reset_tree()
        super().push(priority_data)

    def pop(self):
        self._reset_tree()
        return super().pop()

    def update(self):
        self._reset_tree()
        return super().update()


if __name__ == "__main__":
    data = list(random.randint(50, size=26))
    ht = HeapTree(data)
    print(ht)
    ht.show()
    print(f"Pop: {ht.pop()}")
    print(ht)
    ht.show()
    print("Push '45' to the heap tree")
    ht.push(45)
    print(ht)
    ht.show()
