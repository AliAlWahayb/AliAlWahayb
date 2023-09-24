#j
S=str(input())
for z in S:
    if S.count(z)>1:
        i = S.index(z)
        S=S[:i]+S[i+1:]
print(S)