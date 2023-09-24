#M

from unittest import skip


T= int(input())
for i in range(T):
    c = sorted(list(map(int, input().split())))
    n=int(input())
    price = sorted(list(map(int, input().split())))

    for x in range(5):
        for z in range(n):
            if price[z] <= c[x]:
                price.pop(z)
                break
            elif price[z] > c[x]:
                print("NO")
                exit()
    print("YES")


