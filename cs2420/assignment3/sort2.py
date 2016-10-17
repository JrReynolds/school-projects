import random


def generate_list(length):
    list1 = []
    for i in range(length):
        list1.append(random.randint(0, length - 1))
    return list1

def MergeSort(A):
    compares = 0
    swaps = 0
    if len(A) == 1:
        return (A, compares, swaps)
    mid = len(A) // 2
    LH = A[:mid]
    RH = A[mid:]
    LH, newcompares, newswaps = MergeSort(LH)
    compares += newcompares
    RH, newcompares, newswaps = MergeSort(RH)
    compares += newcompares
    returnList = [-1] * len(A)
    LHCounter = 0
    RHCounter = 0
    FinalCounter = 0
    while FinalCounter < len(A):
        if LHCounter < len(LH) and RHCounter < len(RH):
            compares += 1
            if LH[LHCounter] <= RH[RHCounter]:
                swaps += 1
                returnList[FinalCounter] = LH[LHCounter]
                FinalCounter += 1
                LHCounter += 1
            else:  # LH[LHCounter] > RH[RHCounter]:
                swaps += 1
                returnList[FinalCounter] = RH[RHCounter]
                FinalCounter += 1
                RHCounter += 1
        else:
            while LHCounter < len(LH):
                swaps += 1
                returnList[FinalCounter] = LH[LHCounter]
                FinalCounter += 1
                LHCounter += 1
            while RHCounter < len(RH):
                swaps += 1
                returnList[FinalCounter] = RH[RHCounter]
                FinalCounter += 1
                RHCounter += 1

    return (returnList, compares, swaps)

def QuickSortR(A, low, high, flag):
    compares = 0
    swaps = 0
    if low >= high:
        return A, compares, swaps
    if flag:
        mid = (low + high)//2
        A[mid], A[low] = A[low], A[mid]
        swaps += 1
    pivot = A[low]
    lmbt = low+1
    for i in range(low+1, high+1):
        compares += 1
        if A[i]<pivot:
            A[lmbt], A[i] = A[i], A[lmbt]
            swaps += 1
            lmbt+=1
    rmlt = lmbt-1
    A[low], A[rmlt] = A[rmlt], A[low]
    swaps += 1
    A, newcompares, newswaps = QuickSortR(A, low, rmlt-1, flag)
    compares += newcompares
    swaps += newswaps
    A, newcompares, newswaps = QuickSortR(A, lmbt, high, flag)
    compares += newcompares
    swaps += newswaps
    return (A, compares, swaps)

def QuickSortRegular(A):
    A, compares, swaps = QuickSortR(A, 0, len(A)-1, False)
    return (A, compares, swaps)

def QuickSortMod(A):
    A, compares, swaps = QuickSortR(A, 0, len(A)-1, True)
    return (A, compares, swaps)
    
def HashSort(A):
    new = []
    for i in A:
        new.append(0)
    for i in A:
        new[i] += 1
    final = []
    for i in range(len(new)):
        for j in range(new[i]):
            final.append(i)
    compares = len(A)
    swaps = len(A)
    return (final, compares, swaps)

# def main():
#     size = 10
#     starterList = generate_list(size)
#     defaultSorted = starterList[:]
#     defaultSorted.sort()
#     HashSorted = HashSort(starterList[:])
#     if HashSorted != defaultSorted:
#         print "Error in HashSort"
#     MergeSorted = MergeSort(starterList[:])
#     if MergeSorted != defaultSorted:
#         print "Error in MergeSort"
#     defaultQuickSorted = QuickSort(starterList[:], 0, size, False)
#     if defaultQuickSorted != defaultSorted:
#         print "Error in QuickSort (default)"
#         print defaultSorted
#         print defaultQuickSorted
#     modQuickSorted = QuickSort(starterList[:], 0, size, True)
#     if modQuickSorted != defaultSorted:
#         print "Error in QuickSort (modified)"
#         print defaultSorted
#         print modQuickSorted
#
#     #assignment 3 stuff
#     print


# main()
