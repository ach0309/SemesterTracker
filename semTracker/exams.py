class Exam:
    def __init__(self, num, grade):
        self.num = num
        self.grade = grade

    def assignInfo(self):
        a_info = "Exam #" + str(self.num) + ": " + str(self.grade) + "%"
        return a_info

    def __str__(self):
        return str(self.grade)

    def toPercent(self, score, total):
        grade = ( score/total ) * 100
        return "{:.2f}".format(grade)



