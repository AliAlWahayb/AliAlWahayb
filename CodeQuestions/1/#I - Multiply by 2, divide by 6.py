#I - Multiply by 2, divide by 6
numtest=int(input())
for i in range(numtest):
    counter=0
    x= int(input())

    while x!=1:
        if x%6==0:
            x=x/6
            counter+=1
        else:
            x=x*2
            if x%6!=0:
                counter=-1
                break
            counter+=1
    print(counter)
    

        

    
