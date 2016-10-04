import random

def bubbleSort(A):
    flag = True
    while flag:
        flag = False
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = True

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

# def selectionSort(A):
#     flag = True
#     counter = 0
#     while flag:
#         flag = False
#         lowest = A[counter]
#         lowIndex = counter
#         if counter < len(A):
#             for i in range(counter, len(A)):
#                 if A[i] < lowest:
#                     lowest = A[i]
#                     lowIndex = i
#                     flag = True
#                 counter += 1
#             A[lowIndex],A[counter] = A[counter], A[lowIndex]

def selectionSort(A):
    for i in range(len(A)):
        most = A[i]
        for j in range(i, len(A)):
            if A[j] > most:
                most = j
        A[i], A[most] = A[most], A[i]
    return A


def createRandomList(size):
    newList = []
    for i in range(size):
        newList.append(random.randrange(0, size))
    return newList

def main():
    initialList = createRandomList(10)
    sortedList = initialList[::]
    sortedList.sort()
    print "Initial: {}".format(initialList)
    print "Default: {}".format(sortedList)
    bubbleSorted = initialList[::]
    bubbleSort(bubbleSorted)
    print "Bubble: {}".format(bubbleSorted)
    shakerSorted = initialList[::]
    shakerSort(shakerSorted)
    print "Shaker: {}".format(shakerSorted)
    selectionSorted = initialList[::]
    selectionSort(selectionSorted)
    print "Selection: {}".format(selectionSorted)




main()
