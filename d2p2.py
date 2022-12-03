file = open("input2.txt")

# X = Lose
# Y = Draw
# Z = Win


def rps(cpu, you):
  score = 0
  if ((cpu == 'A' or cpu == 'B' or cpu == 'C') and (you == 'X' or you == 'Y' or you == 'Z')):
    if cpu == 'A': # CPU choose Rock
      if you == 'Z': # You need to win by choosing paper
        score += 6 + 2
      elif you == 'Y': # You need to draw by chooing Rock
        score += 3 + 1
      else: # You need to lose, by choosing Scissors
        score += 3
    elif cpu == 'B': # CPU chooses Paper
      if you == 'Z': # You need to win by choosing Scissors
        score += 6 + 3
      elif you == 'Y': # you need to draw by choosing Paper
        score += 3 + 2
      else: # You need to lose by choosing Rock
        score += 1
    else: # CPU chooses Scissors
      if you == 'Z': # You need to win by choosing Rock
        score += 6 + 1
      elif you == 'Y': # You need to draw by choosing Scissors
        score += 3 + 3
      else: # You need to lose by choosing Paper
        score += 2      
    return score
  else:
    raise Exception('Input invalid. Was given: {} {}'.format(cpu, you))

score = 0
go = True
round = file.readline()

while(go):
  if round == "":
    go = False
    print("The total score is: {}".format(score))
  else:
    if (round[-2] == " "):
      score += rps(round[0], round[-1])
    else:
      score += rps(round[0], round[-2])
    round = file.readline()
  #print(round)