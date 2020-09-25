"""
ID: yingjimmy10
LANG: PYTHON2
TASK: triangles
"""
fin = open ('triangles.in', 'r')
fout = open ('triangles.out', 'w')
N = int(fin.readline())
x = [0]*N
y = [0]*N
for i in range(N):
    x[i], y[i] = map(int, fin.readline().split())

dictX = {}
dictY = {}

for i in range(N):
    if x[i] in dictX:
        yList = dictX.get(x[i])
        yList.append(y[i])
    else:
        dictX.update({x[i]:[y[i]]})

    if y[i] in dictY:
        xList = dictY.get(y[i])
        xList.append(x[i])
    else:
        dictY.update({y[i]:[x[i]]})

Area = 0

for key in dictX:
    yvals = dictX.get(key)
    if len(yvals) > 1:
        for i in yvals:
            xvals = dictY.get(i)
            if len(xvals) > 1:
                sumY = 0
                sumX = 0
                for j in yvals:
                    sumY += abs(j - i)

                for k in xvals:
                    sumX += abs(k-key)
                Area += sumX * sumY




    # ySum = 0
    # xSum = 0
    # for j in range(N):
    #     if j!= i:
    #       if x[j] == x[i]:
    #         ySum += abs(y[j]-y[i])
    #       if y[j] == y[i]:
    #         xSum += abs(x[j]-x[i])
    # Area += xSum * ySum

ans = Area % (10**9+7)

fout.write(str(ans)+"\n")
fout.close()