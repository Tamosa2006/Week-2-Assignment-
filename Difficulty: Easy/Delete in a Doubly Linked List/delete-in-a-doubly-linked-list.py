class Solution:
    def delete_node(self, head, x):
        if head is None:
            return None

        if x == 1:
            temp = head
            head = head.next
            if head:
                head.prev = None
            del temp
            return head

        current = head
        for _ in range(x - 1):
            current = current.next
            if current is None:
                return head 

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

        del current
        return head
