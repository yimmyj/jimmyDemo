fin = open('bfs.in','r')
fout = open('dfs.out','w')

N = int(fin.readline())
K = N*[0]
for i in range(N):
    K[i] = fin.readline().split()

marked = [0] * N #common


#DFS: Recursion, proccesses one path entirely and moves on to next

def proccess(c):
    if c == N-1:
        return True
    marked[c] = 1
    for i in range(N):
        if K[c][i] == '1' and marked[i] != 1:
              if proccess(i) == True:
                  return True
    return False

#BFS: Proccesses one layer at a time

fout.write(str(proccess(0)))
fout.close()