from utils import Node

def find_kth_to_last(head: Node, k):
    slow = fast = head

    for i in range(0, k):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(1)

print(find_kth_to_last(head, 9).value)

