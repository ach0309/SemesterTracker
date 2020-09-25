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
        for item in self.courses: #calculate the gpa
            letter = self.letterGrade(item.totalGrade()) #get totalgrade and convert to lettergrade
            totCredit += item.credit #total credits
            finGPA += (self.gpaFormat(letter) * item.credit)# letterGrade to gpa and add to final gpa for all the courses with credit included
        return "{:.2f}".format((finGPA/totCredit)) #returns the gpa for the semester

# course gpa * credits / (total number of credits of all classes)

    def finalReport(self):
        for course in self.courses:
            classGrade = course.totalGrade()
            print(str(course.name) + ":" + str(classGrade) + "  " + str(self.letterGrade(classGrade)))
        print("Final GPA for " + self.semester + ": " + str(self.finalGPA()))


# add all grades for all courses in sem
# final report on all classes in the semester

if __name__ == "__main__":
    sem_1 = SemesterTracker("Fall2020")
    sem_1.addCourse("3000", "Cody Turner", 0.3, 0.2, 0.3,0.2, 1)
    sem_1.addCourse("3504", "Reda Ammar", 0.25, 0.25, 0.25,0.25, 3)
    sem_1.addCourse("4502", "Raj Sanguthevar", 0.3, 0.25, 0.3,0.15, 3)

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
