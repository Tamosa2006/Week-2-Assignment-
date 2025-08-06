class Solution:
    def isCircular(self, head):
        if head is None:
            return False
        
        temp = head.next
        while temp is not None and temp != head:
            temp = temp.next
        
        return temp == head
