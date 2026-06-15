n = int(input())

petrol = list(map(int, input().split()))
distance = list(map(int, input().split()))

start = 0
fuel = 0
total = 0

for i in range(n):
    balance = petrol[i] - distance[i]

    fuel += balance
    total += balance

    if fuel < 0:
        start = i + 1
        fuel = 0

if total < 0:
    print(-1)
else:
    print(start)
