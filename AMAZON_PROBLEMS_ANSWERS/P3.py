N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
    
key = int(input())

for i in range(N):
    if A[i] == key:
        print(i)
