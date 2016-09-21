import random

def generate_list(length):
	list1 = []
	for i in range(length):
		list1.append(random.randint(0, length-1))
	return list1

def MergeSort(A):
	pass

def QuickSort(A, flag):
	pass

def HashSort(A):
	new = []
	for i in A:
		new.append(0)
	for i in A:
		new[i] += 1
	final = []
	for i in range(len(new)):
		for j in range(i):
			final.append(A[i])
	return final

def main():
	starterList = generate_list(10)
	defaultSorted = starterList[:]
	defaultSorted.sort()
	print starterList
	print defaultSorted
	HashSorted = HashSort(starterList[:])
	print HashSorted

main()
