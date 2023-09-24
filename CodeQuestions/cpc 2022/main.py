#test
case=int(input())

for i in range(case):
    number=input()
    for i in str(number):
        if str(number).count(i)!=str(number).index(i):
            print("not self-describing")
            exit()
        else:
            continue
        print("self-describing")

