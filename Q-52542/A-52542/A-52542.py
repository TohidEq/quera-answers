n=input()
arr=input().split()
c=1
for i in arr:
    x=int(i)
    if(x<4):
        print("*"*x)
    else:
        print("*")
    if(c==n):
        break
    else:
        c+=1