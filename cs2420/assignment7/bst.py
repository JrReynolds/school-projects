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
                self.mSize += 1
                return True
            else:
                print "ERROR: Duplicate entry detected, omitting {}".format(data)
                return False

    def InsertR(self, data, current):
        if current.data > data:
            if current.L is None:
                n = Node(data)
                current.L = n
            else:
                self.InsertR(data, current.L)

        else:
            if current.R is None:
                n = Node(data)
                current.R = n
            else:
                self.InsertR(data, current.R)

    def Traverse(self, callback, *args):



def main():
    database = BST()
    database.Insert(11)
    database.Insert(12)
    database.Insert(11)
    print database.TrueSize()

main()
