class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(values):
    if not values:
        return None

    root = Node(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        curr = queue.pop(0)

        if values[i] != -1:
            curr.left = Node(values[i])
            queue.append(curr.left)
        i += 1
        if i < len(values) and values[i] != -1:
            curr.right = Node(values[i])
            queue.append(curr.right)
        i += 1

    return root


def isBST(root, minVal=float('-inf'), maxVal=float('inf')):
    if root is None:
        return True

    if root.data <= minVal or root.data >= maxVal:
        return False

    return (isBST(root.left, minVal, root.data) and
            isBST(root.right, root.data, maxVal))


arr = list(map(int, input().split()))

root = buildTree(arr)

print(1 if isBST(root) else 0)
