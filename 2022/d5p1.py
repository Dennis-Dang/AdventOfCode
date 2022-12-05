from collections import deque
file = open("input5.txt")

line = file.readline()
line = line.strip("\n")
num = 0

# Given the format of the examples and input,
# You can deduce the number of stacks based on the
# length of each line.
if ((len(line)+ 1) % 4 == 0):
  num = int((len(line) + 1)/4)
line = line+' '
stack = [None] * num
for x in range(num):
  stack[x] = deque()

#stack[0].append(1)
#stack[0].append(2)
# queues: queue.pop(0) to pop first item on list
# stack: stack.pop() to pop last item on list
go = True
while(go):
  for x in range(num):
    # Token gets each group of substring matching pattern '[L] '
    token = line[x*4:x*4+4:]
    for y in token:
      if y.isupper():
        stack[x].append(y)
  # Assumes first letter starts with 'm' (looking for the word 'move')
  if (line[0]=='m'):
    go = False
    #print("Done parsing crate stacks.")
  else:
    line = file.readline()
    line = line.strip("\n")
    line = line+' '

#print(stack)
#print(line)
go = True
while(go):
  if line == "":
    go = False
    for x in range(len(stack)):
      print(stack[x].popleft(), end = "")
  else:
    instr = []
    for x in line.split():
      if x.isdigit():
        instr.append(int(x))
    # print(instr)
    for x in range(instr[0]):
      stack[instr[2]-1].appendleft(stack[instr[1]-1].popleft())

  line = file.readline()