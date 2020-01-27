with open('learning_Python.txt') as file:
    message = file.read()

with open('learning_Python.txt', 'w') as file:
    message = message.replace('Python', 'C')
    file.write(message)

with open('learning_Python.txt') as file:
    print(file.read())
