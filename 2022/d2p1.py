# RPS logic: 
#   Rock defeats Scissors
#   Scissors defeats Paper
#   Paper defeats Rock
#
# Points allocation:
#   Shape: +1 = Rock, +2 = Paper, +3 = Scissors
#   Outcome: 0 = Lose, +3 = draw, +6 = win

file = open("input2.txt")

round = file.readline()
score = 0
go = True

def rps(cpu, you):
  score = 0
  if ((cpu == 'A' or cpu == 'B' or cpu == 'C') and (you == 'X' or you == 'Y' or you == 'Z')):
    if you == 'X': # You play Rock
      score += 1
      if cpu == 'A': # Draw, CPU plays Rock
        score += 3
      elif cpu == 'C': # Win, CPU plays Scissors
        score += 6
    elif you == 'Y': # You play Paper
      score +=2
      if cpu == 'A': # Win, CPU plays Rock
        score += 6
      elif cpu == 'B': # Draw, CPU plays Paper
        score += 3
    else: #You play Scissors
      score += 3
      if cpu == 'C': # Draw, CPU plays Scissors
        score += 3
      elif cpu == 'B': # Win, CPU plays Paper
        score += 6
    return score
  else:
    raise Exception('Input invalid. Was given: {} {}'.format(cpu, you))

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
