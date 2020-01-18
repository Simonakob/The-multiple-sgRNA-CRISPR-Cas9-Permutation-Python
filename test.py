### "1. Pascal's Triangle Numbers" ###

# generate pascal triangle numbers
row=[1]
for i in range(17):    
    print(*row, sep=", ") # print list without brackets  
    newrow=[]
    newrow.append(row[0])
    for i in range(len(row)-1):
        newrow.append(row[i]+row[i+1])
    newrow.append(row[-1])
    row=newrow

# command line on the shell
# python test.py > log.csv


### "2. Total Events for the 4sgRNA System in Tetraploid" ###

import numpy as np
import itertools
from pandas import read_csv

# calculate total combinations                  
a = list(itertools.product([0,1], repeat=16))
    #tetraploid / 4gRNAs; repeat=16
    #tetraploid / 3gRNAs; repeat=12
    #tetraploid / 2gRNAs; repeat=8
    #tetraploid / 1gRNA; repeat=4
    #diploid / 4gRNAs; repeat 8
    #diploid / 3gRNAs; repeat 6
    #diploid / 2gRNAs; repeat 4
    #diploid / 1gRNA; repeat 2

# save into csv
np.savetxt("foo-1.csv", a, delimiter=",", fmt='%4d')

# command line on the shell
# python test.py


### "3. Sums of Events per Chromosome/Target Site" ###

# put the column header in the dataframe and then save it.
df = pd.read_csv("foo-1.csv", sep = ',', names=[
    'a','b','c','d',
    'e','f','g','h',
    'i','j','k','l',
    'm','n','o','p'
    ])
df.to_csv('foo-2.csv')

# command line on the shell
# python test.py

df = read_csv('foo-2.csv')
# sum of events per chromosome 
# (z1 for chrI, z2 for chrII, z3 for chrIII and z4 for chrIV)
# sum of events per TS(target site)
# (y1 for TS1, y2 for TS2, y3 for TS3 and y4 for TS4)
df1 = df.assign(
    z1 = df.a + df.b + df.c + df.d,
    z2 = df.e + df.f + df.g + df.h,
    z3 = df.i + df.j + df.k + df.l,
    z4 = df.m + df.n + df.o + df.p,
    y1 = df.a + df.e + df.i + df.m,
    y2 = df.b + df.f + df.j + df.n,
    y3 = df.c + df.g + df.k + df.o,
    y4 = df.d + df.h + df.l + df.p
    )
#save as csv
df1.to_csv('foo-3.csv')

# command line on the shell
# python test.py

### "4. Tetra-allelic Events" ###

# select rows without '0' values 
# in columns z1, z2, z3 and z4
# filter only tetra-allelic mutations
df2 = read_csv('foo-3.csv')
df3 = df2.loc[
    (df2['z1'] != 0) & 
    (df2['z2'] != 0) & 
    (df2['z3'] != 0) & 
    (df2['z4'] != 0)
    ]
#save as csv
df3.to_csv('foo-4.csv')

# command line on the shell
# python test.py

### "5. Cis-tetra-allelic Events" ###

# select rows with '4' values in columns y1, y2, y3 and y4
# filter only cis-tetra-allelic mutations at TS1
df2 = read_csv('foo-3.csv')
df4 = df2.loc[df2['y1'] == 4]
#save as csv
df4.to_csv('foo-5.csv')

# command line on the shell
# python test.py

### "6. Probability of the Tetra-allelic Events" ###

# In tetraploid the 4sgRNAs/CRISPR/Cas9 could produce 
# tetra-allelic mutants with a probability below.
a = 65536 # total_combinations
b = 50625 # tetra-allelic_events
c = b / a  # probability
p = print('The probability of the tetra-allelic events is %0.4f' %c)

# command line on the shell
# python test.py > log.txt