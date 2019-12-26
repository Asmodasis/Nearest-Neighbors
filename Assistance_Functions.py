
import time
import numpy as np
###########################################################
# FUNCTION: myRandom : makes a random number
# PRECONDITION: takes an integer value as the seed
# POSTCONDITION: returns a random integer
###########################################################
def myRandom(seed):                                                             # generate random numbers with a seed

    intHolder = seed ** seed if seed < 100000 else seed                         # if seed is a big number, don't power set it

    for i in range(1,10):                                                       # loop through ten times
        strHolder = str(intHolder)                                              # store the new made number in a string
        l = int(len(strHolder)) // 2                                            # length of string / 2 is the middle
        strHolder = strHolder[l-2:l+2]                                          # keep only the middle pieces of the "int"
        intHolder = int(strHolder) - i                                          # int is the string minus the iterator 
    return intHolder                                                            # when done return it

###########################################################
# FUNCTION: randomSample : makes a random list
# PRECONDITION:  takes an integer value as the seed
# POSTCONDITION: returns a random integer
###########################################################
def randomSample(population, K): 
    print("{TEST} randomSampleCalled")


#def makeZeroArray(x):
#    returnArray = np.asarray(x)
#    for position in returnArray:
#        returnArray[position] = 0
#    return returnArray
"""
def makeZeroArray(x, y = None):
   
    if y is not None:
        returnArray = np.asarray(x, y)
        for element in returnArray:
            for position in element:
                returnArray[element][position] = 0
    else: 
        returnArray = np.asarray(x)
        for position in returnArray:
            returnArray[position] = 0
    return returnArray

print("Make Zero Array = ", makeZeroArray(2))

"""

print("numpy zeros is ", np.array(
                                    list(list(0 for j in range(3)) for i in range(2))
                                  )
    )

#milli_sec = int(round(time.time() * 1000))
#print(milli_sec)
#print(myRandom(milli_sec))
#def randomSample(population, k):