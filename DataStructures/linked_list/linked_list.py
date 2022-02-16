class Node:
    """Definition of node structure of linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

    def __str__(self):
        return self.data


class LinkedList:
    """Definition of linked list data structure"""
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = node

    def add_after(self, target_data, new_node):
        if self.head is None:
            raise Exception("Empty list")

        node = self.head
        while node:
            if node.data == target_data:
                new_node.next = node.next
                node.next = new_node
                return

            node = node.next
        raise Exception(f"Could not find node with data {target_data}")

    def add_before(self, target_data, new_node):
        if self.head is None:
            raise Exception("Empty list")

        if self.head.data == target_data:
            self.add_first(new_node)
            return

        prev_node = self.head
        curr_node = self.head.next
        while curr_node:
            if curr_node.data == target_data:
                new_node.next = curr_node
                prev_node.next = new_node
                return
            prev_node = curr_node
            curr_node = curr_node.next
        raise Exception(f"Could not find node with data {target_data}")

    def remove(self, target_data):
        if self.head is None:
            raise Exception("Empty list")

        if self.head.data == target_data:
            self.head = self.head.next
            return

        prev_node = self.head
        node = prev_node.next
        while node:
            if node.data == target_data:
                prev_node.next = node.next
                return
            prev_node = node
            node = node.next
        raise Exception(f"Could not find node with data {target_data}")

    def __repr__(self):
        node = self.head
        data = []
        while node:
            data.append(node.data)
            node = node.next
        return "->".join(data)

    def __str__(self):
        node = self.head
        data = []
        while node:
            data.append(node.data)
            node = node.next
        data.append('None')
        return "->".join(data)


if __name__ == "__main__":
    llist = LinkedList()
    print(llist)

    first_node = Node('a')
    second_node = Node('b')
    third_node = Node('c')

    llist.add_first(first_node)
    llist.add_last(second_node)
    llist.add_last(third_node)
    print(llist)



