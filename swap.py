"""
ID: yingjimmy10
LANG: PYTHON2
TASK: swap
"""
import math
fin = open ('swap.in', 'r')
fout = open ('swap.out', 'w')

N, M, K = map(int, fin.readline().split())

lst = [0] * M
for i in range(M):
    A1, A2 = map(int, fin.readline().split())
    lst[i] = [A1,A2]


order = [0]*N
for i in range(N):
    order[i] = i+1

def swap(array,start,end):
    k = array[:]
    for i in range((int(math.floor(end-start+1))/2)):
        a = k[start+i-1]
        k[start+i-1] = k[end-i-1]
        k[end-i-1] = a
    return k

key = order
for i in range(M):
   key = swap(key,lst[i][0],lst[i][1])


def transform(key,prev):
    new = [0] * len(key)
    for i in range(len(key)):
        new[i] = prev[key[i]-1]
    return new

order1 = transform(key,order)
counter = 1
dict = {}
while order1 != order:
    order1 = transform(key,order1)
    counter += 1
    dict.update({counter: order1})

order = dict.get(K%counter)

for i in order:
    fout.write(str(i)+"\n")
fout.close()