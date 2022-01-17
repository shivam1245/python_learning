import calc_fun

print(".............................Welcome To Our Calculator..................................")
print()
print("To use this calculator follow the instructions")
print("Press  z  to quit")
print("Enter  s  for square root")
print("Enter  $  for square")
print("Enter  l  for log")
print("Enter  **  for power")
print("Enter  c  for  addition of complax number")
print("Enter  &  for finding the summesion of the range you want")
print("Enter  f  for finding the factorial of the ")
print("Enter  +  for addition")
print("Enter  -  for substraction")
print("Enter  /  for division")
print("Enter  *  for multiplication")
print("Enter  //  for integer division")

cnt=0

while True :
     
    op=input("Enter the operator to perform........  ")

    if op=='+' :
        print(calc_fun.sum_())
    elif op=='-' :
        print(calc_fun.sub())
    elif op=='*' :
        print(calc_fun.prod())
    elif op=='/' :
        print(calc_fun.div())
    elif op=='//' :
        print(calc_fun.intdiv())
    elif op=='$' :
        print(calc_fun.sqrt())
    elif op=='**' :
        print(calc_fun.pow())
    elif op=='e' :
        print(calc_fun.exp())
    elif op=='s' :
        print(calc_fun.square())
    elif op=='c' :
        print(calc_fun.cube())
    elif op=='***' :
        print(calc_fun.cube_root())
    elif op=='l' :
        print(calc_fun.log())
    elif op=='&' :
        print(calc_fun.summession())
    elif op=='f' :
        print(calc_fun.fact())
    elif op=='z' :
        if cnt>0 :
            print("*************************Thanks For Using Our calculator !*****************************")
        else :
            print()
            print("You wasted our time")
        break
    else :
        print("Invalid Input!")
    cnt+=1
