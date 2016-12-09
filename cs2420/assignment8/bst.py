class Node:
    def __init__(self, data):
        self.data = data
        self.L = None
        self.R = None

class BST:
    def __init__(self):
        self.mRoot = None
        self.mSize = 0

    def Exists(self, data, retflag=False):
        ans = self.ExistsR(data, self.mRoot, retflag)
        return ans

    def ExistsR(self, data, current, retflag):
        if current is None:
            return False
        elif current.data == data:
            if retflag:
                return current
            else:
                return True
        else:
            if current.data > data:
                ans = self.ExistsR(data, current.L, retflag)
            else:
                ans = self.ExistsR(data, current.R, retflag)
            return ans

    def Insert(self, data):
        if self.mRoot is None:
            self.mRoot = Node(data)
            self.mSize += 1
            return True
        else:
            if not self.Exists(data):
                self.InsertR(data, self.mRoot)
                return True
            else:
                print "ERROR: Duplicate entry detected, omitting {}".format(data)
                return False

    def InsertR(self, data, current):
        if current.data > data:
            if current.L is None:
                n = Node(data)
                current.L = n
                # print "Entry {} inserted".format(data)
            else:
                self.InsertR(data, current.L)

        else:
            if current.R is None:
                n = Node(data)
                current.R = n
                # print "Entry {} inserted".format(data)
            else:
                self.InsertR(data, current.R)

    def Traverse(self, callback, *args):
        a = self.TraverseR(self.mRoot, callback, *args)
        return a

    def TraverseR(self, current, callback, *args):
        if current is not None:
            a = callback(current.data, *args)
            if current.L is not None:
                self.TraverseR(current.L, callback, *args)
            if current.R is not None:
                self.TraverseR(current.R, callback, *args)
            return a
        else:
            return False

    def Delete(self, data):
        if self.Exists(data):
            self.mRoot = self.DeleteR(data, self.mRoot)
            return True
        else:
            print "ERROR: Entry not found {}".format(data)
            return False

    def DeleteR(self, data, current):
        if data < current.data:
            current.L = self.DeleteR(data, current.L)

        elif data > current.data:
            current.R = self.DeleteR(data, current.R)

        else:
            if not current.L and not current.R:
                current = None
            elif current.L is None:
                current = current.R
            elif current.R is None:
                current = current.L
            else:
                s = current.R
                while s.L:
                    s = s.L
                current.data = s.data
                current.R = self.DeleteR(s.data, current.R)

        return current

    def Retrieve(self, data):
        a = self.Exists(data, True)
        if a:
            return a.data
        else:
            return False

gTotal = 0
def AddItems(s):
    global gTotal
    gTotal += s
    
def PrintItems(s):
    print s

def main():
    global gTotal
    database = BST()
    data = [20, 10, 30, 5, 25, 40, 2, 8, 23, 27, 45, 42, 22]
    for i in data:
        database.Insert(i)
    database.Delete(42)
    print database.Exists(42)
    database.Delete(30)
    print database.Exists(30)
    database.Delete(40)
    print database.Exists(40)
    database.Delete(23)
    print database.Exists(23)
    gTotal = 0
    database.Traverse(AddItems)
    print "gTotal is",gTotal
    retData = [20, 5, 8, 30]
    total = 0
    for i in retData:
        a = database.Retrieve(i)
        if a:
            total += a
    print total

main()
