class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def removeLeadingZeros(self, head):
        while head and head.data == 0:
            head = head.next
        return head if head else Node(0)

    def addTwoLists(self, head1, head2):
        # Step 1: Reverse both lists
        head1 = self.reverseList(head1)
        head2 = self.reverseList(head2)

        dummy = Node(0)
        current = dummy
        carry = 0

        # Step 2: Add the digits
        while head1 or head2 or carry:
            val1 = head1.data if head1 else 0
            val2 = head2.data if head2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = Node(total % 10)
            current = current.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        # Step 3: Reverse the result and remove leading zeros
        result_head = self.reverseList(dummy.next)
        return self.removeLeadingZeros(result_head)
