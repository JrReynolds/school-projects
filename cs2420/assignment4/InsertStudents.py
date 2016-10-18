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

def main():
    a = Student.Student("Henry", "Jones", "123-45-7899", "indianajones@awesome.com", "40")
    b = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    c = Student.Student("Anakin", "Skywalker", "357-89-7642", "darthvader@darkside.com", "30")
    print a == b
    print b == c

    database = []
    InsertStudent(database, a)
    InsertStudent(database, b)
    InsertStudent(database, c)

main()