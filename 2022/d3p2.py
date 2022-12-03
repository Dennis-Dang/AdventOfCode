file = open("input3.txt")
go = True
common = []

while(go):
  r1 = file.readline()
  r2 = file.readline()
  r3 = file.readline()
  if r1 == "" or r2 == "" or r3 == "":
    go = False
    #print("Common letter pairs are: {}".format(common))
    sum = 0
    for x in common:
      if x.isupper():
        #print("{} is {}".format(x, ord(x)-38))
        sum += (ord(x)-38)
      else:
        #print("{} is {}".format(x, ord(x)-96))
        sum += (ord(x)-96)
    print("The sum is: {}".format(sum))
  else:
    #print("r1: {}".format(r1))
    #print("r2: {}".format(r2))
    r1 = r1.strip("\n")
    r2 = r2.strip("\n")
    r3 = r3.strip("\n")
    temp = "".join(set(r1).intersection(r2))
    #print("intersection of r1+r2: {}".format(temp))
    common.append("".join(set(temp).intersection(r3)))
    #print("intersection of that and r3: {}".format(common))