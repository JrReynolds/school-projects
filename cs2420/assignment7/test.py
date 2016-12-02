def insertR(self, data, current):
    if data > current.data:
        if current.R is None:
            n = Node(data)
            current.R = n
            return True
        else:
            self.insertR(data, current.R)

    else:
        if current.L is None:
            n = Node(data)
            current.L = n
            return True
        else:
            self.insertR(data, current.L)
