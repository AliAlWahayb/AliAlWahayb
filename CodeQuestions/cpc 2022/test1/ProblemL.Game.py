from unittest import skip


T=int(input())
for tests in range(T):
    count=0
    N=int(input())
    lst=list(map(int, input().split()))
    Flst=lst
    while len(lst)!=0:
        for i in lst:
            if len(lst)>0 and i == max(lst) :
                lst=[Flst[z] for z in range(0,lst.index(max(lst)))]
                count+=1
    if count%2==0:
        print("Jack")
    else:
        print("Mike")
    





            
