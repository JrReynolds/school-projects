import random

def bubbleSort(A):
    flag = True
    while flag:
        flag = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
    return A

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

def main():
    initialList = createRandomList(10)
    defaultSorted = initialList[:]
    defaultSorted.sort()
    bubbleSorted = bubbleSort(initialList[:])
    if bubbleSorted != defaultSorted:
        print "Error in Bubble Sort"
    shakerSorted = shakerSort(initialList[:])
    if shakerSorted != defaultSorted:
        print "Error in Shaker Sort"
    selectionSorted = selectionSort(initialList[:])
    if selectionSorted != defaultSorted:
        print "Error in Selection Sort"





main()
