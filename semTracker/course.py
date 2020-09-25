from assign import *
from exams import *
from projects import *
from quiz import *
from percent import *

class Course:
    def __init__(self, name, prof, percentages, credit):
        self.name = name    # same as
        self.prof = prof    # course_1 = Course() -- instance
        self.percentages = percentages  # course_1.name = "Data Structures"
        self.hw = []
        self.proj = []
        self.exams = []
        self.quiz = []
        self.credit = credit


    def course_info(self):
        c_info = "This class is " + self.name + " with Prof. " \
                 + self.prof + "."
        return c_info

# add APEQ(assign, proj, exams, quiz) on respective lists
    def add_hw(self, num, grade):
        newAssign = Assign(num, grade)
        self.hw.append(newAssign)

    def add_exam(self, num, grade):
        newExam = Exam(num, grade)
        self.exams.append(newExam)

    def add_proj(self, num, grade):
        newProj= Proj(num, grade)
        self.proj.append(newProj)

    def add_quiz(self, num, grade):
        newQuiz= Quiz(num, grade)
        self.quiz.append(newQuiz)



#calculate weight of APEQ by final APEQ grade times percentage
    def quizWeight(self):
        total = 0
        count=0
        final=0
        for i in self.quiz:
            total+= i.grade
            count +=1
        final = (total / count)
        return final * self.percentages.Pquiz

    def projWeight(self):
        total = 0
        count=0
        final=0
        for i in self.proj:
            total+= i.grade
            count +=1
        final = (total / count)
        return final * self.percentages.Pproj

    def assignWeight(self):
        total = 0
        count=0
        final=0
        for i in self.hw:
            total+= i.grade
            count +=1
        final = (total / count)
        return final * self.percentages.Phw

    def examWeight(self):
        total = 0
        count=0
        final=0
        for i in self.exams:
            total+= i.grade
            count +=1
        final = (total / count)
        return final * self.percentages.Pexam


#final course weighted grade
    def totalGrade(self):
        return self.examWeight() + self.assignWeight() + self.projWeight() + self.quizWeight()




'''

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


'''   
    def del_hw(self, num):
        for i in self.hw:
            if i == num:
                self.hw.remove(i)
            return "try again"
'''
