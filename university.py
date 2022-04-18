stnum = int(input('Please Enter student number: '))
stavg = int(input('Please Enter GPA of student: '))
stnum2 = 0
stavg2 = 0
con = input('Do You whanna Continue? Y or N: ')
if con == 'y':
    for i in range(1,9999):
        stnumtemp = int(input('Please Enter student number: '))
        stavgtemp = int(input('Please Enter GPA of student: '))
        if stavgtemp >= stavg:
            stnum2 = stnum
            stavg2 = stavg
            stnum = stnumtemp
            stavg = stavgtemp
        elif stavgtemp >= stavg2:
            stnum2 = stnumtemp
            stavg2 = stavgtemp
        if input('Do You Whanna Continue? Y or N: ') == 'n':
            print('the second student is number',stnum2,'with average:',stavg2)
            break 
elif con == 'n':
     print('You entere\' less than two student.')