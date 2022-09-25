x = int(input())

def gameResult(strGame):
  gameArr = strGame.split()
  # Team_Mizban = num
  pres_Pres=int(gameArr[0]) 
  pres_Este=int(gameArr[2])
  este_Pres=int(gameArr[1])
  este_Este=int(gameArr[3])

  # if Tie(All Pres == All Este)
  if(pres_Este+pres_Pres==este_Pres+este_Este):
    if(pres_Este>este_Pres):
      return "perspolis"
    elif(este_Pres>pres_Este):
      return "esteghlal"
    else:
      return "penalty"
  elif(pres_Este+pres_Pres>este_Pres+este_Este):
    return "perspolis"
  else:
    return "esteghlal"



answer = []
for i in range(0,x):
  answer.append(gameResult(input()))
for string in answer:
  print(string)
