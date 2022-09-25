x=input("")
y=input("")
a=x[::-1]
b=y[::-1]
if(int(b)<int(a)):
	print(y," < ",x)
elif(int(a)<int(b)):
	print(x," < ",y)
else:
	print(x," = ",y)