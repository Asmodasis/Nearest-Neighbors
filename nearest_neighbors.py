import numpy as np
import math

def get_distance(X1, X2):
    ln = X1.shape[0]
    dist = 0
    for i in range(ln):
        dist += (X1[i]-X2[i])**2
    return math.sqrt(dist)

def KNN_test(X_train, Y_train, X_test, Y_test, K):
    ln_train = X_train.shape[0]
    ln_test = X_test.shape[0]
    distance_matrix = np.zeros((ln_test, ln_train))
    vote_cast = np.zeros(ln_test)
    real = [i for i in range(ln_train)]
    for i in range(ln_test):
        for j in range(ln_train):
            distance_matrix[i][j] = get_distance(X_test[i], X_train[j])
    
    for i in range(ln_test):
        #print(i, end=": ")
        for j in range(K):
            mn_idx = j
            for k in range(j+1, ln_train):
                if(distance_matrix[i][mn_idx] > distance_matrix[i][k]):
                    temp = real[k]
                    real[k] = real[mn_idx]
                    real[mn_idx] = temp

                    temp = distance_matrix[i][k]
                    distance_matrix[i][k] = distance_matrix[i][mn_idx] 
                    distance_matrix[i][mn_idx] = temp
            #print(real[j], end=", ")
            vote_cast[i] += Y_train[real[j]][0]
        #print()
    #print(distance_matrix)
    #print("Voting: ", vote_cast)
    #print("Labels: ", np.ravel(Y_test))
    errors = 0
    for i in range(ln_test):
        vote_cast[i] = 1 if vote_cast[i]>0 else -1
    print("Voting: ", vote_cast)
    for i in range(ln_test):
        if(vote_cast[i]*Y_test[i][0] <= 0):
            errors += 1
    return 1 - errors/ln_test


def choose_K(X_train, Y_train, X_val, Y_val):
    track_performance = []
    ln_train = X_train.shape[0]
    for i in range(1, ln_train, 2):
        track_performance.append(KNN_test(X_train, Y_train, X_val, Y_val, i))
    max_K = 0
    for i in range(len(track_performance)):
        if(track_performance[max_K]<track_performance[i]):
            max_K = i
    return 2*max_K+1
