s = input()
t = input()

len_s = len(s)
len_t = len(t)

count = 0

if len_s > len_t:
    count += len_s - len_t
    
elif len_s < len_t:
    count += len_t - len_s
    
else:
    for i in range(len_s):
        if s[i] != t[i]:
            count += 1
            
print(count)
    
