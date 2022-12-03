file = open("input.txt", "r")
go = True
temp = file.readline()

total = 0
max = 0
while(go):
  if temp == "\n":
    temp = 0
    if total >= max:
      max = total
    total = 0
  elif(temp == ""):
    go = False
    print("The max is: " + str(max))
  else:
    total += int(temp)
  temp = file.readline()
