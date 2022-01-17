import math

def sum_() :
    num1=float(input("Enter the first number.......  "))
    num2=float(input("Enter the second number.......  "))
    s=num1 + num2
    print(f"Sum of {num1 }and {num2 } is =  ",s)

def sub() :
    num1=float(input("Enter the first number.......  "))
    num2=float(input("Enter the second number.......  "))
    s=num1 - num2
    print(f"Difference of {num1 }and {num2 } is = ",s)

def prod() :
    num1=float(input("Enter the first number.......  "))
    num2=float(input("Enter the second number.......  "))
    s=num1 * num2
    print(f"Product of {num1} and {num2} is = ",s)

def div() :
    num1=float(input("Enter the first number.......  "))
    num2=float(input("Enter the second number.......  "))
    s=num1 / num2
    rem=num1 % num2
    print(f"Quotient of {num1 }and {num2 } is= ",s)
    print("Remender","= ",rem)

def intdiv() :
    num1=float(input("Enter the first number.......  "))
    num2=float(input("Enter the second number.......  "))
    s=num1 // num2
    rem=num1 % num2
    print(f"Integer Quotient of {num1} and {num2} is  = ",s)
    print("Remender","= ",rem)

def pow() :
    num1=float(input("Enter the first number.......  "))
    num2=float(input("Enter the power.......  "))
    s=num1 ** num2
    print(f"{ num1 }to the power { num1}= ",s)

def complax():
    num1=float(input("Enter the first number.......  "))
    num2=float(input("Enter the second number.......  "))
    a=num1 + num3
    b=num2 + num4
    print(num1,op,num2,"= ",s)

def exp() :
    num1=float(input("Enter the power of e.......  "))
    
    s=2.718281828459045**num1 
    print(f"the value of{num1} power of e is = ",s)

def summession() :
    num1=float(input("Enter the first number.......  "))
    num2=float(input("Enter the second number.......  "))

    s=0
    for itr in range(num1,num2+1) :
        s=s+itr
    print("Summession = ",s)

def sqrt() :
    num1=float(input("Enter the first number.......  "))
    
    s=math.sqrt(num1)
    print(f"square root of {num1}= ",s)

def fact() :
    num1=float(input("Enter the first number.......  "))
    
    s=1
    for itr in range(1,num1+1) :
        s*=itr
    print(f"factorial of {num1}= ",s)

def square() :
    num1=float(input("Enter the  number.......  "))
    
    s=num1*num1
    print(f"Square of {num1 } =  ",s)

def log() :
    num1=float(input("Enter the number to find its log value.......  "))
    
    s=math.log10(num1)
    print(f"log of {num1 }=  ",s)

def cube() :
    num1=float(input("Enter the number to find its cube.......  "))
    
    s=num1*num1*num1
    print(f"cube of {num1} is =  ",s)

def cube_root() :
    num1=int(input("Enter the number.......  "))

    for itr in range(num1//2) :
        if itr*itr*itr==num1 :
            print(f"cube root of {num1} is =  ",itr)
