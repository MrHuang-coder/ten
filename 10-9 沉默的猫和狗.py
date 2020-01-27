try:
    file1_name = 'cats.txt'
    file2_name = 'dogs.txt'
    with open(file1_name) as file:
        print(file.read())
except FileNotFoundError:
    pass
else:
    try:
        with open(file2_name) as file:
            print(file.read())
    except FileNotFoundError:
        pass
