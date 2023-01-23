# Task 4.1

from random import randint

with open("marks.txt", "w") as marks_txt:
    for i in range(1,301):
        individual_mark = randint(1,100)
        marks_txt.write(str(individual_mark) + "\n")

counter = 0
with open("marks.txt", "r") as marks_txt:
    marks_data = marks_txt.readlines()
    for mark in marks_data:
       if int(mark) >=70:
           counter += 1
print(counter)

