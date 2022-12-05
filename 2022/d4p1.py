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
    
    # (b1, b2) is fully contained in (a1,a2) or vice versa
    if (a1<=b1 and b2<=a2) or (b1<=a1 and a2<=b2):
      overlaps += 1
    
    
  assign = file.readline()
  assign = assign.strip("\n")