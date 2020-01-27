with open('guest_book.txt', 'a') as file:
    while True:
        ask = input("请输入你的姓名('q'键退出):")
        if ask == 'q':
            break
        ask += '\n'
        print("您好！" + ask)
        file.write(ask)