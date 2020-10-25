def max (number1,number2):
   if number1>number2:
       result=number1
   elif number2>number1:
       result=number2
   return result
number1 = int(input("Number1 : "))
number2 = int(input("Number2 : "))
result = max(number1,number2)
print("Maximum is "+ str(result))
