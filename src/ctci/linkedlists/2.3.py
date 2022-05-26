from utils import Node

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next

head = Node('a')
head.next = Node('b')
head.next.next = Node('c')
head.next.next.next = Node('d')
head.next.next.next.next = Node('e')
head.next.next.next.next.next = Node('f')
head.next.next.next.next.next.next = Node('g')
head.next.next.next.next.next.next.next = Node('h')

delete_middle_node(head.next.next.next.next.next.next)
print(head)
