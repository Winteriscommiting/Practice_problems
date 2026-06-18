def dectobin(n):
    res=""
    while n>0:
        rem=n%2
        n//=2
        res+=str(rem)
    return res[::-1]
def bintodec(n):
    res=1
    for i in range(len(n)):
        res+=(int(n[i])*2)
    return res
st,end=map(int,input().split())
res=dectobin(st)
end_bin=dectobin(end)
if len(res)!=len(end_bin):
    res='0'+res
for i in range(st+1,end+1):
    temp=dectobin(i)
    if len(temp)!=len(end_bin):
        temp='0'+temp
    l=[]
    for j in range(len(res)):
        temp1=int(res[j])^int(temp[j])
        l.append(str(temp1))
    res="".join(l)
res=bintodec(res)
print(res)
