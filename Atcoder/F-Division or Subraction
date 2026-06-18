n=int(input())
if n==2: 
    print(1)
    exit()
ans=set()
for j in (n,n-1):
    i=1
    while i*i<=j:
        if j%i==0:
            for k in (i,j//i):
                if k>1:
                    if j==n-1:
                        ans.add(k)
                    else:
                        temp=n
                        while temp%k==0:
                            temp //= k
                        if temp%k==1:
                            ans.add(k)
        i+=1
print(len(ans))
