#D - Team
x= int(input())
lst =[]
for i in range(x):
    y = str(input().split("\n"))
    lst.append(y)

answer=0
for i in range(x):
    if lst[i].count("1")>1:
        answer+=1
print(answer)