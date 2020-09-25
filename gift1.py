"""
ID: your_id_here
LANG: PYTHON2
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
NP = int(fin.readline())
people = [0]*NP
money = [0]*NP
for i in range(NP):
  people[i] = fin.readline()

def give(giver,amount,receiver):
  money[people.index(giver)] -= amount
  money[people.index(receiver)] += amount

for i in range(NP):
  name = fin.readline()
  amt, num = map(int, fin.readline().split())
  if num > 0:
    for j in range(num):
      receiver = fin.readline()
      amount = amt//num
      give(name,amount,receiver)

for i in range(NP):
  fout.write(people[i].rstrip() + " " + str(money[i]) + "\n")
fout.close()