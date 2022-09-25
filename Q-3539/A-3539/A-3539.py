n=input()
x=0
while( len(str(n)) != 1):
        i = 0
        x=0
        while( i < len(str(n)) ):
                y=str(n)
                y=y[i]
                x=int(y)+int(x)
                i+=1
        n=x
print(n)
