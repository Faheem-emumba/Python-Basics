# Simple Calculator

#function implementation
def calculate(operant1 , operant2 , desired_operator):
    if desired_operator == '+':
        return operant1 + operant2
    elif desired_operator == '-':
        return operant1- operant2
    elif desired_operator == '*':
        return operant1 * operant2
    elif desired_operator == '/':
        return operant1 / operant2    
    else:
        print("invalid operator entered")

#actual usage of function
print("Please enter the operants ")

num1= int(input("Enter operant 1 : "))
num2= int(input("Enter operant 2 : "))

operator = input("Please enter your desired operator from  + , - , * ,/ " )

print("Your answer is : ", calculate(num1,num2,operator))