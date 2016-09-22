import random

def generate_list(length):
	list1 = []
	for i in range(length):
		list1.append(random.randint(0, length-1))
	return list1

def MergeSort(A):
	if len(A) == 1:
		return A
	mid = len(A)//2
	LH = A[:mid]
	RH = A[mid:]
	LH = MergeSort(LH)
	RH = MergeSort(RH)
	returnList = [-1] * len(A)
	LHCounter = 0
	RHCounter = 0
	FinalCounter = 0
	while FinalCounter < len(A):
		if LHCounter < len(LH) and RHCounter < len(RH):
			if LH[LHCounter] <= RH[RHCounter]:
				returnList[FinalCounter] = LH[LHCounter]
				FinalCounter += 1
				LHCounter += 1
			else: # LH[LHCounter] > RH[RHCounter]:
				returnList[FinalCounter] = RH[RHCounter]
				FinalCounter += 1
				RHCounter += 1
		else:
			while RHCounter < len(RH):
				returnList[FinalCounter] = RH[RHCounter]
				FinalCounter += 1
				RHCounter += 1
			while LHCounter < len(LH):
				returnList[FinalCounter] = LH[LHCounter]
				FinalCounter += 1
				LHCounter += 1

	return returnList
		

def QuickSort(A, low, high, flag):
	if low < high:
		pivot = A[0]
		for i in range(len(A)):


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
	return final

def main():
	starterList = generate_list(1000)
	defaultSorted = starterList[:]
	defaultSorted.sort()
	HashSorted = HashSort(starterList[:])
	if HashSorted != defaultSorted:
		print "Error in HashSort"
	MergeSorted = MergeSort(starterList[:])
	if MergeSorted != defaultSorted:
		print "Error in MergeSort"

main()
