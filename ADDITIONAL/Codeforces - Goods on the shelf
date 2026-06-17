import sys

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    
    first, last, count = {}, {}, {}
    for i, x in enumerate(a):
        if x not in first: first[x] = i
        last[x] = i
        count[x] = count.get(x, 0) + 1
        
    l, r = 0, n - 1
    while l < n and last[a[l]] - l + 1 == count[a[l]] and all(a[k] == a[l] for k in range(l, last[a[l]] + 1)):
        l = last[a[l]] + 1
    while r >= l and r - first[a[r]] + 1 == count[a[r]] and all(a[k] == a[r] for k in range(first[a[r]], r + 1)):
        r = first[a[r]] - 1
        
    if l > r:
        print("YES")
        continue
        
    blocks = []
    prev = None
    for i in range(l, r + 1):
        if a[i] != prev:
            blocks.append(i)
            prev = a[i]
    blocks.append(r)
    candidates = sorted(list(set(blocks)))
    
    if len(candidates) > 15:
        print("NO")
        continue
        
    found = False
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            idx1, idx2 = candidates[i], candidates[j]
            a[idx1], a[idx2] = a[idx2], a[idx1]
            
            possible, seen, prev_val = True, set(), None
            for k in range(l, r + 1):
                if a[k] != prev_val:
                    if a[k] in seen:
                        possible = False
                        break
                    seen.add(a[k])
                    prev_val = a[k]
                    
            if possible:
                found = True
                a[idx1], a[idx2] = a[idx2], a[idx1]
                break
            a[idx1], a[idx2] = a[idx2], a[idx1]
        if found: break
        
    print("YES" if found else "NO")
