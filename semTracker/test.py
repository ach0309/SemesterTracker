from semester import *

if __name__ == "__main__":
    sem_1 = SemesterTracker("Fall2020")
    sem_1.addCourse("Physics", "AAAA", 0.3, 0.2, 0.3,0.2, 1)
    sem_1.addCourse("Calculus", "BBBB", 0.25, 0.25, 0.25,0.25, 3)
    sem_1.addCourse("Intro to Engineering", "CCCC", 0.3, 0.25, 0.3,0.15, 3)

    sem_1.addHwToCourse("Physics", 1, 90)
    sem_1.addHwToCourse("Physics", 2, 100)
    sem_1.addExamsToCourse("Physics", 1, 100)
    sem_1.addExamsToCourse("Physics", 2, 50)
    sem_1.addProjToCourse("Physics", 1, 100)
    sem_1.addProjToCourse("Physics", 2, 50)
    sem_1.addQuizToCourse("Physics", 1, 100)
    sem_1.addQuizToCourse("Physics", 2, 50)

    sem_1.addHwToCourse("Calculus", 1, 65)
    sem_1.addHwToCourse("Calculus", 2, 90)
    sem_1.addExamsToCourse("Calculus", 1, 52)
    sem_1.addExamsToCourse("Calculus", 2, 85)
    sem_1.addProjToCourse("Calculus", 1, 91)
    sem_1.addProjToCourse("Calculus", 2, 93)
    sem_1.addQuizToCourse("Calculus", 1, 87)
    sem_1.addQuizToCourse("Calculus", 2, 96)

    sem_1.addHwToCourse("Intro to Engineering", 1, 92)
    sem_1.addHwToCourse("Intro to Engineering", 2, 93)
    sem_1.addExamsToCourse("Intro to Engineering", 1, 95)
    sem_1.addExamsToCourse("Intro to Engineering", 2, 85)
    sem_1.addProjToCourse("Intro to Engineering", 1, 91)
    sem_1.addProjToCourse("Intro to Engineering", 2, 93)
    sem_1.addQuizToCourse("Intro to Engineering", 1, 87)
    sem_1.addQuizToCourse("Intro to Engineering", 2, 96)


    sem_1.finalReport()

'''
for course.py tests 


course_1_percentages = Percent( .2, .2, .3, .3)
course_1 = Course('SDP', 'AAAAA', course_1_percentages)
course_2 = Course('CSE', 'BBBB', course_1_percentages)

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