import random
import sys
from sort2 import *

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
    compares = 0
    swaps = 0
    flag = True
    while flag:
        flag = False
        for i in range(len(A)-1):
            compares += 1
            if A[i] > A[i+1]:
                swaps += 1
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
        for i in range(1, len(A), -1):
            compares += 1
            if A[i] < A[i-1]:
                swaps += 1
                A[i], A[i+1] = A[i+1], A[i]
                flag = True
    return (A, compares, swaps)

def selectionSort(A):
    compares = 0
    swaps = 0
    for i in range(len(A)):
        most = A[i]
        mostIndex = i
        for j in range(i, len(A)):
            compares += 1
            if A[j] < most:
                most = A[j]
                mostIndex = j
        A[i], A[mostIndex] = A[mostIndex], A[i]
        swaps += 1
    return (A, compares, swaps)

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
    file = open("RandomCompares.txt", "w")
    sizeList = []
    sizeListCounter = 8
    while sizeListCounter <= 4096:
        sizeList.append(sizeListCounter)
        sizeListCounter *= 2
    for i in sizeList:
        RList = createRandomList(i)
        # MSList = createMSList(i)
        funcs = [bubbleSort, shakerSort, selectionSort, MergeSort, QuickSort, HashSort]
        for f in funcs:
            if f != QuickSort:
                a = f(RList)
                RResultString = str(a[1])
            else:
                a = f(RList, 0, i, False)
                b = f(RList, 0, i, True)
                RResultString = str(a[1]) + str(b[1])
            file.write(RResultString)

    file.close()











main()
