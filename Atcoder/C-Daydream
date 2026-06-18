s=input()
rev=s[::-1]
l=["maerd","remaerd","esare","resare"]
c=0
temp=1
while c<len(rev):
    m=0
    for j in l:
        if rev[c:].startswith(j):
            c+=len(j)
            m=1
            break
    if not m:
        temp=0
        break
if temp and c==len(rev):
    print("YES")
else:
    print("NO")
