#h
Flst=list(map(int, input().split()))
N=Flst[0]
M=Flst[1]
d2lst=[]
count=0
for i in range(N):
    lst=list(map(int, input().split()))
    d2lst.append(lst)
for i in d2lst:
    onemove=1
    if i.count(0)>i.count(1) and onemove==1:
        onemove=0
        i[i.index(0)]=1-i[i.index(0)]
        continue
        
    if i.count(0)<i.count(1) and onemove==1:
        onemove=0
        i[i.index(1)]=1-i[i.index(1)]
        continue
for i in d2lst:
    if i.count(0)!= i.count(1):
        print("NO")
        exit()

print("YES")
