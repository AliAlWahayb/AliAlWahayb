#test
from ast import Break


T= int(input())
for i in range(T):
    str=input()
    count=0
    for i in str:
        if i =='U':
            count+=1
        elif i=='D':
            break
    print(count)


