#k

T= int(input())
for i in range(T):
    count=0
    x=int(input())
    lst=[]
    for X in range(x-1):
        M, Y = input().split()
        lst.append(int(M))
        lst.append(int(Y))
    for N in lst:
        if lst.count(N)==1:
            count+=1
    print(count)