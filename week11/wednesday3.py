
def sum(Total,userInput):
    return Total+userInput
numberOfValues=int(input("Number of values: "))
Total=0
for n in range(numberOfValues):
  userInput=int(input("Value"+str(n+1)+":"))
  Total=sum(Total,userInput)
print("The sum is : ",Total)