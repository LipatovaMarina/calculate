def strToBin(st):
    b = ''
    for char in st:
        if char in '01':
            b += char
    return b

while True:
    print('Выберите логическое выражение:\n',
          'xor - ^\nand - &\nor - |\nnot - !\n',
          'Для завершения программы - ex')
    choice = input()
    if choice == '^':
        print('Введите два двоичных числа')
        a = '0b' + strToBin(input('1) '))
        b = '0b' + strToBin(input('2) '))
        print('1) ', a)
        print('2) ', b)
        print('=> ', bin(int(a, 2) ^ int(b, 2)))
    elif choice == '&':
        print('Введите два двоичных числа')
        a = '0b' + strToBin(input('1) '))
        b = '0b' + strToBin(input('2) '))
        print('1) ', a)
        print('2) ', b)
        print('=> ', bin(int(a, 2) & int(b, 2)))
        pass
    elif choice == '|':
        print('Введите два двоичных числа')
        a = '0b' + strToBin(input('1) '))
        b = '0b' + strToBin(input('2) '))
        print('1) ', a)
        print('2) ', b)
        print('=> ', bin(int(a, 2) | int(b, 2)))
        pass
    elif choice == '!':
        print('Введите двоичное число')
        a = '0b' + strToBin(input('1) '))
        print('1) ', a)
        print('=> ', bin(~int(a, 2)))
        pass
    elif choice == 'ex':
        break
print('Завершение программы')