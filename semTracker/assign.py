class Assign:
    def __init__(self, num, grade):
        self.num = num
        self.grade = grade

    def assignInfo(self):
        a_info = "Assignment #" + str(self.num) + ": " + str(self.grade) + "%"
        return a_info

    def __str__(self):
        return str(self.grade)

#    def toPercent(self, score, total):
#        grade = ( score/total ) * 100
#        return "{:.2f}".format(grade)



#print(assignInfo.toPercent(45, 50))
