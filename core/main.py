'''
Created on Aug 20, 2015

@author: Sheece Gardezi
implementation of Edit Distance - Dynamic Programming
'''
testStrings=["Distance","aDiatanc"]
lenghtTestString=[len(testStrings[0]),len(testStrings[1])];

interger=0
distanceMatrics=[[interger for i in range(lenghtTestString[0])] for j in range(lenghtTestString[1])]

for i in range(0,lenghtTestString[0]):
    for j in range(0,lenghtTestString[1]):
        distanceMatrics[i][j]=0;
        
print(distanceMatrics)

s = [[str(e) for e in row] for row in distanceMatrics]
lens = [max(map(len, col)) for col in zip(*s)]
fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
table = [fmt.format(*row) for row in s]
print '\n'.join(table)