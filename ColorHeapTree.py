import heapq
from collections import deque

from BuildHeapTree import draw_tree, build_heap_tree


def dfs(root):
    nodes = []
    q = [root]
    while q:
        cur = q.pop()
        if cur is None:
            continue
        nodes.append(cur)
        q.append(cur.right)
        q.append(cur.left)
    color_incr = 0xFF // (len(nodes) + 12)
    color = color_incr * 12
    for ix in range(len(nodes)):
        color += color_incr
        nodes[ix].color = f"#00{color:02x}{color:02x}"
    return [n.val for n in nodes]


def bfs(root):
    nodes = []
    q = deque([root])
    while q:
        cur = q.popleft()
        if cur is None:
            continue
        nodes.append(cur)
        q.append(cur.left)
        q.append(cur.right)
    color_incr = 0xFF // (len(nodes) + 12)
    color = color_incr * 12
    for ix in range(len(nodes)):
        color += color_incr
        nodes[ix].color = f"#00{color:02x}{color:02x}"
    return [n.val for n in nodes]


if __name__ == "__main__":
    # Let's take a list and make a heap
    heap_array = [12, 1, 9, 5, 8, 4, 2, 5, 11, 7, 9, 5]
    heapq.heapify(heap_array)
    # Build a binary tree
    heap_tree_root = build_heap_tree(heap_array)
    dfs_order = dfs(heap_tree_root)
    print(f"Heap tree list: {heap_array}")
    # Draw the tree after DFS
    print(f"DFS order: {dfs_order}")
    draw_tree(heap_tree_root)

    bfs_order = bfs(heap_tree_root)
    # Draw the tree after BFS
    print(f"BFS order: {bfs_order}")
    draw_tree(heap_tree_root)
