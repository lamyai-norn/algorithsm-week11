def sumFromTo(start,end):
  result=0
  if start>end:
    return 0
  else:
    for index in range(start,end+1):
       result=result+index
    return result
startValue=int(input("Start value : "))
endValue=int(input("End value : "))
print(sumFromTo(startValue,endValue))