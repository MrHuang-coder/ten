with open('English Novel.txt',encoding='utf-8') as file:
    message = file.read()
    print(message.lower().count('the'))
