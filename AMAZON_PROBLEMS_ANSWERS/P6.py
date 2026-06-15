R = int(input())
C = int(input())

M = []

for i in range(R):
    M.append(list(map(int, input().split())))

maxSum = float('-inf')

for left in range(C):
    temp = [0] * R

    for right in range(left, C):

        for i in range(R):
            temp[i] += M[i][right]

        current = temp[0]
        best = temp[0]

        for i in range(1, R):
            current = max(temp[i], current + temp[i])
            best = max(best, current)

        maxSum = max(maxSum, best)

print(maxSum)
