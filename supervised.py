import random
import numpy
from sympy import *

W_MARGIN = 0.00000001


def get_input_results(x: int) -> int:
    return x + random.uniform(-0.3, 0.3)


def generate_training_sets() -> list:
    training_sets = list()
    for i in range(1, 10):
        training_set = list()
        x = i  # random.randint(1, 101)
        y = get_input_results(x)
        training_set.append(x)
        training_set.append(y)
        training_sets.append(training_set)
    return training_sets


# return set of calculated weights
def learn(training_sets: list, learning_rate) -> list:
    weight0 = random.uniform(-1, 1)
    weight1 = random.uniform(-1, 1)

    w0, w1, x, y = symbols('w0 w1 x y')
    loss = (y - (w0 + w1 * x)) ** 2

    loss_for_w0 = diff(loss, w0)
    function_for_w0 = lambdify((w0, w1, x, y), loss_for_w0, 'numpy')
    loss_for_w1 = diff(loss, w1)
    function_for_w1 = lambdify((w0, w1, x, y), loss_for_w1, 'numpy')

    # save weights to position i (0 at first), then update and store in position (i + 1)%2
    # by repeating this, we keep current weights and what weights previously were
    last_w0, last_w1 = weight0+1, weight1+1
    while abs(last_w0 - weight0) > W_MARGIN and abs(last_w1 - weight1) > W_MARGIN:
        sum0 = 0
        sum1 = 0
        for trainingSet in training_sets:
            sum0 = sum0 + function_for_w0(weight0, weight1, trainingSet[0], trainingSet[1])
            sum1 = sum1 + function_for_w1(weight0, weight1, trainingSet[0], trainingSet[1])
        last_w0, last_w1 = weight0, weight1
        weight0 -= sum0/len(training_sets) * learning_rate
        weight1 -= sum0/len(training_sets) * learning_rate
    return weight0, weight1


def main():
    training_sets = generate_training_sets()
    '''for set in sets:
        for val in set:
            print(val, end=' ')
        print()'''
    rate = 0.00001
    w0, w1 = learn(training_sets, rate)

    print("Learning rate = ", rate)

    loss = 0
    for t in training_sets:
        loss += t[1] - (w0 + w1 * t[0])
    print ("Loss = ", loss/len(training_sets))
    print("weight0 = ", w0)
    print("weight1 = ", w1)
    print()

    x_average = 0
    y_average = 0
    for training_set in training_sets:
        x_average += training_set[0]
        y_average += training_set[1]
    x_average /= 10
    y_average /= 10
    print("Average output - average input = ", y_average - x_average)
    print("Testing weights where input = 5, output = ", w0 + w1*5)



if __name__ == '__main__':
    main()
