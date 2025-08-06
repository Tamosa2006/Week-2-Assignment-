class Solution:    
    def pairWiseSwap(self, head):
        if head is None or head.next is None:
            return head

        prev = None
        current = head
        head = current.next

        while current and current.next:
            next_node = current.next
            next_pair = next_node.next

            next_node.next = current
            current.next = next_pair

            if prev:
                prev.next = next_node

            prev = current
            current = next_pair

        return head
