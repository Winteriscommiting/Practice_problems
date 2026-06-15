class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


prev = None
head = None


def convert(root):
    global prev, head

    if root is None:
        return

    convert(root.left)

    if prev is None:
        head = root
    else:
        root.left = prev
        prev.right = root

    prev = root

    convert(root.right)


def printDLL(head):
    while head:
        print(head.data, end=" ")
        head = head.right


n = int(input())

values = list(map(int, input().split()))

if n > 0:
    root = Node(values[0])
    queue = [root]
    i = 1

    while i < n:
        curr = queue.pop(0)

        if values[i] != -1:
            curr.left = Node(values[i])
            queue.append(curr.left)
        i += 1

        if i < n and values[i] != -1:
            curr.right = Node(values[i])
            queue.append(curr.right)
        i += 1

    convert(root)
    printDLL(head)
