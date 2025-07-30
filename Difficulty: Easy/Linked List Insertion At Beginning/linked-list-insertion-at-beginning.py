# Definition for singly-linked list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to insert a node at the beginning of the linked list
    def insertAtBegining(self, head, x):
        new_node = Node(x)    # Create a new node with the given value
        new_node.next = head  # Point the new node's next to the current head
        return new_node       # New node becomes the new head
