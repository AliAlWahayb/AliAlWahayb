#B - String Task
a =str(input())
a=a.lower()
voule="aoyeui"
for i in voule:
    a=a.replace(i, "")

new = list(a)
for i in range(0,len(a)*2,2):
    new.insert(i, '.')


new = ''.join(new)

print(new)
