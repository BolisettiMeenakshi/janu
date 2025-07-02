class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
item1 = Node(100)
item2 = Node(200)
item3 = Node(300)

item1.next = item2
item2.next = item3

print(item1.next.val)