file = open("input.txt", "r")
go = True
temp = file.readline()

total = 0
max = 0
top = []
while(go):
  if temp == "\n":
    temp = 0
    top.append(total)
    total = 0
  elif(temp == ""):
    go = False
    top = sorted(top, reverse=True)[:3]
    print("The top 3 calories is: " + str(top))
    print("The sum is: " + str(sum(top)))
  else:
    total += int(temp)
  temp = file.readline()