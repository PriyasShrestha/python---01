salary = int(input('Enter the salary'))

if salary <= 250000 and salary>0:
    print('annual Income: {salary}')
    print('Taxable Income()%:0')
    print('Remaining Amount= {salary}' )

elif salary >= 250000 and salary <=500000:
    print(f'annual Income: {salary}')
    tax=salary*.05
    print(f'Taxable Income(5)%:{tax}')
    Remaining=salary-tax
    print(f'Remaining Amount= {Remaining}' )

elif salary >= 500000 and salary < 1000000:
    print(f'annual Income: salary')
    tax=salary*.2
    print(f'Taxable Income()%:{tax}')
    Remaining=salary-tax
    print(f'Remaining Amount= {Remaining}' )

elif salary > 1000000:
    print(f'annual Income: salary')
    tax=salary*.3
    print(f'Taxable Income()%:{tax}')
    Remaining=salary-tax
    print(f'Remaining Amount= {Remaining}' )

else :
    print(f'Salary should be in postive number')