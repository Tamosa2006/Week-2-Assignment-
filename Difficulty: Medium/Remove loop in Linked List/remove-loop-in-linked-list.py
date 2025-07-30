class Solution:
    def removeLoop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.breakLoop(head, slow)
                return True

        return True  
    
    def breakLoop(self, head, meeting_point):
        ptr1 = head
        ptr2 = meeting_point

        if ptr1 == ptr2:
            while ptr2.next != ptr1:
                ptr2 = ptr2.next
        else:
            while ptr1.next != ptr2.next:
                ptr1 = ptr1.next
                ptr2 = ptr2.next

        ptr2.next = None
