inp=input()
inp=inp.split()
S=inp[0]
K=int(inp[1])
answe= False
anserl=''

for i in range(len(S)):
    if S.count(S[i])== K:
        for z in range(K):
            if S[i]!=S[z]:
                continue
        answe=True
        anserl=S[i]
        break

if answe== True:
    print(f'YES {S[i]}')      
else:
    print("NO")





            
