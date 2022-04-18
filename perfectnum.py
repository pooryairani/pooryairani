con = 'y'
while con != 'n':
    sum = 0
    check = int(input('Please Enter a number: '))
    for i in range(1,int(check/2)+1):
        if check % i == 0:
            sum += i
    if sum == check:
        print('Yeah\' this is Perfect number')
    else:
        print('No that\'s not perfect number')
    con = input('Are you whanna continue? Y or N: ')