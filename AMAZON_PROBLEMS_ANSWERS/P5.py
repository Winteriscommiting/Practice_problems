class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


leaf_level = -1

def check(root, level):
    global leaf_level

    if root is None:
        return True

    if root.left is None and root.right is None:
        if leaf_level == -1:
            leaf_level = level
            return True
        return level == leaf_level

    return check(root.left, level + 1) and check(root.right, level + 1)


n = int(input())

arr = list(map(int, input().split()))

if n > 0:
    root = Node(arr[0])
    q = [root]
    i = 1

    while i < n:
        curr = q.pop(0)

        if arr[i] != -1:
            curr.left = Node(arr[i])
            q.append(curr.left)
        i += 1

        if i < n and arr[i] != -1:
            curr.right = Node(arr[i])
            q.append(curr.right)
        i += 1

    print(1 if check(root, 0) else 0)
