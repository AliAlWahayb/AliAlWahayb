#o

def gcd(a, b):
    if(b == 0):
        return abs(a)
    else:
        return gcd(b, a % b)
 
a = 1
b = 2
 
T= int(input())
for i in range(T):
    x=int(input())
    if x==1:
        if a<b:
            a=a+2
        elif b<a:
            b=b+2
    elif x==2:
        print(gcd(a,b))
    