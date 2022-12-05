file = open("input4.txt")
go = True
overlaps = 0

assign = file.readline()
assign = assign.strip("\n")
while(go):
  if assign == "":
    go = False
    print("Overlaps are: {}".format(overlaps))
  else:
    section1, section2 = assign.split(",")
    a1, a2 = section1.split("-")
    b1, b2 = section2.split("-")
    a1, a2, b1, b2 = [int(x) for x in [a1, a2, b1, b2]] # Turn s1id1 .... s2id2 into integers.
    
    # +1 for the range because it's inclusive.
    if (set(range(a1,a2+1)).intersection(set(range(b1,b2+1)))):
      overlaps += 1
      #print(section1, section2, end=" ")
      #print()
  assign = file.readline()
  assign = assign.strip("\n")