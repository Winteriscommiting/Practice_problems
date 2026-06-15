s = list(input())
count = {}

for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 0
        
res = ""
k = list(count.keys())
v = list(count.values())
for i in range(len(k)):
    res += k[i] + str(v[i])
    
print(res)
