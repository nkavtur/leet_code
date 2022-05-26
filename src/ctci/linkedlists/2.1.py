from utils import Node

def remove_duplicates1(head: Node):
    seen = set()

    prev, current = None, head
    while current:
        if current.value not in seen:
            seen.add(current.value)
            prev = current
        else:
            prev.next = current.next
        current = current.next

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(1)

print(head)
remove_duplicates1(head)
print(head)


def remove_duplicates2(head: Node):
    primary = head
    while primary:

        secondary = primary
        while secondary.next:
            if secondary.next.value == primary.value:
                secondary.next = secondary.next.next
            else:
                secondary = secondary.next

        primary = primary.next

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(3)
head.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(1)

print(head)
remove_duplicates2(head)
print(head)
