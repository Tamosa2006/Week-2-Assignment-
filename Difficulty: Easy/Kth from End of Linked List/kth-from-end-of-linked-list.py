class Solution:
    def getKthFromLast(self, head, k):
        first = head
        second = head

        for i in range(k):
            if first is None:
                return -1
            first = first.next

        while first:
            first = first.next
            second = second.next

        if second:
            return second.data
        else:
            return -1
