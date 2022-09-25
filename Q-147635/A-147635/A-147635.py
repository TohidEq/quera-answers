days = int(input())
x=input().split()
for i in range(0,days):
  if(int(x[i])>15):
    print("cooler")
  else:
    print("heater")