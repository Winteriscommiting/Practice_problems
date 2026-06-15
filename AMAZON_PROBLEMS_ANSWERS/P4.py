N = int(input())
M = int(input())
mat = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(input()))
    mat.append(row)

X = int(input())
for i in mat:
    if X in i:
        print(1)
        break
    else:
        print(0)
        break
