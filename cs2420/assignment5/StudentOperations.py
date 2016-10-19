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

def TraverseStudent(student, total):
    total += student.getAge()
    return total

def TraverseAllStudents(A):
    total = 0.0
    for student in A:
        total = TraverseStudent(student, total)
    print "Average Age: " + str(total/len(A))


def main():
    # a = Student.Student("Henry", "Jones", "123-45-7899", "indianajones@awesome.com", "40")
    # b = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    # c = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    # print a == b
    # print b == c
    #
    # database = []
    # InsertStudent(database, a)
    # InsertStudent(database, b)
    # InsertStudent(database, c)

    database = []
    print "Insert Duration: " + str(timeSomething(InsertAllStudents, (database, "InsertNames.txt")))
    avgAge = TraverseAllStudents(database)





print "Main Duration: " + str(timeSomething(main))