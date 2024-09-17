

def subjectAverage(sparse_grades, noOfStudents, noOfGrades):
    subject_totals = [0] * noOfGrades
    subject_counts = [0] * noOfGrades

    for (student, subject), marks in sparse_grades.items():
        subject_totals[subject] += marks
        subject_counts[subject] += 1

    subject_averages = [0] * noOfGrades

    for i in range(0,noOfGrades):
        subject_averages[i]=subject_totals[i]/subject_counts[i]
    return  subject_averages

# def highestScore(sparse_grades, studentArr , subjectArr):

def main():
    grades = [
        [0, 56, 54, 66],
        [85, 0, 0, 0],
        [0, 0, 78, 92],
        [89, 0, 88, 0]
    ]

    noOfStudents = len(grades)
    noOfGrades = len(grades[0])
    studentArr = ["mayank", "pratik", "sagar", "yash"]
    subjectArr = ["maths", "physics", "chemistry", "marathi"]

    sparse_grades = {}
    for i in range(len(grades)):
        for j in range(len(grades[i])):
            if grades[i][j] != 0:
                sparse_grades[(i, j)] = grades[i][j]

    print(sparse_grades)

    subject_averages = subjectAverage(sparse_grades,noOfStudents,noOfGrades)

    print(subject_averages)


main()