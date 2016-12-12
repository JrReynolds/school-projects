import time
import Student
import hashtable


def timeSomething(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time() - start_time
    return end_time

def InsertAllStudents(A, filename):
    StudentFile = open(filename, "r")
    for line in StudentFile:
        # print line
        line = line.split()
        line[2] = line[2].split("-")
        line[2] = "".join(line[2])
        student = Student.Student(line[0], line[1], line[2], line[3], line[4])
        A.Insert(student)
    StudentFile.close()

def TraverseAllStudents(A):
    A.Traverse(TraverseAdd)
    print "Average Age: {}".format(gTotalAge/A.mSize)

def TraverseAdd(student):
    global gTotalAge
    gTotalAge += int(student.getAge())

def DeleteStudents(A, filename):
    DeleteFile = open(filename, "r")
    for line in DeleteFile:
        line = line.split()
        line = line[0]
        line = line.split("-")
        line = "".join(line)
        A.Delete(line)
    DeleteFile.close()

def RetrieveNames(A, filename):
    RetrieveFile = open(filename, "r")
    ageTotal = 0.0
    countTotal = 0.0
    for line in RetrieveFile:
        retrVal = line.split()
        retrVal = retrVal[0]
        retrVal = retrVal.split("-")
        retrVal = "".join(retrVal)
        ans = A.Retrieve(retrVal)
        if ans:
            ageTotal += int(ans.getAge())
            countTotal += 1
    print "Average Age of Retrieved: {}".format(ageTotal/countTotal)

    RetrieveFile.close()

gTotalAge = 0.0

def main():
    # a = Student.Student("Henry", "Jones", "123-45-7899", "indianajones@awesome.com", "40")
    # b = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    # c = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    #
    # database = bst.BST()
    # database.Insert(a)
    # database.Insert(b)
    # database.Insert(c)

    database = hashtable.HashTable(30000)
    print "Insert Duration: " + str(timeSomething(InsertAllStudents, database, "InsertNames.txt"))
    print "Traverse Duration: " + str(timeSomething(TraverseAllStudents, database))
    print "Delete Duration: " + str(timeSomething(DeleteStudents, database, "DeleteNames.txt"))
    print "Retrieve Duration: " + str(timeSomething(RetrieveNames, database, "RetrieveNames.txt"))

print "Main Duration: " + str(timeSomething(main))