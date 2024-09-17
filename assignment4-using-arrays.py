rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]

studentArr = ["mayank", "pratik", "sagar", "yash", "jay"]
subjectArr = ["maths", "physics", "chemistry", "marathi", "english"]

totalStudents = 0

arr[0] = [90, 65, 79, 76, 93]
arr[1] = [56, 95, 59, 66, 77]
arr[2] = [66, 77, 99, 73, 93]
arr[3] = [60, 65, 69, 66, 87]
arr[4] = [87, 86, 86, 65, 88]


def printStudents():
    j = 0
    for row in arr:
        print(studentArr[j], end=" ")
        for i in range(0, 5):
            print(row[i], end=" ")
        print()
        j = j + 1


def subjectAverage(subject):
    sum = 0
    for i in range(0, 5):
        if subject == subjectArr[i]:
            for row in arr:
                sum = sum + row[i]
            average = sum / len(studentArr)
            # print("average of subject",subject,"=",average)
            return average
    print("subject not found")
    return


def highestAverage():
    highestSubject = subjectArr[0]
    highestAverage = subjectAverage(subjectArr[0])
    for i in range(1, 5):
        average = subjectAverage(subjectArr[i])
        if average > highestAverage:
            highestAverage = average
            highestSubject = subjectArr[i]
    print("highest average:", highestAverage)
    print("subject with highest average:", highestSubject)
    return highestSubject


def highestScore():
    sum = 0
    highestSudent = ''
    HighestAverage = 0
    for row in arr:
        for mark in row:
            sum = sum + mark
        studentAverage = sum / len(subjectArr)
        if studentAverage > HighestAverage:
            highestAverage = studentAverage
    print(highestAverage)


# subjectAverage("chemistry")
highestAverage()


def menu():
    print("enter choice")
    print("1. add student")
    print("2. calculate average grade of subject")
    print("3. student with highest grade")
    print("4. subject with highest average grade")



