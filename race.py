"""
ID: yingjimmy10
LANG: PYTHON2
TASK: race
"""
import sys
fin = open ('race.in', 'r')
fout = open ('race.out', 'w')
dist, nums = map(int, fin.readline().split())
speeds=[0]*nums
for i in range(nums):
  speeds[i] = fin.readline()
outputs = [0]*nums

def f(distance,speed,counter):
  if speed ==1 and distance ==1:
    return counter

  if speed > distance:
    return sys.maxint
  if distance<0:
    return sys.maxint
  if speed <= 0:
    return sys.maxint
  
  v1 = f(distance-speed,speed-1,counter+1)
  v2 = f(distance-speed,speed+1,counter+1)
  v3 = f(distance-speed,speed,counter+1)
  return min(v1, min(v2, v3))

outputs[0] = f(dist,1,0)+1
for i in range(1, nums):
  outputs[i] = min(outputs[i-1], f(dist,i,0)+1)

output2 = [0]*nums
for i in range(nums):
  output2[i] = outputs[speeds[i]]

for j in range(nums):
  fout.write(str(output2[j])+"\n")
fout.close()


