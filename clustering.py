import numpy as np
import random
import math

def get_distance(X1, X2):
    ln = X1.shape[0]
    dist = 0
    for i in range(ln):
        dist += (X1[i]-X2[i])**2
    return math.sqrt(dist)

def get_closest(C, x):
    len_cl = C.shape[0]
    min_idx, min_dist = 0, get_distance(C[0], x)
    for i in range(len_cl):
        distance = get_distance(C[i], x)
        if(min_dist >= distance):
            min_idx = i
            min_dist = distance
    return min_idx

def recursive_K_means(X, C):
    ln_X = X.shape[0]
    clusters = [[] for i in range(C.shape[0])]
    for i in range(ln_X):
        clusters[get_closest(C, X[i])].append(i)
    
    #print(clusters)
    C_ = np.zeros_like(C)
    
    for i in range(C.shape[0]):
        ln = len(clusters[i])
        for j in range(X.shape[1]):
            mean_ = 0
            for k in range(ln):
                mean_ += X[clusters[i][k]][j]
            try:
                C_[i][j] = mean_/ln
            except:
                continue
    #print(C_)
    if array_equal(C, C_):
        #TODO: replace np.array_equal
        return C_, clusters
    return recursive_K_means(X, C_)


def K_Means(X, K):
    choose = random.sample(range(X.shape[0]), K)
    C = np.array([X[choose[i]] for i in range(K)])
    return recursive_K_means(X, C)

"""
###########################################################
# FUNCTION: K_Means_Better : computes a variety of K means and returns the best
# PRECONDITION: takes a numpy array (population) and the amount of samples(cluster choses)
# POSTCONDITION: returns a numpy array
###########################################################
def K_Means_better(X, K):
    
    possibleArrays = []                                                             # arrays will contain a 2 element list, occurance and the kmean array
    maxLoops = 10000                                                                # how many ways can you arrange K objects
    creation = 0                                                                    # the position to create arrays at
    occurance = 0                                                                   # how many times does something occur?
    occurancePosition = 0                                                           # if it occurs more than once, the location is stored
    tempArray = []                                                                  # resolve the scope of kmeans array, in a temp location

    while creation < maxLoops :                                                     # create possibly unique arrays 
        #print("{TEST} first for loop  : ")                                         # REMOVE
        tempArray = K_Means(X,K)
        #TODO: Sort the tempArray
        if creation >= len(possibleArrays):
           # print("{TEST} if creation > len  : ", creation)                         # REMOVE
            possibleArrays.append( [ 1  , tempArray ] )                             # add entry to the array ( you're at the end )
        else:                                                                       # you are inside the array
            #print("{TEST} else creation > len  : ")                                 # REMOVE
            for _ in range(creation):                                               # loop from beginning to the position you're at.
               # print("{TEST} second for loop  : ")                                 # REMOVE
                if np.array_equal(possibleArrays[creation][1], tempArray):          # is the kmean equal to any one prior?
                    #TODO: replace np.array_equal
                    possibleArrays[creation][0] = possibleArrays[creation][0] + 1   # yes? then increment the occurance of that array
            creation += 1
    
    
    for find in range(len(possibleArrays)):                                         # find the highest occurance in the possible arrays
        #print("{TEST} third for loop  : ")                                          # REMOVE
        #print("{TEST} possible array is : ", possibleArrays[find][1].tolist())      # REMOVE
        if occurance < possibleArrays[find][0]:                                     # if it is greater than the previous occurance, it is the current highest
            occurancePosition = find                                                # assign the position of the found spot to the position
    return np.array(possibleArrays[occurancePosition][1].tolist())                  # return an array at that found position
"""

def array_equal(A, B):
    if (A.shape != B.shape):
        return False
    if not isinstance(A, np.ndarray):
        return A == B
    for i, j in zip(A, B):
        if not array_equal(i, j):
            return False
    return True

def K_Means_better(X, K):
    cluster_centers = []
    maxLoops = 10000
    unique_centers = 0
    for _ in range(maxLoops):
        new_centers, cls_ = K_Means(X, K)
        got = True
        for i in range(unique_centers):
            if(array_equal(cluster_centers[i][1], new_centers)):
                cluster_centers[i][0] += 1
                got = False
                break
        if(got):
            cluster_centers.append([1, new_centers, cls_])
            unique_centers += 1
    highest_occurance = 0
    for i in range(unique_centers):
        if(cluster_centers[highest_occurance][0] < cluster_centers[i][0]):
            highest_occurance = i
    
    #for i in cluster_centers:
    #    print(i)
    
    return np.array(cluster_centers[highest_occurance][1]), cluster_centers[highest_occurance][2]