def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

input=input().split()
a=int(input[0])
x=int(input[1])
n=int(input[2])
k=0
answer=0
while(k <= n):
        answer += (x**k)*(a**(n-k))*(factorial(n) / ( factorial(k) * factorial( n-k ) ))
        k+=1

answer=str(answer)
answer=answer[:-2]
print(int(answer))
