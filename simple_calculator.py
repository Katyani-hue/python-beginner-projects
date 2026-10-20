print('hello world')
print('I am Soli')
#Add Two Numbers
num1=int(input('enter the number: '))
num2=int(input('enter the number: '))
Sum=num1+num2
print(Sum)

#simple calculator
num1=float(input('enter the number: '))
num2=float(input('enter the number: '))
operator=input('Enter operator(Sum,Sub,Mul,Div): ')
Sum=num1+num2
Sub=num1-num2
Mul=num1*num2
if operator=='Sum':
	print('Result:',num1+num2)
elif operator=='Sub':	
	print('Result:',num1-num2)
elif operator=='Mul':
    print('Result: ',num1*num2)
elif operator=='Div':
      if num2!=0:
         print('Number is divisible.')
      else:
          print('Number is not divisible')
else:
  print('Invalid Operator')
  
  
   #SIMPLE CALCULATOR
   
print(" SIMPLE CALCULATOR ")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator!")
