number = int(input("Enter a number:"))
primeflag=True

print("task1")

if number > 1:
    for i in range(2,number):
        if (number%i)==0:
            print(number,"is not a prime number")
            primeflag=False
            break
        else:
            print(number,"is a prime number")
            break

print("task2")

if primeflag==False:
    print("the factors of ",number," are:")
    for i in range(1,number+1):
        if number%i ==0:
            print(i)

print("task3")

for x in range(-5,5):
    Y =(8*(x*x))+1
    print(Y)