#H - Buy a Shovel
x, y = input().split()
x= int(x)
y= int(y)
counter=1
while True :
    if (x*counter)%10== y or (x*counter)%10==0:
        break
    else:
        counter+=1
        
print(counter)

