import random

def bubbleSort(A):
    compares = 0
    swaps = 0
    flag = True
    while flag:
        flag = False
        for i in range(len(A)-1):
            compares+=1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swaps+=1
                flag = True
    return (A, compares, swaps)

def shakerSort(A):
    flag = True
    while flag:
        flag = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
        for i in range(1, len(A), -1):
            if A[i] < A[i-1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
    return A

def selectionSort(A):
    for i in range(len(A)):
        most = A[i]
        mostIndex = i
        for j in range(i, len(A)):
            if A[j] < most:
                most = A[j]
                mostIndex = j
        A[i], A[mostIndex] = A[mostIndex], A[i]
    return A

def createRandomList(size):
    newList = []
    for i in range(size):
        newList.append(random.randrange(0, size))
    return newList

def createMSList(size):
    newList = []
    for i in range(size):
        newList.append(i)
    newList[0], newList[size-1] = newList[size-1], newList[0]
    return newList

def main():
    randomList = createRandomList(8)
    MSList = createMSList(8)
    bubbleSortedR = bubbleSort(randomList[:])
    bubbleSortedMS = bubbleSort(MSList[:])
    print bubbleSortedR[1], bubbleSortedR[2]





main()
