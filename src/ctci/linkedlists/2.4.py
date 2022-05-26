from utils import Node, generate


def partition(head: Node, target):
    current, left = head, None

    while current:
        if not left and current.value >= target:
            left = current

        if left and current.value < target:
            left.value, current.value = current.value, left.value
            left = left.next

        current = current.next


head = generate(1, 100, 30)
print(head)

partition(head, 66)
print(head)
