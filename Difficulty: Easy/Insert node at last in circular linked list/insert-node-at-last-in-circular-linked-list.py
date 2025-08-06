class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    new_node = Node(data)
    
    if not head:
        new_node.next = new_node
        return new_node

    temp = head
    while temp.next != head:
        temp = temp.next

    temp.next = new_node
    new_node.next = head

    return head
