"""
ID: yingjimmy10
LANG: PYTHON2
TASK: photo
"""

fin = open ('photo.in', 'r')
fout = open ('photo.out', 'w')
length = fin.readline()
order = str(fin.readline())
s = []
s.append(order)

def convert(s): 
    return ([int(i) for item in s for i in item.split()]) 
  
lst = convert(s)

print(lst)

deltas = [0]* (length-2)

for i in range(len(deltas)):
  deltas[i] = lst[i+1]-lst[i]

print(deltas)

def comb(x):
  for i in range(len(x)-2):
    x[i+2] += x[i]
  return x

newdeltas = [0,0] + comb(deltas)
print(newdeltas)

answers = [0]*length
checker = []


for i in range(1,lst[0]+1):
  for j in range(1,lst[0]+1):
    if i + j == lst[0]:
      answers[0] = i
      answers[1] = j
      for k in range(2,length,2):
        answers[k] = i + newdeltas[k]
      for l in range(3,length,2):
        answers[l] = j + newdeltas[l]
  flag = 0
  flag = len(set(answers)) == len(answers)
  if flag:
   checker.append(answers)
  answers = [0] * length

checker.sort()

for i in checker[0]:
  fout.write(i),
fout.write("\n")
fout.close()



