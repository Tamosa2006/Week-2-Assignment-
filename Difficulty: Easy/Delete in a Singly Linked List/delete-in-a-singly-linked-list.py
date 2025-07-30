def deleteNode(head, x):
    if x == 1:
        return head.next

    current = head
    for i in range(x - 2):
        current = current.next

    if current.next:
        current.next = current.next.next

    return head
