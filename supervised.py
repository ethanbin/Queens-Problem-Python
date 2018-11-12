import random


W_MARGIN = 0.0001

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

    i = 0
    while ( abs(weights[i][0] - weights[(i+1)%2][0]) < W_MARGIN and
                    abs(weights[i][1] - weights[(i+1)%2][1]) < W_MARGIN):
        weights[i][0] = weights[i][0] + 0
        i = (i + 1) % 2

def main():
    sets = generateTrainingSets()
    '''for set in sets:
        for val in set:
            print(val, end=' ')
        print()'''
    learn(sets)


if __name__ == '__main__':
    main()