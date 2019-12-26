import numpy as np
import random

MAX_EPOCH = 10

def run_epoch(X, Y, w_, b_):
    #print("1", w_, b_)
    w, b = w_.copy(), float(b_)
    for i in range(X.shape[0]):
        activation = b
        for j in range(X.shape[1]):
            activation += w[j]*X[i][j]
        if(activation*Y[i][0] <= 0):
            b += Y[i][0]
            for j in range(X.shape[1]):
                w[j] += X[i][j]*Y[i][0]
    #print("2", w, b)
    return w, b

def compare(w, b, w_, b_):
    for i in range(w.shape[0]):
        if(w[i] != w_[i]):
            return True
    return b != b_

def perceptron_train(X, Y):
    w = np.array([random.random() for i in range(X.shape[1])])
    b = random.random()
    w_, b_ = run_epoch(X, Y, w, b)
    epoch = 1
    while(epoch<MAX_EPOCH and compare(w, b, w_, b_)):
        w, b = run_epoch(X, Y, w_, b_)
        epoch += 1
        if(compare(w_, b_, w, b)):
            w_, b_ = run_epoch(X, Y, w, b)
        else:
            break
    print(epoch)
    return w_, b_

def perceptron_test(X_test, Y_test, w, b):
    correct = 0
    for i in range(X_test.shape[0]):
        activation = b
        for j in range(X_test.shape[1]):
            #print("{TEST} Y_test is ", Y_test[i][0].tolist())   #REMOVE
            activation += w[j]*X_test[i][j]
        if(activation*Y_test[i][0] > 0):
            correct += 1
    return correct/X_test.shape[0]

