import math
import random



class HashTable:
    def __init__(self, size):
        s2 = size*2+1
        while not self.isPrime(s2):
            s2+=2
        self.mTable = [None] * s2
        self.mSize = 0
        self.mTableSize = s2

    def isPrime(self, n):
        n = float(n)
        root = math.ceil(math.sqrt(n))
        if root % 2 == 0:
            root += 1
        for i in range(int(root), 1, -2):
            if n/i == int(n/i):
                return False
        return True

    def Exists(self, data):
        initIndex = int(data) % self.mTableSize
        index = initIndex
        while self.mTable[index] is not None:
            if self.mTable[index] is not False and self.mTable[index] == data:
                return True
            index += 1
            if index == self.mTableSize:
                index = 0
            if index == initIndex:
                return False
        return False

    def Insert(self, data):
        if self.Exists(data):
            print "ERROR: Duplicate Object {}".format(data)
            return False
        index = int(data) % self.mTableSize
        while self.mTable[index] is not None and self.mTable[index] != False:
            index += 1
            if index >= self.mTableSize:
                index = 0
        self.mTable[index] = data
        self.mSize += 1

    def Traverse(self, callback, *args):
        for i in self.mTable:
            if i is not None and i != False:
                callback(i, *args)

    def Retrieve(self, data):
        if self.Exists(data):
            initIndex = int(data) % self.mTableSize
            index = initIndex
            while self.mTable[index] is not None:
                if self.mTable[index] is not False and self.mTable[index] == data:
                    return self.mTable[index]
                index += 1
                if index == self.mTableSize:
                    index = 0
                if index == initIndex:
                    return False
            return False
    def Delete(self, data):
        if self.Exists(data):
            initIndex = int(data) % self.mTableSize
            index = initIndex
            while not self.mTable[index] == data or self.mTable[index] is None:
                index += 1
                if index == self.mTableSize:
                    index = 0
                if index == initIndex:
                    return False
            if self.mTable[index] == data:
                self.mTable[index] = False
                self.mSize -= 1

def main():
    HT = HashTable(300000)
    HT.Insert(11)
    HT.Insert(11)
    HT.Insert(72)
    print HT.Retrieve(72)
    print HT.mSize
    HT.Delete(11)
    print HT.Exists(11)
    HT.Delete(72)
    print HT.Exists(72)
    print HT.mSize
    for i in range(300000):
        HT.Insert(random.randrange(0,999999999))
    print HT.mSize
    print HT.mTableSize





# main()
