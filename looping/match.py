number=int(input('Enter the number'))

match number:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tueday')
    case 4:
        print('wedday')
    case 5:
        print('thusday')
    case 6:
        print('friday')
    case 7 :
        print('saturday')
    case _:
        print('invalid number')
