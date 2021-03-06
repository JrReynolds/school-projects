import time
import Student
import bst


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
    for line in StudentFile:
        line = line.split()
        student = Student.Student(line[0], line[1], line[2], line[3], line[4])
        A.Insert(student)
    StudentFile.close()



def TraverseAllStudents(A):
    A.Traverse(TraverseAdd)
    print gAgeTotal/A.getTrueSize()


def TraverseAdd(student):
    global gAgeTotal
    gAgeTotal += student.getAge()

def RemoveStudent(A, ssn):
    if ssn in A:
        A.remove(ssn)
    else:
        print "ERROR: Student {} not found in database".format(ssn)

def DeleteStudents(A, filename):
    DeleteFile = open(filename, "r")
    for line in DeleteFile:
        line = line.split()
        A.Delete(line[0])
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
        ans = A.Retrieve(line.strip())
        if ans:
            ageTotal += int(ans.getAge())
            countTotal += 1
    print "Average Age of Retrieved: {}".format(ageTotal/countTotal)

    RetrieveFile.close()

gAgeTotal = 0.0

def main():
    # a = Student.Student("Henry", "Jones", "123-45-7899", "indianajones@awesome.com", "40")
    # b = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    # c = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    #
    # database = bst.BST()
    # database.Insert(a)
    # database.Insert(b)
    # database.Insert(c)


    database = bst.BST()
    print "Insert Duration: " + str(timeSomething(InsertAllStudents, database, "InsertNames.txt"))
    global gAgeTotal
    print "Traverse Duration: " + str(timeSomething(TraverseAllStudents, database))
    print "Delete Duration: " + str(timeSomething(DeleteStudents, database, "DeleteNames.txt"))
    print "Retrieve Duration: " + str(timeSomething(RetrieveNames, database, "RetrieveNames.txt"))








print "Main Duration: " + str(timeSomething(main))