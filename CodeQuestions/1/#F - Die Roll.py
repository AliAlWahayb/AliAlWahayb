#F - Die Roll

from fractions import Fraction
x, y = input().split()

counter = 0
for i in range(1,6+1):
    if i>=max(int(x),int(y)):
        counter += 1
    

if counter/6==0:
    print("0/1")
elif counter/6==1:
    print("1/1")
else:
    print (Fraction(counter, 6))




