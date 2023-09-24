#sadaw
N=int(input())
jackgits=list(map(int, input().split()))
greggifts=list(map(int, input().split()))

if sum(jackgits)==sum(greggifts):
    print("fair")
elif sum(jackgits)!=sum(greggifts):
    print("not fair")