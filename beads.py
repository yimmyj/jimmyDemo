"""
ID: your_id_here
LANG: PYTHON2
TASK: beads
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
length = int(fin.readline())
necklace = str(fin.readline())

def readBlue(nklc,leng):
  counter1 = 0
  while nklc[counter1] != 'r':
    counter1 += 1
  index2 = 0
  counter2 = 0
  while nklc[index2] != 'r':
    index2 -= 1
    counter2 += 1
  counter2 -= 1
  return counter1, counter2

def readRed(nklc,leng):
  counter1 = 0
  while nklc[counter1] != 'b':
    counter1 += 1
  index2 = 0
  counter2 = 0
  while nklc[index2] != 'b':
    index2 -= 1
    counter2 += 1
  counter2 -= 1
  return counter1, counter2

maxLeft = 0
maxRight = 0
if readBlue(necklace,length)[0] >= readRed(necklace, length)[0]:
  maxLeft = readBlue(necklace,length)[0]
else:
  maxLeft = readRed(necklace, length)[0]

if readBlue(necklace,length)[1] >= readRed(necklace, length)[1]:
  maxRight = readBlue(necklace,length)[1]
else:
  maxRight = readRed(necklace, length)[1]

total = int(maxLeft) + int(maxRight)



fout.write(total + "\n")
fout.close()