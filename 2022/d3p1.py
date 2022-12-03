file = open("input3.txt")

rucksack = file.readline()
go = True
common = []

while(go):
  if rucksack == "":
    go = False
    # print("Common letter pairs are: {}".format(common))
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
    n = len(rucksack)
    r1 = rucksack[0:n//2]
    r2 = rucksack[n//2:]
    common.append("".join(set(r1).intersection(r2)))
  rucksack = file.readline()
