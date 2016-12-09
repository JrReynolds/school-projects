import time
import Student
import hashtable


def timeSomething(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time() - start_time
    return end_time

def InsertStudent(A, student):
    if student.getSSN() in A:
        print "ERROR: Student {} {} (SSN {}) already in database".format(student.getFName(), student.getLName(), student.getSSN())
    else:
        A.append(student)


def InsertAllStudents(A, filename):
    StudentFile = open(filename, "r")
    print "Open File (Insert)"
    for line in StudentFile:
        # print line
        line = line.split()
        student = Student.Student(line[0], line[1], line[2], line[3], line[4])
        A.Insert(student)
    StudentFile.close()



def TraverseAllStudents(A):
    total = 0.0
    total += A.Traverse(TraverseAdd, total)
    print total


def TraverseAdd(student, total):
    total += int(student.getAge())
    return total

def RemoveStudent(A, ssn):
    if ssn in A:
        A.remove(ssn)
    else:
        print "ERROR: Student {} not found in database".format(ssn)

def DeleteStudents(A, filename):
    DeleteFile = open(filename, "r")
    for line in DeleteFile:
        line = line.split()
        line = line[0]
        line = line.split("-")
        line = "".join(line)
        A.Delete(line)
    DeleteFile.close()

def PullName(A, ssn):
    if ssn in A:
        at = A.index(ssn)
        return A[at].getAge()
    else:
        print "ERROR: Student {} not found in database".format(ssn)
        return 0

def RetrieveNames(A, filename):
    RetrieveFile = open(filename, "r")
    ageTotal = 0.0
    countTotal = 0.0
    for line in RetrieveFile:
        retrVal = line.split()
        retrVal = retrVal[0]
        retrVal = retrVal.split("-")
        retrVal = "".join(retrVal)
        print retrVal
        ans = A.Retrieve(retrVal)
        print ans
        if ans:
            ageTotal += int(ans.getAge())
            countTotal += 1
    print "Average Age of Retrieved: {}".format(ageTotal/countTotal)

    RetrieveFile.close()


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
    # print "Traverse Duration: " + str(timeSomething(TraverseAllStudents, database))
    print "Delete Duration: " + str(timeSomething(DeleteStudents, database, "DeleteNames.txt"))
    print "Retrieve Duration: " + str(timeSomething(RetrieveNames, database, "RetrieveNames.txt"))








print "Main Duration: " + str(timeSomething(main))