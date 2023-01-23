# Task 4.3

with open("swanseazoo.txt","r") as f:
    lines = [a.strip("\n") for a in f.readlines()]
    animals = []
    for i in range(0,len(lines)-3,3):
        animals.append([lines[i], lines[i+1], lines[i+2]])

print(animals)
count = 0
for animal in animals:
    if animal[2] == "North":
        count += int(animal[1])
print(count)
