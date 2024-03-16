class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = LinkedList.Node(data)
        new_node.next, self.head = self.head, new_node

    def insert_at_end(self, data):
        new_node = LinkedList.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_from(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
        return self

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Previous node doesn't exist")
            return
        new_node = LinkedList.Node(data)
        prev_node.next, new_node.next = new_node, prev_node.next

    def delete_node(self, data: int):
        cur = self.head
        if cur and cur.data == data:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != data:
            prev, cur = cur, cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_node(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse_inplace(self):
        if self.head is None:
            return
        new_ll = self.head
        old_ll = new_ll.next
        new_ll.next = None

        while old_ll:
            cur = old_ll
            old_ll = old_ll.next
            cur.next = new_ll
            new_ll = cur
        self.head = new_ll
        return

    def reverse(self, inplace=False):
        if inplace:
            self.reverse_inplace()
            return self

        ll_new = LinkedList()
        cur = self.head
        while cur:
            ll_new.insert_at_beginning(cur.data)
            cur = cur.next
        return ll_new

    def sort(self):
        if self.head is None:
            return self
        tmp_ll = self.head.next
        self.head.next = None
        while tmp_ll:
            node = tmp_ll
            tmp_ll = tmp_ll.next
            if self.head.data >= node.data:
                node.next, self.head = self.head, node
            else:
                prev = self.head
                cur = self.head.next
                while cur and (cur.data < node.data):
                    prev, cur = cur, cur.next
                prev.next, node.next = node, cur
        return self

    def merge_sorted(self, other_sorted_ll):
        if (
            not isinstance(other_sorted_ll, LinkedList)
            or other_sorted_ll.head is None
        ):
            return self
        if self.head is None:
            self.head = other_sorted_ll.head
            return self

        cur1 = self.head
        cur2 = other_sorted_ll.head
        while cur2 and (self.head.data > cur2.data):
            t = self.head
            self.head = cur2
            cur2 = cur2.next
            self.head.next = t
        prev = self.head
        cur1 = self.head.next
        while cur1 and cur2:
            if cur1.data > cur2.data:
                t = cur2
                cur2 = cur2.next
                t.next = cur1
                prev.next = t
            else:
                cur1 = cur1.next
            prev = prev.next
        if cur2:
            prev.next = cur2
        return self

    def __str__(self):
        l = list()
        current = self.head
        while current:
            l.append(current.data)
            current = current.next
        return str(l)


if __name__ == "__main__":
    llist = LinkedList()

    # llist.insert_at_beginning(5)
    # llist.insert_at_beginning(10)
    # llist.insert_at_beginning(10)
    # llist.insert_at_beginning(15)
    # llist.insert_at_end(20)
    # llist.insert_at_end(25)
    # llist.insert_at_end(10)

    # print(f"Current LL:            {llist}")

    # llist.delete_node(10)

    # print(f"LL after delete [10]:  {llist}")

    # node = llist.search_node(15)
    # print(f"Search node [15]: {node.data if node else None}")

    # print(f"Reversed LL (new LL):  {llist.reverse()}")
    # print(f"Reversed LL (inplace): {llist.reverse(inplace=True)}")
    # print(f"Reversed LL (inplace): {llist.reverse(inplace=True)}")
    # print(f"Sorted LL (inplace):   {llist.sort()}")

    print(LinkedList().sort())
    print(LinkedList().insert_from([2]).sort())
    print(LinkedList().insert_from([1, 2]).sort())
    print(LinkedList().insert_from([0, 1, 2]).sort())
    print(LinkedList().insert_from([0, 2, 1]).sort())
    print(LinkedList().insert_from([2, 1, 0]).sort())
    print(LinkedList().insert_from([2, 0, 1]).sort())

    print(LinkedList().merge_sorted(LinkedList()))
    print(LinkedList().merge_sorted(2))
    print(
        LinkedList().merge_sorted(LinkedList().insert_from([5, 3, 1]).sort())
    )
    print(
        LinkedList()
        .insert_from([2, 0, 1])
        .sort()
        .merge_sorted(LinkedList().insert_from([5, 3, 1]).sort())
    )
