name = input('请输入您的名字:')

with open('guest.txt', 'a') as file:
    file.write(name)