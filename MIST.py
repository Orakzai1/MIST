import pandas as pd
import math
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
df= pd.read_csv("signalnew.csv",header=None)
data1=df.values

df1= pd.read_csv("s1.csv",header=None)
s1=df1.values


#df2 = pd.read_csv("voxel.csv",header=None)
#data2=df2.values



voxel = [[ ['0' for col in range(100)] for col in range(100)] for row in range(12)]
distance =0
#locationforant=[[0,50],[1,3],[0,50],[1,3],[0,50],[1,3],[0,50],[1,3],[0,50],[1,3],[0,50],[1,3]]
locationforant=[[0,50],[6.699,75],[25,93.301],[50,100],[75,93.301],[93.301,75],[100,50],[93.301,25],[75,6.699],[50,0],[25,6.699],[6.699,25]]

for a in range(12):
    for x in range(100):
        for y in range(100):
            distance=((math.sqrt((x-locationforant[a][0])**2+(y-locationforant[a][1])**2))/100)*3567
            voxel[a][x][y]=round(distance)




news=[ ['0' for col in range(3567)]  for row in range(12)]
new=df.values
for x in range(12):
    for y in range(3567):
        news[x][y]=new[x][3566-y]




x=df.values
delay=voxel
s2=[ ['0' for col in range(100)]  for row in range(100)]
for u in range(100):
    for v in range(100):
        energy=0
        for h in range(3567):
            z=0.0
            for l in range(12):
                if h+delay[l][u][v] < 3567:
                    m= int(h+delay[l][u][v])
                    z=z+x[l][m]
            energy=energy+z*z
        s2[u][v]=round(energy)


s3=[ ['0' for col in range(100)]  for row in range(100)]
for n in range(100):
    for o in range(100):
        s3[n][o]=s1-s2[n][o]


plt.pcolor(s2)
plt.show()