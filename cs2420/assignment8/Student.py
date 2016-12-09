class Student:
    def __init__(self, fname, lname, ssn, email, age):
        self.mFName = fname
        self.mLName = lname
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age

    def __int__(self):
        ssn = self.getSSN()
        ssn = ssn.split("-")
        ssn = int("".join(ssn))
        return int(ssn)

    def __eq__(self, other): #if slow check here
        if isinstance(other, Student):
            return self.mSSN == other.mSSN
        elif isinstance(other, str):
            return self.mSSN == other

    def __contains__(self, other):
        return self==other

    def __str__(self):
        return "{} {} ({})".format(self.getFName(), self.getLName(), self.getSSN())

    def __gt__(self, other):
        if isinstance(other, Student):
            a = int(self)
            b = int(other)
            return a > b
        elif isinstance(other, str):
            a = int(self)
            b = other.split("-")
            b = int("".join(b))
            return a > b

    def __lt__(self, other):
        if isinstance(other, Student):
            a = int(self)
            b = int(other)
            return a < b
        elif isinstance(other, str):
            a = int(self)
            b = other.split("-")
            b = int("".join(b))
            return a < b


    # __int__ = intify


    def getSSN(self):
        return self.mSSN

    def getFName(self):
        return self.mFName

    def getLName(self):
        return self.mLName

    def getAge(self):
        return self.mAge
