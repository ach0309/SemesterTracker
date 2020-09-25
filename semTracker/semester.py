from course import *


class SemesterTracker:
    def __init__(self, semester):
        self.semester = semester
        self.courses = []

    def addCourse(self, name, prof, hwPercent, projPercent, examPercent, quizPercent, credit):
        percentages = Percent(hwPercent, projPercent, examPercent, quizPercent)
        currentCourse = Course(name, prof, percentages, credit)
        self.courses.append(currentCourse)

# total class grade to equivalent letterGrade
    def letterGrade(self, totalGrade):
        lg = ""
        if totalGrade >= 94 and totalGrade <=100:
            lg = "A"
        if totalGrade  >= 90 and totalGrade <=93:
            lg = "A-"
        if totalGrade  >= 87 and totalGrade <=89:
            lg = "B+"
        if totalGrade  >= 83 and totalGrade <=86:
            lg = "B"
        if totalGrade  >= 80 and totalGrade <=83:
            lg = "B-"
        if totalGrade  >= 77 and totalGrade <=79:
            lg = "C+"
        if totalGrade  >= 73 and totalGrade <=76:
            lg = "C"
        if totalGrade  >= 70 and totalGrade <=72:
            lg = "C-"
        if totalGrade  >= 67 and totalGrade <=79:
            lg = "D+"
        if totalGrade  >= 60 and totalGrade <=66:
            lg = "D"
        if totalGrade  >= 0 and totalGrade <=59:
            lg = "F"
        return lg

# letterGrade to equivalent gpa
    def gpaFormat(self, letterGrade):
        score = 0
        if letterGrade == "A" or letterGrade =="a":
            score += 4.0
        if letterGrade == "A-" or letterGrade == "a-":
            score += 3.7
        if letterGrade == "B+" or letterGrade == "b+":
            score += 3.3
        if letterGrade == "B" or letterGrade == "b":
            score += 3.0
        if letterGrade == "B-" or letterGrade == "b-":
            score += 2.7
        if letterGrade == "C+" or letterGrade == "c-":
            score += 2.3
        if letterGrade == "C" or letterGrade == "c":
            score += 2
        if letterGrade == "C-" or letterGrade == "c-":
            score += 1.7
        if letterGrade == "D+" or letterGrade == "d+":
            score += 1.3
        if letterGrade == "D" or letterGrade == "d":
            score += 1
        if letterGrade == "D-" or letterGrade == "d-":
            score += 0.7
        if letterGrade == "F" or letterGrade == "f":
            score += 0
        return score

# add respective APEQ to the specific course
    def addHwToCourse(self, course, num, grade):
        for item in self.courses:
            if item.name == course:
                item.add_hw(num, grade)
    def addQuizToCourse(self, course, num, grade):
        for item in self.courses:
            if item.name == course:
                item.add_quiz(num, grade)
    def addProjToCourse(self, course, num, grade):
        for item in self.courses:
            if item.name == course:
                item.add_proj(num, grade)
    def addExamsToCourse(self, course, num, grade):
        for item in self.courses:
            if item.name == course:
                item.add_exam(num, grade)

    def finalGPA(self):
        finGPA=0
        totCredit = 0
        for item in self.courses:
            letter = self.letterGrade(item.totalGrade()) #get totalgrade and convert to lettergrade
            totCredit += item.credit #total credits for the semester
            finGPA += (self.gpaFormat(letter) * item.credit)# letterGrade to gpa * credir, add to final gpa for all courses
        return "{:.2f}".format((finGPA/totCredit)) #returns the gpa for the semester


    def finalReport(self):
        for course in self.courses:
            classGrade = course.totalGrade()
            print(str(course.name) + ":" + str(classGrade) + "  " + str(self.letterGrade(classGrade)))
        print("Final GPA for " + self.semester + ": " + str(self.finalGPA()))

