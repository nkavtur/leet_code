import random


class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def __str__(self) -> str:
        res = ''

        current = self
        while current.next:
            res += f"{current.value} -> "
            current = current.next
        res += str(current.value)

        return res

def generate(min, max, k):
    node_values = random.sample(range(min, max), k)

    head = current = None
    for value in node_values:
        if not head:
            head = current = Node(value)
        else:
            current.next = Node(value)
            current = current.next

    return head

