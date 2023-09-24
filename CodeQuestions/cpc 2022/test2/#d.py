# d

T = int(input())
for i in range(T):
    lst = []
    X, Y = input().split()
    for i2 in range(int(X)):
        c = list(map(int, input().split()))
        lst.append(c)
    for i3 in lst:
        ans=[]
        for i4 in lst:
            if i3!= i4:
                ans.append(sum([i*j for (i, j) in zip(i3, i4)]))
    print(max(ans))