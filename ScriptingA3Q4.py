"""
        Question 4: In this question we will be taking the grades of 25 Students
                    in 6 different classes while averaging them and sorting them
                    in descending order
"""
#Defining StudentInfo class
class StudentInfo():
#Defining the name and different classes
    def __init__(self, name, math, english, history, science, writing, gym):
        self.name = name
        self.math = math
        self.english = english
        self.history = history
        self.science = science
        self.writing = writing
        self.gym = gym
#Calculating the average of all classes
    def avg(self):
        self.average = (self.math + self.english + self.history + self.science + self.writing + self.gym)/6
        return self.average

#Defining the students array and putting in all the grades for each student
Students = []
Students.append(StudentInfo("Ethan",90 ,85 ,85 ,75 ,97 ,80))
Students.append(StudentInfo("Jam  ",70 ,65 ,70 ,78 ,56 ,87))
Students.append(StudentInfo("Tam  ",60 ,85 ,90 ,73 ,78 ,68))
Students.append(StudentInfo("Ham  ",80 ,82 ,89 ,90 ,87 ,82))
Students.append(StudentInfo("Ram  ",89 ,96 ,94 ,93 ,95 ,90))
Students.append(StudentInfo("Cam  ",80 ,81 ,89 ,80 ,90 ,90))
Students.append(StudentInfo("Bam  ",72 ,74 ,79 ,66 ,86 ,82))
Students.append(StudentInfo("Lam  ",82 ,85 ,86 ,90 ,95 ,80))
Students.append(StudentInfo("Jar  ",90 ,88 ,94 ,65 ,90 ,76))
Students.append(StudentInfo("Dar  ",93 ,84 ,79 ,93 ,84 ,86))
Students.append(StudentInfo("Bar  ",96 ,80 ,67 ,78 ,73 ,82))
Students.append(StudentInfo("Blam ",97 ,79 ,92 ,79 ,86 ,87))
Students.append(StudentInfo("Clam ",60 ,65 ,67 ,70 ,63 ,68))
Students.append(StudentInfo("Wam  ",96 ,90 ,94 ,92 ,90 ,87))
Students.append(StudentInfo("Slam ",90 ,85 ,84 ,75 ,78 ,80))
Students.append(StudentInfo("Man  ",80 ,83 ,94 ,89 ,84 ,88))
Students.append(StudentInfo("Jet  ",82 ,80 ,79 ,75 ,74 ,75))
Students.append(StudentInfo("Bert ",96 ,93 ,92 ,98 ,91 ,83))
Students.append(StudentInfo("Cod  ",89 ,85 ,83 ,88 ,82 ,85))
Students.append(StudentInfo("Dod  ",69 ,67 ,73 ,75 ,74 ,80))
Students.append(StudentInfo("Day  ",90 ,95 ,92 ,98 ,89 ,90))
Students.append(StudentInfo("Way  ",97 ,94 ,98 ,99 ,94 ,93))
Students.append(StudentInfo("Hay  ",92 ,90 ,82 ,73 ,92 ,83))
Students.append(StudentInfo("Slay ",92 ,80 ,84 ,85 ,90 ,81))
Students.append(StudentInfo("Bay  ",82 ,83 ,89 ,89 ,90 ,76))
Students.append(StudentInfo("John ",95 ,85 ,81 ,84 ,80 ,87))
Students.sort(key = lambda x: x.avg(), reverse = True)

print("Name", " M", " E", " H", " S", " W", " G", " AVG")
#Displaying the grades and average to the user
for j in Students:
    print(j.name, j.math,j.english,j.history,j.science,j.writing,j.gym, '%.2f' % j.avg())
#Calculating the averages for different classes and printing them
def printAvgs():
    mathAvg = 0
    for i in Students:
        mathAvg = mathAvg + i.math
    mathAvg = mathAvg/25

    engAvg = 0
    for i in Students:
        engAvg = engAvg + i.english
    engAvg = engAvg/25

    histAvg = 0
    for i in Students:
        histAvg = histAvg + i.history
    histAvg = histAvg/25

    scienceAvg = 0
    for i in Students:
        scienceAvg = scienceAvg + i.science
    scienceAvg = scienceAvg/25

    writingAvg = 0
    for i in Students:
        writingAvg = writingAvg + i.writing
    writingAvg = writingAvg/25

    gymAvg = 0
    for i in Students:
        gymAvg = gymAvg + i.gym
    gymAvg = gymAvg/25
    print("Averages for every class:")
    print("Math:",mathAvg, "English:", engAvg, "History:", histAvg, "Science:", scienceAvg, "Writing:", writingAvg, "Gym:", gymAvg)
printAvgs()
