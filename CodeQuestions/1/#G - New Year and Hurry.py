#G - New Year and Hurry
x, y = input().split()
ToMidNight=240
counter=0
for i in range(1,int(x)+1):
    if ToMidNight-(i*5)>=int(y):
        counter+=1
        ToMidNight=ToMidNight-(i*5)

print(counter)