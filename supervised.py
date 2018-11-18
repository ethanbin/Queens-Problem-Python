import random
import numpy
from sympy import *

W_MARGIN = 0.000001


def get_input_results(x: int) -> int:
    return x + random.uniform(-0.3, 0.3)


def generate_training_sets() -> list:
    training_sets = list()
    for x in range(1, 10):
        training_set = list()
        y = get_input_results(x)
        training_set.append(x)
        training_set.append(y)
        training_sets.append(training_set)
    return training_sets


# return set of calculated weights
def learn(training_sets: list) -> list:
    weights = list()
    w1 = random.uniform(-1, 1)
    w2 = random.uniform(-1, 1)
    weights = [[w1, w2], [w1 + 1, w2 + 1]]

    w0, w1, x, y = symbols('w0 w1 x y')
    # save weights to position i (0 at first), then update and store in position (i + 1)%2
    # by repeating this, we keep current weights and what weights previously were
    i = 0
    while (abs(weights[i][0] - weights[(i+1) % 2][0]) > W_MARGIN and
                    abs(weights[i][1] - weights[(i+1) % 2][1]) > W_MARGIN):
        loss = (y - (w0 + w1 * x))**2

        loss_for_w0 = diff(loss, w0)
        function_for_w0 = lambdify((w0, w1, x, y), loss_for_w0, 'numpy')
        loss_for_w1 = diff(loss, w1)
        function_for_w1 = lambdify((w0, w1, x, y), loss_for_w1, 'numpy')
        sum0 = 0
        sum1 = 0
        for trainingSet in training_sets:
            sum0 = sum0 + function_for_w0(weights[i][0], weights[i][1], trainingSet[0], trainingSet[1])
            sum1 = sum1 + function_for_w1(weights[i][0], weights[i][1], trainingSet[0], trainingSet[1])

        weights[(i + 1) % 2][0] = weights[i][0] + sum0  # + derivative of L with respect to weight0
        weights[(i + 1) % 2][1] = weights[i][1] + sum1  # + derivative of L with respect to weight0
        i = (i + 1) % 2
    print(weights[0][0], end=' ')
    print(weights[0][1])
    print(weights[1][0], end=' ')
    print(weights[1][1])
    return weights[i]


def main():
    training_sets = generate_training_sets()
    '''for set in sets:
        for val in set:
            print(val, end=' ')
        print()'''
    learn(training_sets)


if __name__ == '__main__':
    main()
