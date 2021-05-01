a = float(input("Enter First Number : "))
b = float(input("Enter Second Number: "))
opr = str(input(("Enter Operation: (+, -, *, /:")))

if opr == "+":
 sum = a+b
if opr == "-":
 sum = a-b
if opr == "*":
    sum = a*b
if opr == "/":
 sum = a/b

print(sum)