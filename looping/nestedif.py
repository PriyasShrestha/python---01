attandance=int(input('Enter the attandance'))
internal_marks=float(input('Enter tha marks'))

if attandance >= 75:
    if internal_marks >=40:
        print('You are eligible')
    else:
   
        print("your internal marks is low")

else:
    print("Not eligible for exam")