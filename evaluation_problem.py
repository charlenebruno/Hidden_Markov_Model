#Algorithm to compute the probability of a given sequence of visible states from an HMM M.

import numpy as np

#nb of hidden states
N=3

#nb of observable states
T=4
K=4

#given sequence: x = {x1,x3,x2,x0}

#Matrix aij (transition probability from z(t-1)=zi to z(t)=zj
aij = np.array([[1,0,0,0],
                [0.2,0.3,0.1,0.4],
                [0.2,0.5,0.2,0.1],
                [0.7,0.1,0.1,0.1]])
print("aij")
print(aij)

#Matrix bjk (emission probability from z(t)=zj to x(t)=xk
bjk = np.array([[1,0,0,0,0],
                [0,0.3,0.4,0.1,0.2],
                [0,0.1,0.1,0.7,0.1],
                [0,0.5,0.2,0.1,0.2]])
print("bjk")
print(bjk)

#initialization
alphaMatrix = np.zeros((N+1,T+1))

for j in range(0,N+1):
    if j == 1:
        alphaMatrix[j][0] = 1
    else:
        alphaMatrix[j][0] = 0
print(alphaMatrix)

#HMM forward algorithm
def HMM(T,N,alphaMatrix,aij,bjk):
    for t in range(1,T+1):
        for j in range(1,N+1):
            sum = 0
            for i in range(0,N+1):
                sum+= alphaMatrix[i][t-1]*aij[i][j]
            print(sum)
            alphaMatrix[j][t] = bjk[j][t]*sum
    print(alphaMatrix)
    return alphaMatrix[0][T]

result = HMM(T,N,alphaMatrix,aij,bjk)
print(result)


