with open('reason.txt', 'a') as file:
    while True:
        why = input("为什么喜欢编程('q'键退出):")
        if why == 'q':
            break
        why += '\n'
        file.write(why)
