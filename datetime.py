import datetime
print(datetime.datetime.now())
a = datetime.datetime.now()
b = datetime.datetime(1975,1,1)
c = a - b
txt = str(c)
txt1 = txt[:5]
print(txt1,"Days")
print(int(int(txt1)/365),"Years")
print(int(int(txt1)/30.5),"Months")

a = 8
b = 3
mat = a if a > b else b ; print(mat)

g = 7

s = ''

s = 'true' if g < 10 else 'false'; print(s)

