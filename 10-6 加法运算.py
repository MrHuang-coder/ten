try:
    temp1 = int(input("请输入第一个整数:"))
    temp2 = int(input('请输入第二个整数:'))
except ValueError:
    print('请输入整数！')
else:
    sum = temp1 + temp2
