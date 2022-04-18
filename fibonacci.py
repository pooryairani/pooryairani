repeat = int(input('How many fibonacci number should be produced? : '))
firstnum = 0
secondnum = 1
print(firstnum)
print(secondnum)
for i in range(1,repeat+1):
    temp=secondnum
    secondnum+= firstnum
    firstnum = temp
    print(secondnum)
