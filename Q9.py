# Student Grade Calculator.This program calculates the final grade of a student
# based on three test scores It includes input validation, bonus logic, and
# grade determination.
#Test Case.

grade_1= int(input("Enter first test score:")) #integer
grade_2 = int(input("Enter second test score:")) #integer
grade_3 = int(input("Enter third test score:")) #integer


#Input..
if (grade_1 < 0 or grade_1 > 100) or (grade_2 < 0 or grade_2 > 100) or (grade_3 < 0 or grade_3 > 100):
    print("Error: All test scores must be between 0 and 100.")
else:

    average = (grade_1 + grade_2 + grade_3) / 3  #Calculate Average

       #Assign Grades.

    if average >= 90:
        grade = "A"
        message = "Excellent work!"
    elif average >= 80:
        grade = "B"
        message = "Great, Keep it up!"
    elif average >= 70:
        grade = "C"
        message = "Good effort,Keep improving."
    elif average >= 60:
        grade = "D"
        message = "Keep trying, push yourself hard"
    else:
        grade = "F"
        message = "Don't give up, study harder and do better next time."

if grade_1 >= 80 and grade_2 >= 80 and grade_3 >= 80: #Bonus logic
        average += 5
        print("Consistency bonus: +5 points")

        #OUTPUT RESULTS.

print("Average:", average)
print("Grade:", grade)
print(message)