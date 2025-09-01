def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y != 0:
        return x/y
    else:
        return "Division by zero error"
    

print("======simple calculator======")
print("Select operation.")
print("1. ADD (+)")
print("1. Dsubstraction (-)")
print("3. multiplication (*)")
print("4. division (/)")

op = input("enter your choice(+,-,*,/,) \n")

a = float(input("enter first number--> "))
b = float (input("enter a second number---> "))

if op =='+':
    result = add(a,b)

elif op == "-":
     result = subtract(a,b )

elif op =="*":
    result = multiply(a,b)

elif op =="/":
    result = divide(a,b)

print (f"youer answer is {result}")
