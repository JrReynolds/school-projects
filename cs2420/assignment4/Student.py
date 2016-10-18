class Student:
    def __init__(self, fname, lname, ssn, email, age):
        self.mFName = fname
        self.mLName = lname
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.mSSN == other.mSSN
        elif isinstance(other, str):
            return self.mSSN == other

    def getSSN(self):
        return self.mSSN

    def getFName(self):
        return self.mFName

    def getLName(self):
        return self.mLName