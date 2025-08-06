class Solution:
    def addNode(self, head, p, x):
        new_node = Node(x)

        current = head
        for _ in range(p):
            if current is not None:
                current = current.next

        if current is not None:
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node

        return head
