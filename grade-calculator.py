#Total credit
#Hours
semesterOneHours = 13
semesterTwoHours = 12
semesterThreeHours = 14

#GPA
semesterOneGpa = 3.28
semesterTwoGpa = 4.00
semesterThreeGpa = 3.45

#Total credit point & hours
semesterOnePoint = semesterOneGpa * semesterOneHours
semesterTwoPoint = semesterTwoGpa * semesterTwoHours
semesterThreePoint = semesterThreeGpa * semesterThreeHours

totalCreditPoints = semesterOnePoint + semesterTwoPoint + semesterThreePoint
totalCreditHours = semesterOneHours+semesterTwoHours+semesterThreeHours

#calculating cGPA
cgpa = totalCreditPoints/totalCreditHours

print("Your cGPA is:", round(cgpa, 2))