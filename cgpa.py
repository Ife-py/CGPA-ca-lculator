import time
from colorama import Fore

logo = '''
   _____ _____ _____           _____          _      _____ _    _ _            _______ ____  _____  
  / ____/ ____|  __ \ /\      / ____|   /\   | |    / ____| |  | | |        /\|__   __/ __ \|  __ \ 
 | |   | |  __| |__) /  \    | |       /  \  | |   | |    | |  | | |       /  \  | | | |  | | |__) |
 | |   | | |_ |  ___/ /\ \   | |      / /\ \ | |   | |    | |  | | |      / /\ \ | | | |  | |  _  / 
 | |___| |__| | |  / ____ \  | |____ / ____ \| |___| |____| |__| | |____ / ____ \| | | |__| | | \ \ 
  \_____\_____|_| /_/    \_\  \_____/_/    \_|______\_____|\____/|______/_/    \_|_|  \____/|_|  \_\
                                                                                                    
'''

print(logo)

print('welcome to ife and humanx CGPA generator \n hope you are supplying the correct data')
print("Loading.....")
time.sleep(3)

course_delimeter = 0

a = int(input('enter your number of courses this semester: '))
#constants
total_units = 0
total_point = 0
points = 0
score= 0
tryings=0
for i in range(a):
    course_code = input("Enter your course: ")
    course_grade = input("Enter your grade: ")
    course_unit = int(input("Enter your units here: "))
    course_delimeter+=1
    print("you've calculated " + str(course_delimeter) +  " courses")
    print("##################################################################")
    total_units += course_unit
    if course_grade == "A":
        score = 5
        
    elif course_grade == "B":
        score = 4
   
    elif course_grade == "C":
        score = 3
        
    elif course_grade == "D":
        score = 2
        
    elif course_grade == "E":
        score = 1
        
    elif course_grade == "F":
        score = 0

    points += score
    first_point_generated= score * course_unit
    tryings += first_point_generated 
 
print(total_units) 
#point = course_unit * score
print(f"these are your points optained",points)  
Cgpa= tryings / total_units
print(Cgpa)
cgpa =float(tryings/ total_units)
print(cgpa)
print(f"your cgpa is",Cgpa )
#print(point)
classs = ""
if Cgpa >= 4.50:
	    classs = "First class"
elif Cgpa >= 3.50 and Cgpa<= 4.49:
	classs = "Second class upper"
elif Cgpa >= 2.40 and Cgpa <= 3.49:
		classs = "Second class lower"
else:
	classs = "Third class"
print("YOUR CGPA IS: " + str(round(Cgpa, 2)))
print("You got a " + classs + " there's still room for improvement")