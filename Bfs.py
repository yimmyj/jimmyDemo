fin = open('bfs.in','r')
fout = open('bfs.out','w')

N = int(fin.readline())
K = N*[0]
for i in range(N):
    K[i] = fin.readline().split()

marked = [0] * N


lst = [0]
#maintain the list, use while loop
def proccess(c):
    marked[c] = 1
    lst.pop(0)
    for i in range(N):
        if K[c][i] == '1':
            if marked[i] != 1 and i not in lst:
              lst.append(i)

while len(lst) > 0:
    if lst[0] == N - 1:
        fout.write('True')
        fout.close()
        exit()
    if marked[lst[0]] == 0:
       proccess(lst[0])


fout.write('False')
fout.close()