print("Welcome to the Python Calculator!")

def calculate(number1,number2,operator):
    if operator == '+':
        answer = number1+number2
    elif operator == '-':
        answer = number1-number2
    elif operator == '*':
        answer =  number1*number2
    elif operator == '/':
        answer = number1/number2
        
    return answer


number1 = float(input("Enter first number: "))

operator = input("Enter operator (+,-,*,/): ")

number2 = float(input("Enter second number: "))

answer = calculate(number1,number2,operator)

print(number1,operator,number2)

print("=",answer)


