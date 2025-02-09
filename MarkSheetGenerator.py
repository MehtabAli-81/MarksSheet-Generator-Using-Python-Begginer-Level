# BASIC MARKSHEET GENERATOR BACKEND PROJECT USING PYTHON

# INPUT SECTION
print("------------------------------------------------------------")
print("                         DETAILS                            ")
print("------------------------------------------------------------")
Name = input("ENTER YOUR NAME: ")
RollNumber = int(input("ENTER YOUR ROLL NUMBER: "))
Class = int(input("ENTER YOUR CLASS: "))

print("------------------------------------------------------------")
print("                 ENTER SUBJECT WISE MARKS.                  ")
print("------------------------------------------------------------")

# Taking subject-wise marks input
Mark01 = int(input("MATHEMATICS MARKS: "))
Mark02 = int(input("ENGLISH MARKS: "))
Mark03 = int(input("COMPUTER MARKS: "))
Mark04 = int(input("PHYSICS MARKS: "))
Mark05 = int(input("CHEMISTRY MARKS: "))
Mark06 = int(input("SOCIAL STUDY MARKS: "))
Mark07 = int(input("HISTORY MARKS: "))

# Total Marks and Percentage Calculation
Total = Mark01 + Mark02 + Mark03 + Mark04 + Mark05 + Mark06 + Mark07
Percentage = (Total / 700) * 100

# Function to determine pass or fail for each subject
def subject_status(marks):
    return "Pass" if marks >= 40 else "Fail"

# Determine overall pass or fail based on percentage
OverallResult = "Pass" if Percentage >= 50 else "Fail"

# OUTPUT SECTION
print("---------------------------------------------------------------")
print("                          MARKSHEET                          ")
print("---------------------------------------------------------------")
print("FULL NAME    : ", Name)
print("ROLL NUMBER  : ", RollNumber)
print("CLASS        : ", Class)
print("----------------------------------------------------------------")
print("SUBJECT          MAXIMUM MARKS      MARKS OBTAINED      STATUS")
print("----------------------------------------------------------------")
print(f"MATHEMATICS    -     100         -       {Mark01}        -      {subject_status(Mark01)}")
print(f"ENGLISH        -     100         -       {Mark02}        -      {subject_status(Mark02)}")
print(f"COMPUTER       -     100         -       {Mark03}        -      {subject_status(Mark03)}")
print(f"PHYSICS        -     100         -       {Mark04}        -      {subject_status(Mark04)}")
print(f"CHEMISTRY      -     100         -       {Mark05}        -      {subject_status(Mark05)}")
print(f"SOCIAL STUDY   -     100         -       {Mark06}        -      {subject_status(Mark06)}")
print(f"HISTORY        -     100         -       {Mark07}        -      {subject_status(Mark07)}")
print("--------------------------------------------------------------")
print(f"TOTAL MARKS    -     700         -       {Total} ")
print(f"PERCENTAGE     -                 -       {Percentage:}% ")
print(f"RESULT         -                 -       {OverallResult} ")
print("--------------------------------------------------------------")
print("                       THANK YOU                              ")
print("--------------------------------------------------------------")