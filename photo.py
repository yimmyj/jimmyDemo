"""
ID: yingjimmy10
LANG: PYTHON2
TASK: photo
"""

fin = open ('photo.in', 'r')
fout = open ('photo.out', 'w')
length = int(fin.readline())
order = fin.readline()


s = []
s.append(order)

def convert(s): 
    return ([int(i) for item in s for i in item.split()]) 
  
lst = convert(s)



deltas = [0]* (length-2)

for i in range(len(deltas)):
  deltas[i] = lst[i+1]-lst[i]


def comb(x):
  for i in range(len(x)-2):
    x[i+2] += x[i]
  return x

newdeltas = [0,0] + comb(deltas)


answers = [0]*length
checker = []

flag = 0
for i in range(1,lst[0]):
  j=lst[0]-i
  answers[0] = i
  answers[1] = j
  for k in range(2,length,2):
    answers[k] = i + newdeltas[k]
  for l in range(3,length,2):
    answers[l] = j + newdeltas[l]
  flag = len(set(answers)) == len(answers)
  if flag:
   checker.append(answers)

  answers = [0] * length



checker.sort()

if len(checker)>0:
  s = str(checker[0][0])
  
  # s += str(len(checker[0]))
  for i in range (1, len(checker[0])):
    s +=" "
    s += str(checker[0][i])
  s.rstrip()
  fout.write(s)
fout.close()



