from semester import *

if __name__ == "__main__":
    sem_1 = SemesterTracker("Fall2020")
    sem_1.addCourse("Physics", "AAAA", 0.3, 0.2, 0.3,0.2, 1)
    sem_1.addCourse("Calculus", "BBBB", 0.25, 0.25, 0.25,0.25, 3)
    sem_1.addCourse("Intro to Engineering", "CCCC", 0.3, 0.25, 0.3,0.15, 3)

    sem_1.addHwToCourse("3000", 1, 90)
    sem_1.addHwToCourse("3000", 2, 100)
    sem_1.addExamsToCourse("3000", 1, 100)
    sem_1.addExamsToCourse("3000", 2, 50)
    sem_1.addProjToCourse("3000", 1, 100)
    sem_1.addProjToCourse("3000", 2, 50)
    sem_1.addQuizToCourse("3000", 1, 100)
    sem_1.addQuizToCourse("3000", 2, 50)

    sem_1.addHwToCourse("3504", 1, 65)
    sem_1.addHwToCourse("3504", 2, 90)
    sem_1.addExamsToCourse("3504", 1, 52)
    sem_1.addExamsToCourse("3504", 2, 85)
    sem_1.addProjToCourse("3504", 1, 91)
    sem_1.addProjToCourse("3504", 2, 93)
    sem_1.addQuizToCourse("3504", 1, 87)
    sem_1.addQuizToCourse("3504", 2, 96)

    sem_1.addHwToCourse("4502", 1, 92)
    sem_1.addHwToCourse("4502", 2, 93)
    sem_1.addExamsToCourse("4502", 1, 95)
    sem_1.addExamsToCourse("4502", 2, 85)
    sem_1.addProjToCourse("4502", 1, 91)
    sem_1.addProjToCourse("4502", 2, 93)
    sem_1.addQuizToCourse("4502", 1, 87)
    sem_1.addQuizToCourse("4502", 2, 96)


    sem_1.finalReport()

'''
for course.py tests 


course_1_percentages = Percent( .2, .2, .3, .3)
course_1 = Course('Senior Design', 'Johnson', course_1_percentages)
course_2 = Course('CSE1010', 'Bradford', course_1_percentages)

course_1.add_hw(1, 100)
course_1.add_hw(2, 50)

course_1.add_exam(1, 100)
course_1.add_exam(2, 50)

course_1.add_proj(1, 200)
course_1.add_proj(2, 30)

course_1.add_quiz(1, 200)
course_1.add_quiz(2, 30)


print(course_1.examWeight())
print(course_1.assignWeight())
print(course_1.projWeight())
print(course_1.quizWeight())
print(course_1.totalGrade())
'''