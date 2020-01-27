with open('learning_Python.txt') as file:
    contents = file.read()
    print(contents)

with open('learning_Python.txt') as file:
    for line in file:
        print(line.strip())

with open('learning_Python.txt') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())