#A - Soldier and Bananas

k, n, w = input().split()

sum=0
for i in range(int(w)):
    sum+=(i+1)*int(k)

answer=sum-int(n)
if answer<0:
    answer=0


print(int(answer))
