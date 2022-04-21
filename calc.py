def calc(firstnum,secondnum,operator):
    if operator == "-":
       return firstnum - secondnum
    elif operator == "+":
        return firstnum + secondnum
    elif operator == "*":
        return firstnum * secondnum
    elif operator == "/":
        return firstnum / secondnum
    else:
        return "Please Enter a valid Operator"

for i in range(1,999999):
   print(calc(int(input("please enter a number: ")),int(input("please enter another one: ")),input("please enter an operator(-+*/): ")))
   if input("Are you continue? Y or N : ") == "n":
       break
