#E - Team Olympiad
x = int(input())
lst = input().split()
minimum = int(min(lst.count('1'),lst.count('2'),lst.count('3')))
print(minimum)
math=''
program=''
pe=''
for i in lst:
    if i=="1":
        math+=str(lst.index(i))
        lst[lst.index(i)]="0"
    elif i=="2":
        program+=str(lst.index(i))
        lst[lst.index(i)]="0"
    elif i=="3":
        pe+=str(lst.index(i))
        lst[lst.index(i)]="0"

if minimum>0:
    for i in range(minimum):
        print(math[i]+" "+program[i]+" "+pe[i])

