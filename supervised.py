import random
import numpy
from sympy import *

W_MARGIN = 0.000001

def getInputResults(x : int) -> int:
    return x + random.uniform(-0.3, 0.3)

def generateTrainingSets() -> list:
    trainingSets = list()
    for x in range(1, 10):
        trainingSet = list()
        y = getInputResults(x)
        trainingSet.append(x)
        trainingSet.append(y)
        trainingSets.append(trainingSet)
    return trainingSets

# return set of calculated weights
def learn(trainingSets : list) -> list:
    weights = list()
    w1 = random.uniform(-1,1)
    w2 = random.uniform(-1,1)
    weights = [[w1, w2], [w1 + 1, w2 + 1]]

    w0, w1, x, y = symbols('w0 w1 x y')
    # save weights to position i (0 at first), then update and store in position (i + 1)%2
    # by repeating this, we keep current weights and what weights previously were
    i = 0
    while ( abs(weights[i][0] - weights[(i+1)%2][0]) > W_MARGIN and
                    abs(weights[i][1] - weights[(i+1)%2][1]) > W_MARGIN):
        L = (y - (w0 + w1 * x))**2

        L0 = diff(L, w0)
        f0 = lambdify((w0, w1, x, y), L0, 'numpy')
        L1 = diff(L, w1)
        f1 = lambdify((w0, w1, x, y), L1, 'numpy')
        sum0 = 0
        sum1 = 0
        for trainingSet in trainingSets:
            sum0 = sum0 + f0(weights[i][0], weights[i][1], trainingSet[0], trainingSet[1])
            sum1 = sum1 + f1(weights[i][0], weights[i][1], trainingSet[0], trainingSet[1])

        weights[(i + 1) % 2][0] = weights[i][0] + sum0 # + derivative of L with respect to weight0
        weights[(i + 1) % 2][1] = weights[i][1] + sum1 # + derivative of L with respect to weight0
        i = (i + 1) % 2
    print(weights[0][0], end=' ')
    print(weights[0][1])
    print(weights[1][0], end=' ')
    print(weights[1][1])


def main():
    sets = generateTrainingSets()
    '''for set in sets:
        for val in set:
            print(val, end=' ')
        print()'''
    learn(sets)


if __name__ == '__main__':
    main()