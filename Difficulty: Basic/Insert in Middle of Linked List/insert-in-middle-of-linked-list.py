# Node Class
class Node:
    def __init__(self, data):  
        self.data = data
        self.next = None


class Solution:
    def insertInMiddle(self, head, x):
        # Create new node
        new_node = Node(x)

        # If the list is empty, the new node becomes the head
        if head is None:
            head = new_node
            return head

        # Use slow and fast pointer to find the middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Insert new_node after slow (middle node)
        new_node.next = slow.next
        slow.next = new_node

        return head
