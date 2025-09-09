#Benjamin Gonzales
#CH2 Practice Prg1
#This application will calculate the remaining credit hours to complete a program

total = 64

name = input("Enter student name: ")
degree = input("Enter degree name: ")
completed = float(input("Enter credits completed: "))

left = total - completed

print("Pass 'Em State College")
print(name, "is in the", degree, "program and has", left, "credits left to graduate")


