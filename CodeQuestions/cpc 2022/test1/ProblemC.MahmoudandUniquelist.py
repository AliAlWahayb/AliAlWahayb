#c
from collections import OrderedDict
T=int(input())
for tests in range(T):
    lst=list(map(str, input().split()))
    if len(lst)<3:
        lst=" ".join(lst)
    else:
        lst = list(OrderedDict.fromkeys(lst))
        lst=" ".join(lst)
    print(lst)
    
    