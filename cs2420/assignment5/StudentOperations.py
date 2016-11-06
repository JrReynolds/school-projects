import time
import Student


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
        InsertStudent(A, student)
    StudentFile.close()



def TraverseAllStudents(A):
    total = 0.0
    for student in A:
        total += int(student.getAge())
    print "Average Age: " + str(total/len(A))


def RemoveStudent(A, ssn):
    if ssn in A:
        A.remove(ssn)
    else:
        print "ERROR: Student {} not found in database".format(ssn)

def DeleteStudents(A, filename):
    DeleteFile = open(filename, "r")
    for line in DeleteFile:
        line = line.split()
        RemoveStudent(A, line[0])
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
        line = line.split()
        retAge = int(PullName(A, line[0]))
        if retAge != 0:
            ageTotal += retAge
            countTotal += 1
    print "Average Age of Retrieved: {}".format(ageTotal/countTotal)

    RetrieveFile.close()


def main():
    # a = Student.Student("Henry", "Jones", "123-45-7899", "indianajones@awesome.com", "40")
    # b = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    # c = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    #
    # database = []
    # InsertStudent(database, a)
    # InsertStudent(database, b)
    # InsertStudent(database, c)
    #
    # print str(PullName(database, "123-45-7899"))
    # print database

    database = []
    print "Insert Duration: " + str(timeSomething(InsertAllStudents, database, "InsertNames.txt"))
    print "Traverse Duration: " + str(timeSomething(TraverseAllStudents, database))
    print "Delete Duration: " + str(timeSomething(DeleteStudents, database, "DeleteNames.txt"))
    print "Retrieve Duration: " + str(timeSomething(RetrieveNames, database, "RetrieveNames.txt"))





print "Main Duration: " + str(timeSomething(main))