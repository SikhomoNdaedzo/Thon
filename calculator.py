#Simple calculator with user input

#add two numbers
def add(x,y):
    return x + y

# subtract two numbers
def subtrsct(x,y):
    return x-y

#multiples of two numbers
def multiply(x,y):
    return x*y

#divide two numbers
def divide(x,y):
    return(x/y)

#print maths operations menu amd take input from user
print("Select Operation:.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter your choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))

elif choice == '2':
    print(num1,"-",num2, '=',subtract(num1,num2))
    
elif choice == '3':
    print(num1,"*",num2,"=",multiply(num1,num2))
    
elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
    
else:
    print("Invalid Choice!")