"""
ID: your_id_here
LANG: PYTHON2
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
s = []
for line in fin:
  s.append(line)

def encode(x):
  total = 1
  for i in range(len(x)):
    total *= (ord(x[i]) - 64)
  return total

answer = ""
if encode(s[0]) %47 == encode(s[1]) %47:
  answer = "GO"
else:
  answer = "STAY"
fout.write (str(answer) + '\n')
fout.close()

