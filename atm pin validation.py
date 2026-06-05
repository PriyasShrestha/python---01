pin = 1234
rem = 3

while rem > 0:
    new_pin = int(input('Enter the PIN: '))
    if new_pin == pin:
        print('Access granted')
        break
    else:
        rem =rem- 1
        print(f'Wrong PIN. {rem} attempts left.')

    if rem == 0:
        print('Card Blocked')
        break
